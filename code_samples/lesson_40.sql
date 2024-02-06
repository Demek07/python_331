-- Lesson 40
-- 06.02.2024
-- SELECT, FROM, WHERE, ORDER BY, LIMIT, OFFSET
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


-- Лысые злодеи! Bad Characters ALIGN и Bald Hair
-- Сортировка по имени по возрастанию