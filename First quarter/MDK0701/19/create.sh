#!/bin/sh
set -eu

psql -v ON_ERROR_STOP=1 --username "postgres" --dbname "postgres" -h localhost <<-EOSQL
drop database if exists radiation;
create database radiation;
\c radiation

create schema data;
set search_path = 'data';
create table station(id integer, latitude double precision, longitude double precision);
alter table station add constraint pk_station_id primary key (id);

create table measurement_part(station integer, mark timestamp, value integer) partition by range(mark);
alter table measurement_part add constraint fk_measurement_station_id foreign key (station) references station(id);
create unique index ix_measurement_station_mark_value on measurement_part (station, mark, value);

create table shape (polygon integer, segment integer, latitude double precision, longitude double precision);
create index ix_shape_polygon on shape (polygon);
create index ix_shape_latitude on shape(latitude);
create index ix_shape_longitude on shape(longitude);

create table measurement_y2023m04 partition of measurement_part for values from ('2023-04-01') to ('2023-05-01');
create table measurement_y2023m05 partition of measurement_part for values from ('2023-05-01') to ('2023-06-01');
create table measurement_y2023m06 partition of measurement_part for values from ('2023-06-01') to ('2023-07-01');
create table measurement_y2023m07 partition of measurement_part for values from ('2023-07-01') to ('2023-08-01');
create table measurement_y2023m08 partition of measurement_part for values from ('2023-08-01') to ('2023-09-01');
create table measurement_y2023m09 partition of measurement_part for values from ('2023-09-01') to ('2023-10-01');
create table measurement_y2023m10 partition of measurement_part for values from ('2023-10-01') to ('2023-11-01');
create table measurement_y2023m11 partition of measurement_part for values from ('2023-11-01') to ('2023-12-01');
create table measurement_y2023m12 partition of measurement_part for values from ('2023-12-01') to ('2024-01-01');


create view station_stats as
select station, count(*) as measurement 
from measurement_part 
group by station;

\COPY station (id, latitude, longitude) FROM 'all_stations.csv' CSV;
\COPY measurement_part (station, mark, value) FROM 'stations_data_consolidated.csv' CSV;

EOSQL
