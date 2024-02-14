--CREATE DATABASE radiation;


CREATE SCHEMA data;
SET search_path = 'data';

-- Создание таблицы для станций
CREATE TABLE station (
    id INTEGER PRIMARY KEY,
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION
);

-- Создание таблицы для измерений с разбиением по времени
CREATE TABLE measurement_part (
    station INTEGER,
    mark TIMESTAMP,
    value INTEGER,
    PRIMARY KEY (station, mark, value)
) PARTITION BY RANGE (mark);

-- Добавление внешнего ключа для связи с таблицей станций
ALTER TABLE measurement_part 
ADD CONSTRAINT fk_measurement_station_id 
FOREIGN KEY (station) 
REFERENCES station (id);

-- Создание таблицы для геометрических данных
CREATE TABLE shape (
    polygon INTEGER,
    segment INTEGER,
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION
);

-- Создание индексов
CREATE INDEX idx_shape_polygon ON shape (polygon);
CREATE INDEX idx_shape_latitude ON shape (latitude);
CREATE INDEX idx_shape_longitude ON shape (longitude);

-- Создание таблицы-партиции для измерений за апрель 2023 года
CREATE TABLE measurement_2023m04 PARTITION OF measurement_part 
FOR VALUES FROM ('2023-04-01') TO ('2023-05-01');

-- Аналогично 
CREATE TABLE measurement_2023m05 PARTITION OF measurement_part 
FOR VALUES FROM ('2023-05-01') TO ('2023-06-01');

CREATE TABLE measurement_2023m06 PARTITION OF measurement_part 
FOR VALUES FROM ('2023-06-01') TO ('2023-07-01');

CREATE TABLE measurement_2023m07 PARTITION OF measurement_part 
FOR VALUES FROM ('2023-07-01') TO ('2023-08-01');

CREATE TABLE measurement_2023m08 PARTITION OF measurement_part 
FOR VALUES FROM ('2023-08-01') TO ('2023-09-01');

CREATE TABLE measurement_2023m09 PARTITION OF measurement_part 
FOR VALUES FROM ('2023-09-01') TO ('2023-10-01');

CREATE TABLE measurement_2023m10 PARTITION OF measurement_part 
FOR VALUES FROM ('2023-10-01') TO ('2023-11-01');

CREATE TABLE measurement_2023m11 PARTITION OF measurement_part 
FOR VALUES FROM ('2023-11-01') TO ('2023-12-01');

CREATE TABLE measurement_2023m12 PARTITION OF measurement_part 
FOR VALUES FROM ('2023-12-01') TO ('2024-01-01');