-- Lesson 42 13.02.2024
-- Разбор [[PYTHON331 HW №25]]
-- Поля, типы данных, первичные ключи
-- Создание 1 таблицы
-- CRUD для одной таблицы
-- Transaction
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

-- Вставка данных (Работать не будет, имя не задали)
INSERT INTO User (last_name, age, address, table_number)
VALUES ('Чебатков', 30, 'ул. Пушкина, д. Колотушкина', 1);

-- Запишет пустую строку в имя. Это не будет ошибкой. :(
INSERT INTO User (first_name, last_name, age, address, table_number)
VALUES ('', 'Чебатков', 30, 'ул. Пушкина, д. Колотушкина', 1),
('Иван', 'Иванов', 25, 'ул. Ленина, д. 1', 2);

-- UPDATE - обновление данных Добавим в id 1 имя Евгений
UPDATE User
SET first_name = 'Евгений'
WHERE id = 1;

UPDATE User
SET first_name = 'Сергей'

-- DELETE - удаление данных Удалим Петра Чебаткова
-- Лучше это делать по первичному ключу, но я сделаю это так
DELETE FROM User
WHERE first_name = 'Петр' AND last_name = 'Чебатков';

-- BEGIN TRANSACTION - начало транзакции
-- COMMIT - подтверждение транзакции
-- ROLLBACK - откат транзакции

-- Допустим я хочу создать новую таблицу UserNew, которая будет иметь middle_name default NULL
-- И перенести данные из таблицы User в таблицу UserNew
-- Это можно сделать безопасно, используя транзакции

-- Начнем транзакцию
BEGIN TRANSACTION;

-- Создадим новую таблицу
CREATE TABLE UserNew (
id INTEGER PRIMARY KEY AUTOINCREMENT,
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
middle_name TEXT DEFAULT NULL,
age INTEGER NOT NULL,
address TEXT,
table_number INTEGER UNIQUE
);

-- Вставим данные из таблицы User в таблицу UserNew
INSERT INTO UserNew (first_name, last_name, age, address, table_number)
SELECT first_name, last_name, age, address, table_number
FROM User;

-- Удалим таблицу User
DROP TABLE User;

-- Переименуем таблицу UserNew в User
ALTER TABLE UserNew RENAME TO User;

-- Сделаем выборку из таблицы User
SELECT * FROM User;

-- Откатим транзакцию
ROLLBACK;

-- Подтвердим транзакцию
COMMIT;

-- Пересоздадим таблицу User, сделаем table_number_id внешним ключом
-- Сделаем таблицу Table, c table_number первичным ключем и table_data (содержимое личного дела) default NULL

CREATE TABLE Tabledata (
table_number TEXT PRIMARY KEY,
table_data TEXT DEFAULT NULL
);

CREATE TABLE User (
id INTEGER PRIMARY KEY AUTOINCREMENT,
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
middle_name TEXT DEFAULT NULL,
age INTEGER NOT NULL,
address TEXT,
table_number TEXT,
FOREIGN KEY (table_number) REFERENCES Tabledata(table_number)
);

-- Таблица с паспортными данными составной первичный ключ (серия номер паспорта) и внешний ключ User.id
CREATE TABLE Passport (
passport_series TEXT,
passport_number TEXT,
user_id INTEGER,
FOREIGN KEY (user_id) REFERENCES User(id),
PRIMARY KEY (passport_series, passport_number)
);
