--    Создание таблицы city:
--        Поля: id (первичный ключ), city_name, lat, lon, population, subject_id (внешний ключ), district_id (внешний ключ).
--        Создание индекса для city_name.
--
--    Создание таблиц subject и district:
--        Для каждой таблицы должен быть указан первичный ключ.

-- subject
CREATE TABLE IF NOT EXISTS subject (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_name TEXT NOT NULL
);

-- district
CREATE TABLE IF NOT EXISTS district (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    district_name TEXT NOT NULL
);

-- city

CREATE TABLE IF NOT EXISTS city (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city_name TEXT NOT NULL,
    lat REAL NOT NULL,
    lon REAL NOT NULL,
    population INTEGER NOT NULL,
    subject_id INTEGER NOT NULL,
    district_id INTEGER NOT NULL,
    FOREIGN KEY (subject_id) REFERENCES subject(id),
    FOREIGN KEY (district_id) REFERENCES district(id)
);

-- Содание индекса для city_name
CREATE INDEX IF NOT EXISTS city_name ON city(city_name);
