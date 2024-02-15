-- Lesson 43 15.02.2024
-- Работа с несколькими таблицами
-- JOIN, LEFT JOIN, RIGHT JOIN
-- UNION ?
-- CRUD для нескольких таблиц

-- Сделаем таблицу с котиками
-- id, name, shop_id
CREATE TABLE Cats (
id INTEGER,
name TEXT,
shop_id INTEGER
);

-- Сделаем таблицу с магазинами
-- id, name
CREATE TABLE Shops (
id INTEGER,
name TEXT
);

-- Добавим 5 котиков
-- у последнего будет shop_id = 10
INSERT INTO Cats (id, name, shop_id)
VALUES (1, 'Мурзик', 1),
(2, 'Барсик', 1),
(3, 'Матроскин', 2),
(4, 'Булочка', 2),
(5, 'Батон', 10);

-- Добавим 5 магазинов
INSERT INTO Shops (id, name)
VALUES (1, 'Зоомагазин Усы и хвост'),
(2, 'Зоомагазин Зоомир'),
(3, 'Зоомагазин Котомир'),
(4, 'Зоомагазин Золотая рыбка'),
(5, 'Зоомагазин Котопес');

-- Выведем всех котиков
select * from cats;

-- Выведем всех котиков + названия магазинов
-- JOIN - объединение таблиц
-- Аналогично INNER JOIN
SELECT Cats.name AS Котик, Shops.name AS Магазин
FROM Cats, Shops
WHERE Cats.shop_id = Shops.id;

-- JOIN - по-умолчанию = INNER JOIN
-- INNER JOIN - внутреннее объединение - Даст ВСЕХ котиков, у которых есть магазин
SELECT Cats.name AS Котик, Shops.name AS Магазин
FROM Cats
INNER JOIN Shops ON Cats.shop_id = Shops.id;


-- LEFT JOIN - левое объединение - Даст ВСЕХ котиков, даже тех, у кого нет магазина
SELECT Cats.name AS Котик, Shops.name AS Магазин
FROM Cats
LEFT JOIN Shops ON Cats.shop_id = Shops.id;

-- RIGHT JOIN - правое объединение - Даст ВСЕ магазины, даже те, в которых нет котиков
SELECT Cats.name AS Котик, Shops.name AS Магазин
FROM Cats
RIGHT JOIN Shops ON Cats.shop_id = Shops.id;

-- FULL JOIN - полное объединение - Даст ВСЕХ котиков и ВСЕ магазины
SELECT Cats.name AS Котик, Shops.name AS Магазин
FROM Cats
FULL JOIN Shops ON Cats.shop_id = Shops.id;

-- Модифицируем эти таблицы
-- Добавим первичные ключи и внешний ключ

-- Удалим таблицы
DROP TABLE Cats;
DROP TABLE Shops;


CREATE TABLE Cats (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
shop_id INTEGER
FOREIGN KEY (shop_id) REFERENCES Shops(id)
);

-- Сделаем таблицу с магазинами
-- id, name
CREATE TABLE Shops (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT
);

INSERT INTO Cats (name, shop_id)
VALUES ('Мурзик', 1),
('Барсик', 1),
('Матроскин', 2),
('Булочка', 2),
('Батон', 10);

INSERT INTO Shops (name)
VALUES ('Зоомагазин Усы и хвост'),
('Зоомагазин Зоомир'),
('Зоомагазин Котомир'),
('Зоомагазин Золотая рыбка'),
('Зоомагазин Котопес');

-- Добавим котика Маффин в магазин Зоомагазин Золотая рыбка так, чтобы ID добылся автоматически
INSERT INTO Cats (name, shop_id)
VALUES ('Маффин', (
    SELECT id
    FROM Shops
    WHERE name = 'Зоомагазин Золотая рыбка')
);

-------------------------------------------------------
-------------------------------------------------------
-- Отношения между таблицами
-- Один ко многим - One to Many - КОгда один объект в одной таблице связан с несколькими объектами в другой таблице
-- Один ко одному - One to One - Когда один объект в одной таблице связан с одним объектом в другой таблице
-- Многие ко многим - Many to Many - Когда несколько объектов в одной таблице связаны с несколькими объектами в другой таблице

-- Пример ВУЗа. Студенты - Паспорта. Один студент - один паспорт. Один паспорт - один студент.
-- One to One

CREATE TABLE Students (
id INTEGER PRIMARY KEY AUTOINCREMENT,
passport_id INTEGER NOT NULL UNIQUE,
name TEXT NOT NULL,
FOREIGN KEY (passport_id) REFERENCES Passports(id)
);

CREATE TABLE Passports (
id INTEGER PRIMARY KEY AUTOINCREMENT,
series_number TEXT NOT NULL UNIQUE,
date_of_issue TEXT NOT NULL,
department TEXT NOT NULL
);

-- Добавим паспорт
INSERT INTO Passports (series_number, date_of_issue, department)
VALUES ('1234 567890', '01.01.2000', 'Отделение УФМС по г. Москва');

-- Добавим студента
INSERT INTO Students (passport_id, name)
VALUES (1, 'Иванов Иван Иванович');

-- Читаем студента и его паспорт
SELECT Students.name AS Студент, Passports.series_number AS Паспорт
FROM Students
JOIN Passports ON Students.passport_id = Passports.id;


BEGIN TRANSACTION;

INSERT INTO Passports (series_number, date_of_issue, department)
VALUES ('4321 123456', '2020-01-01', 'Отделение №1');

INSERT INTO Students (name, passport_id)
VALUES ('Николаева Анна Степановна', (SELECT id FROM Passports WHERE series_number = '4321 123456'));

COMMIT;

-- Поменяем паспортные данные Анны, найдя её по имени, по id паспорта, и изменим номер паспорта на '4321 654321'
UPDATE Passports
SET series_number = '4321 654321'
WHERE id = (SELECT passport_id FROM Students WHERE name = 'Николаева Анна Степановна');

-- Поменяем фамилию Анны (вышла замуж), найдя её по номеру паспорта в нашей базе
UPDATE Students
SET name = 'Степанова Анна Петровна'
WHERE passport_id = (SELECT id FROM Passports WHERE series_number = '4321 654321');

-- Виртуальная таблица - VIEW
-- Создадим виртуальную таблицу, которая будет содержать имена студентов и их паспортные данные
CREATE VIEW StudentsPassports AS
SELECT Students.name AS Студент, Passports.series_number AS Паспорт
FROM Students
JOIN Passports ON Students.passport_id = Passports.id;

-- Выведем содержимое виртуальной таблицы
SELECT * FROM StudentsPassports;

-- Добавим еще студента
BEGIN TRANSACTION;

INSERT INTO Passports (series_number, date_of_issue, department)
VALUES ('2233 234456', '2020-01-01', 'Отделение №1');

INSERT INTO Students (name, passport_id)
VALUES ('Смирнова Александра Павловна', (SELECT id FROM Passports WHERE series_number = '2233 234456'));

COMMIT;

-- Удалим паспорт Александры Павловны
DELETE FROM Passports
WHERE series_number = '2233 234456';

-- Это сделать мы не можем. Но мы можем удалить студента, а затем удалить паспорт
-- Или изменить поведение внешнего ключа, разрешить Null, и установить поведение при удалении

-- One to Many - Один ко многим
-- Факультеты. Один факультет - много студентов. Много студентов - один факультет.

CREATE TABLE Faculties (
name TEXT PRIMARY KEY,
director TEXT NOT NULL
);

CREATE TABLE Students (
id INTEGER PRIMARY KEY AUTOINCREMENT,
faculty TEXT DEFAULT "Без факультета",
name TEXT NOT NULL,
FOREIGN KEY (faculty) REFERENCES Faculties(name) ON DELETE SET DEFAULT ON UPDATE CASCADE
);

-- Варианты действий в таблице на которую ссылается внешний ключ
-- DELETE - удаление записи
-- UPDATE - изменение записи

-- Варианты поведения при работе с данными в таблице на которую ссылается внешний ключ
-- CASCADE - каскадное изменение
-- SET NULL - установить NULL
-- SET DEFAULT - установить значение по-умолчанию
-- RESTRICT - запретить изменение
-- NO ACTION - ничего не делать

-- Добавим факультеты 3 штуки
INSERT INTO Faculties (name, director)
VALUES ('Факультет Информационных Технологий', 'Иванов Иван Иванович'),
('Факультет Экономики', 'Петров Петр Петрович'),
('Факультет Математики', 'Сидоров Сидор Сидорович');

-- Добавим студентов
INSERT INTO Students (faculty, name)
VALUES ('Факультет Информационных Технологий', 'Сергеев Петр Алекандрович'),
('Факультет Информационных Технологий', 'Безруков Станислав Сергеевич'),
('Факультет Экономики', 'Уколов Петр Леонидович'),
('Факультет Математики', 'Макаренко Анна Сергеевна'),
('Факультет Математики', 'Монин Валентин Прохорович'),
('Факультет Математики', 'Сидорова Сидора Сидоровна');

-- Переименуем факультет Экономики в Факультет Экономики и Финансов
UPDATE Faculties
SET name = 'Факультет Экономики и Финансов'
WHERE name = 'Факультет Экономики';

-- Удалим факультет Факультет Экономики и Финансов
DELETE FROM Faculties
WHERE name = 'Факультет Экономики и Финансов';

-- Нельзя. Потому что это внешний ключ, и он указывает на таблицу с факультетами, а факультета
-- с названием Без факультета у нас нет. Мы можем изменить поведение внешнего ключа, разрешить Null, и установить поведение при удалении
-- или добавить факультет Без факультета

-- Добавим факультет Без факультета
INSERT INTO Faculties (name, director)
VALUES ('Без факультета', 'Неизвестно');


-- Проверяем версию с Null

CREATE TABLE Faculties (
name TEXT PRIMARY KEY,
director TEXT NOT NULL
);

CREATE TABLE Students (
id INTEGER PRIMARY KEY AUTOINCREMENT,
faculty TEXT DEFAULT NULL,
name TEXT NOT NULL,
FOREIGN KEY (faculty) REFERENCES Faculties(name) ON DELETE SET DEFAULT ON UPDATE CASCADE
);

DELETE FROM Faculties
WHERE name = 'Факультет Экономики';

-- Многие ко многим - Many to Many
CREATE TABLE Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    last_name TEXT NOT NULL
    -- Другие поля, связанные со студентом
);

CREATE TABLE Teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    last_name TEXT NOT NULL
    -- Другие поля, связанные с учителем
);

CREATE TABLE StudentsTeachers (
    student_id INTEGER,
    teachers_id INTEGER,
    PRIMARY KEY (student_id, teachers_id),
    FOREIGN KEY (student_id) REFERENCES Students (id)
        ON DELETE CASCADE
        ON UPDATE NO ACTION,
    FOREIGN KEY (teachers_id) REFERENCES Teachers (id)
        ON DELETE CASCADE
        ON UPDATE NO ACTION
);
