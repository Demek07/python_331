-- Lesson 42 13.02.2024
-- Разбор [[PYTHON331 HW №25]]
-- Поля, типы данных, первичные ключи
-- Создание 1 таблицы
-- CRUD для одной таблицы
-- Аномалии при работе с 1 таблицей
-- Нормальные формы
-- Создание нескольких таблиц
-- Вставка данных в несколько таблиц (по очереди)
-- Чтение данных через JOIN
-- Вставка данных через JOIN
-- Задание на неделю - причесать марвел таблицу


-- Создание максимально простой таблицы
-- CREATE TABLE User - создание таблицы

CREATE TABLE User (
first_name TEXT,
last_name TEXT,
age INTEGER
);

-- CRUD для одной таблицы

-- Вставка данных
-- INSERT INTO User - вставка данных
INSERT INTO User (first_name, last_name, age)
VALUES ('Евгений', 'Чебатков', 30);

-- Вставляем несколько строк
INSERT INTO User (first_name, last_name, age)
VALUES ('Иван', 'Иванов', 25),
('Петр', 'Петров', 35);

-- Вставка неполных данных
INSERT INTO User (first_name, last_name)
VALUES ('Сидора', 'Сидорова');

-- Что такое PRIMARY KEY - первичный ключ - уникальный идентификатор строки
-- Может быть только один первичный ключ, но он может состоять из нескольких столбцов
-- Переписываем таблицу с первичным ключом

-- DROP TABLE - удаление таблицы
DROP TABLE User;

-- Создание таблицы с первичным ключом
CREATE TABLE User (
id INTEGER PRIMARY KEY AUTOINCREMENT, -- autoincrement - первичный ключ будет автоматически увеличиваться
first_name TEXT NOT NULL, -- not null - обязательное поле
last_name TEXT NOT NULL,
age INTEGER NOT NULL,
address TEXT,
table_number INTEGER UNIQUE -- уникальный столбец
);