drop table if exists kalman_state;
drop table if exists daily_samples;

create unlogged table kalman_state(kid integer primary key, kx float, kcov float, kR float, kQ float);

create or replace function kalman(id integer, z float) returns float language plpgsql as $$
declare
    x float;
    cov float;
    predX float;
    predCov float;
    K float;
    u float = 0.0;
    R float;
    Q float;
    A float = 1.0;
    B float = 0.0;
    C float = 1.0;
begin
	select kx, kcov, kR, kQ from kalman_state where kid = id into x, cov, R, Q;
	if x is null then
		x = 1.0 / C * z;
		cov = 1.0 / C * Q * (1 / C);
	else
		predX = A * x + B * u;
		predCov = A * cov * A + R;
		K = predCov * C * (1.0 / (C * predCov * C + Q));
		x = predX + K * (z - C * predX);
		cov = predCov - K * C * predCov;
	end if;
	update kalman_state set kx = x, kcov = cov where kid = id;
	return x;
end
$$;

create unlogged table daily_samples (station int, mark timestamp, samples int, mean float, filtered float);

create or replace function daily_average(sta int, ts timestamp) returns table (samples int, value float) language sql as 
$$
    select count(value), avg(value) from data.measurement_part
      where station = sta and mark between ts and ts + interval '1 day';
$$;

create or replace function interpolate_average(sta int, ts timestamp) returns float language sql as
$$
    with lerp (p, a, b) as (
	with row1(t, v) as (
		select mark, mean from daily_samples 
		where mark <= ts and station = sta and samples > 0 order by mark desc limit 1
	), row2 (t, v) as (
	    select mark, mean from daily_samples
	        where mark >= ts and station = sta and samples > 0 order by mark asc limit 1
	)
	select extract(epoch from ts - row1.t) / coalesce(nullif(extract(epoch from row2.t - row1.t), 0), 1),
            row1.v, row2.v from row1, row2
    )
    select a + (b - a) * p from lerp;
$$;

create or replace function filter_station(sta integer) returns void language sql as
$$
    with seq(st, mk, vl) as (select station, mark, mean from daily_samples where station = sta order by mark asc)
        update daily_samples set filtered = kalman(station, mean) from seq where station = st and mark = mk;
$$;

create or replace procedure generate_daily() language sql as $$
    truncate table daily_samples;
    with station_date_list (sta, ts) as 
    (
	with station_interval (sta, lo, hi) as
	    (select station, date_trunc('day', min(mark)), date_trunc('day', max(mark)) from data.measurement_part group by station)
	select sta, lo + interval '1 day' * ofs from station_interval, generate_series(0, extract('days' from hi - lo)::int) as ofs
    )
    insert into daily_samples
        select sta, ts, samples value from station_date_list, daily_average(sta, ts);

    update daily_samples set mean = interpolate_average(station, mark) where samples = 0;
    truncate table kalman_state;
    insert into kalman_state (kid, kR, kQ) select station, 1.0, stddev(mean) * 3.0 from daily_samples group by station;
    select filter_station(station) from daily_samples group by station;
$$;

call generate_daily();