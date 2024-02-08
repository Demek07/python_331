-- Lesson 41
-- 08.02.2024
-- Like
-- Функции
-- count
-- HAVING

--, подзапросы, триггеры, виртуальные таблицы?


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

-- Like - поиск по шаблону
-- % - любое количество символов
-- _ - один символ


-- TODO Поищем like FIRST_APPEARANCE  оканчивается на 62
SELECT name
FROM MarvelCharacters
WHERE FIRST_APPEARANCE LIKE '%62';

-- Посчитаем сколько персонажей впервые появились в августе 1962
-- В результате мы получим новый столбец aug62 с количеством персонажей (одна строка)
SELECT count(*) aug62
FROM MarvelCharacters
WHERE FIRST_APPEARANCE LIKE 'aug-62';


-- Мы можем группировать строки по значениям столбца
-- Этот запрос выполняется дольше, чем DISTINCT, но позволяет использовать агрегатные функции
SELECT hair
FROM MarvelCharacters
GROUP BY hair;

-- Посчитаем сколько персонажей с каким цветом волос
-- Сортируем по убыванию
SELECT hair, count(*) total
FROM MarvelCharacters
GROUP BY hair
ORDER BY total DESC

-- Посчитаем сколько персонажей с каким цветом волос
-- Сортируем по убыванию
-- Выведем только те, у которых больше 50
SELECT hair, count(*) total
FROM MarvelCharacters
WHERE hair not null
GROUP BY hair
HAVING total > 50
ORDER BY total DESC

-- TODO - Сделайте подобную операцию по identify