create schema if not exists clustering;
set search_path = 'clustering';

drop procedure if exists fill_table;
drop procedure if exists generate_points;
drop procedure if exists assign_cluster_at_point;
drop procedure if exists assign_clusters;

drop function if exists distance_from_point;
drop function if exists points_close_to_point;

drop view if exists cluster_info;

drop table if exists points;

create table points (id serial primary key, x float, y float, cluster integer);

create view cluster_info as
    select cluster, avg(x) as cx, avg(y) as cy, count(id) as pts from points group by cluster;

create procedure generate_points(x0 float, y0 float, r float, n integer) language sql as $$
    with vec(dir, ofs) as (select random() * 2 * pi(), random() from generate_series(1, n))
        insert into points (x, y) select x0 + r * cos(dir) * ofs, y0 + r * sin(dir) * ofs from vec;
$$;

create procedure fill_table() language sql as $$
    delete from points;
    call generate_points(3, 3, 1, 100);
    call generate_points(5, 5, 1, 100);
    call generate_points(7, 7, 1, 100);
$$;

create function distance_from_point(i integer) returns table (id integer, dist float) language sql as $$
    with p (x, y) as (select x, y from points where id = i)
        select id, sqrt((pi.x - p.x) * (pi.x - p.x) + (pi.y - p.y) * (pi.y - p.y)) as distance from points as pi, p;
$$;

create function points_close_to_point(i integer) returns table (id integer) language sql as
$$
    with p(x, y) as (select x, y from points where id = i)
        select id from points as pi, p where sqrt((pi.x - p.x) * (pi.x - p.x) + (pi.y - p.y) * (pi.y - p.y)) < 2;
$$;

create procedure assign_cluster_at_point(i integer, d float) language sql as $$
    with p(id, x0, y0) as (select id, x, y from points where id = i)
        update points set cluster = p.id from p where sqrt((x - p.x0) * (x - p.x0) + (y - p.y0) * (y - p.y0)) < d;
$$;

create procedure assign_clusters(d float) language sql as $$
    update points set cluster = null where cluster is not null;
    with pt(cid, x0, y0) as (update points set cluster = id where cluster is null returning id, x, y)
        update points set cluster = cid from pt where sqrt((x - x0) * (x - x0) + (y - y0) * (y - y0)) < d;
$$;

call fill_table();
call assign_clusters(2);
