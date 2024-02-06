-- Lesson 40
-- 06.02.2024
-- SELECT, FROM, WHERE, ORDER BY,
-- IN, BETWEEN, LIKE,
-- LIMIT, OFFSET
-- Структура таблицы Marvel
CREATE TABLE MarvelCharacters (
    id               INTEGER PRIMARY KEY AUTOINCREMENT,
    page_id          INTEGER,
    name             TEXT,
    urlslug          TEXT,
    identify         TEXT,
    ALIGN            TEXT,
    EYE              TEXT,
    HAIR             TEXT,
    SEX              TEXT,
    GSM              TEXT,
    ALIVE            TEXT,
    APPEARANCES      INTEGER,
    FIRST_APPEARANCE TEXT,
    Year             INTEGER
);

-- SELECT
-- Если название таблицы с цифры или есть пробелы - обязательно обернуть в кавычки или [ ]
SELECT * FROM MarvelCharacters;

-- Вытащим только столбцы имя, пол, и год
-- SQL - регистронезависимый язык.

SELECT name, SEX, YEAR  -- year записан в другом регистре но все работает
FROM MarvelCharacters

-- WHERE - условие
-- Выберем где год не null
SELECT name, SEX, year
FROM MarvelCharacters
WHERE YEAR not null

-- Выберем год 1962
SELECT name, SEX, year
FROM marvelcharacters
WHERE YEAR = 1962

-- Выберем год 1962 и пол not null
SELECT name, SEX
FROM MarvelCharacters
WHERE YEAR = 1962 AND SEX NOT null

-- ORDER BY - сортировка
-- Год НЕ равно 1962 и пол не null, отсортированный по году
SELECT name, SEX, year
FROM MarvelCharacters
WHERE YEAR != 1962 AND SEX NOT null
ORDER BY year

-- YEAR < 1944
-- Кроме = != AND NOT OR можно использовать < > <= >=
-- ORDER BY DESC - сортировка по убыванию
SELECT name, SEX, year
FROM MarvelCharacters
WHERE YEAR < 1944 AND SEX NOT null
ORDER BY year DESC

-- Поставим столбцы так как удобно нам, год, имя, пол
-- сделаем сортировку по году, полу по убыванию и имени
SELECT year, name, sex
FROM MarvelCharacters
WHERE YEAR < 1944 AND SEX NOT null
ORDER BY year, SEX DESC, name

-- Добавим псевдонимы для столбцов
-- Псевдонимы пишутся после названия столбца через пробел
SELECT year as 'Год', name as 'Имя', SEX as 'Пол'
FROM MarvelCharacters
WHERE YEAR < 1944 AND SEX NOT null
ORDER BY year, SEX DESC, name

-- TOOD: практика!
-- имя, год появления количество появлений девушки блондинки с голубыми глазами
-- Blond Hair, Blue Eyes сортировка по году, и по количеству появлений
SELECT name, year, APPEARANCES
FROM MarvelCharacters
WHERE HAIR = 'Blond Hair' AND EYE = 'Blue Eyes' AND SEX = 'Female Characters'
AND APPEARANCES not null AND YEAR not null
ORDER BY year DESC, APPEARANCES DESC
-- Лысые злодеи! Bad Characters ALIGN и Bald Hair
-- Сортировка по имени по возрастанию
SELECT name, year, APPEARANCES
FROM MarvelCharacters
WHERE HAIR = 'Bald' AND ALIGN = 'Bad Characters'
AND APPEARANCES not null AND YEAR not null
ORDER BY name

-- IN - входит в список
-- Blond Hair, Strawberry Blond Hair, Red Hair
SELECT name, hair
FROM MarvelCharacters
WHERE HAIR = 'Blond Hair' OR HAIR = 'Strawberry Blond Hair' OR HAIR = 'Red Hair'
--WHERE HAIR IN ('Blond Hair', 'Strawberry Blond Hair', 'Red Hair')
ORDER BY hair


-- Получим персонажей с голубыми или зелеными глазами ИЛИ с рыжими или светлыми волосами
SELECT name, hair, eye
FROM MarvelCharacters
WHERE HAIR OR EYE
IN ('Blond Hair', 'Strawberry Blond Hair', 'Red Hair', 'Blue Eyes', 'Green Eyes')
ORDER BY hair


-- BETWEEN - между 1940 и 1945 годом где год и количество появлений не null
-- Сортировка по году и количеству появлений
SELECT name, year, APPEARANCES
FROM MarvelCharacters
WHERE YEAR BETWEEN 1940 AND 1945 AND (year AND APPEARANCES not null)
ORDER BY year, APPEARANCES DESC

-- Частота появления между 4043 и 200 раз где количество появлений не null
-- Сортировка по количеству появлений
SELECT name, year, APPEARANCES
FROM MarvelCharacters
WHERE APPEARANCES BETWEEN 200 AND 4043

-- Уникальные значения - DISTINCT
-- Уникальные значения пола
SELECT DISTINCT SEX FROM MarvelCharacters

-- LIMIT - ограничение количества строк
-- OFFSET - смещение

SELECT DISTINCT EYE FROM MarvelCharacters
LIMIT 5 OFFSET 10