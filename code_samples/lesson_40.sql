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