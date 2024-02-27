--    Создание таблицы city:
--        Поля: id (первичный ключ), city_name, lat, lon, population, subject_id (внешний ключ), district_id (внешний ключ).
--        Создание индекса для city_name.
--
--    Создание таблиц subject и district:
--        Для каждой таблицы должен быть указан первичный ключ.

-- subject
CREATE TABLE subject (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_name TEXT NOT NULL
);

-- district
CREATE TABLE district (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    district_name TEXT NOT NULL
);

-- city
CREATE TABLE city (
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