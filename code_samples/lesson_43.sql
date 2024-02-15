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