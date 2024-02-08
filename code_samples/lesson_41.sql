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

-- AVG - среднее значение
-- Сделаем групировку по FIRST_APPEARANCE и посчитаем среднее APPEARANCES
SELECT FIRST_APPEARANCE month, AVG(APPEARANCES) avg_appearances
FROM MarvelCharacters
GROUP BY month
ORDER BY month DESC

-- MAX, MIN - максимальное и минимальное значение
-- Максимальное количество появлений персонажа + имя персонажа
SELECT name, FIRST_APPEARANCE month, MAX(APPEARANCES) max_appearances
FROM MarvelCharacters
GROUP BY month
ORDER BY max_appearances DESC


-- Минимальное количество появлений персонажа + имя персонажа
SELECT name, FIRST_APPEARANCE month, MIN(APPEARANCES) min_appearances
FROM MarvelCharacters
GROUP BY month
HAVING min_appearances > 5
ORDER BY min_appearances DESC

-- ROUND - округление
-- Округлим среднее количество появлений персонажа до 2 знаков после запятой
SELECT FIRST_APPEARANCE month, ROUND(AVG(APPEARANCES), 2) avg_appearances
FROM MarvelCharacters
GROUP BY month
ORDER BY month DESC


-- Максимальное количество появлений персонажа в каждом году + имя персонажа
SELECT name Имя, year Год, MAX(appearances) Макс_появления
FROM MarvelCharacters
WHERE Год not null
GROUP BY Год
ORDER BY Год

-- Подзапросы
-- Вложенный запрос
-- Выведем имена персонажей, у которых больше появлений, чем у персонажа с id 1
SELECT name
FROM MarvelCharacters
WHERE APPEARANCES > (SELECT APPEARANCES FROM MarvelCharacters WHERE id = 1)

-- Альтернатива группировке
-- Подзапрос возвращает максимальное количество появлений персонажа в 1970 году
-- Внешний запрос возвращает имя персонажа, год и количество появлений
SELECT name AS Имя, Year AS Год, APPEARANCES AS Макс_появления
FROM MarvelCharacters
WHERE Year = 1970 AND
APPEARANCES = (
SELECT MAX(APPEARANCES)
FROM MarvelCharacters
WHERE Year = 1970
)

-- Подзапрос возвращает среднее количество появлений персонажа * 100
-- Внешний запрос возвращает имя персонажа и количество появлений
-- В итоге мы имеем персонажей, у которых количество появлений больше, чем среднее количество появлений * 100
SELECT name, appearances
FROM MarvelCharacters
WHERE appearances > (
SELECT AVG(appearances) * 100
FROM MarvelCharacters
);