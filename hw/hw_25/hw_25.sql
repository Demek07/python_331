-- Задача 1: Лысые злодеи 90х годов
SELECT name, FIRST_APPEARANCE, APPEARANCES
FROM MarvelCharacters
WHERE HAIR = 'Bald' AND ALIGN = 'Bad Characters' AND Year BETWEEN 1990 AND 1999;

-- Задача 2: Герои с тайной идентичностью и необычными глазами
SELECT name, Year, EYE
FROM MarvelCharacters
WHERE identify = 'Secret Identity' AND EYE NOT IN ('Blue Eyes', 'Brown Eyes', 'Green Eyes');

-- Задача 3: Персонажи с изменяющимся цветом волос
SELECT name, HAIR
FROM MarvelCharacters
WHERE HAIR = 'Variable Hair';

-- Задача 4: Женские персонажи с редким цветом глаз
SELECT name, EYE
FROM MarvelCharacters
WHERE SEX = "Female Characters" AND EYE IN ('Gold Eyes', 'Amber Eyes');

-- Задача 5: Персонажи без двойной идентичности, сортированные по году появления
SELECT name, Year
FROM MarvelCharacters
WHERE identify = 'No Dual Identity'
ORDER BY Year DESC;

-- Задача 6: Герои и злодеи с необычными прическами
SELECT name, ALIGN, HAIR
FROM MarvelCharacters
WHERE HAIR NOT IN ('Brown Hair', 'Black Hair', 'Blond Hair', 'Red Hair');

-- Задача 7: Персонажи, появившиеся в определённое десятилетие
SELECT name, Year
FROM MarvelCharacters
WHERE Year BETWEEN 1960 AND 1969;

-- Задача 8: Персонажи с уникальным сочетанием цвета глаз и волос
SELECT name, EYE, HAIR
FROM MarvelCharacters
WHERE EYE = 'Yellow Eyes' AND HAIR = 'Red Hair';

-- Задача 9: Персонажи с ограниченным количеством появлений
SELECT name, APPEARANCES
FROM MarvelCharacters
WHERE APPEARANCES < 10;

-- Задача 10: Персонажи с наибольшим количеством появлений
SELECT name, APPEARANCES
FROM MarvelCharacters
ORDER BY APPEARANCES DESC
LIMIT 5;

-- Задача 11: Персонажи, появившиеся только в одном десятилетии
SELECT name, Year
FROM MarvelCharacters
WHERE Year BETWEEN 2000 AND 2009;

-- Задача 12: Персонажи с самыми редкими цветами глаз
SELECT name, EYE
FROM MarvelCharacters
WHERE EYE IN ('Magenta Eyes', 'Pink Eyes', 'Violet Eyes');

-- Задача 13: Герои с публичной идентичностью, сортированные по году
SELECT name, identify, Year
FROM MarvelCharacters
WHERE identify = 'Public Identity'
ORDER BY Year;

-- Здесь LIKE необходим для задачи 4, чтобы учесть возможные вариации представления женского пола в данных, например, "Female Characters".

-- Задача 14: Персонажи с конкретным цветом волос и глаз, упорядоченные по имени
SELECT name, HAIR, EYE
FROM MarvelCharacters
WHERE HAIR = 'Black Hair' AND EYE = 'Green Eyes'
ORDER BY name;

-- Задача 15: Злодеи с нестандартными физическими характеристиками
SELECT name, SEX
FROM MarvelCharacters
WHERE ALIGN = 'Bad Characters' AND SEX NOT IN ('Male Characters', 'Female Characters');

-- Задача 16: Персонажи с наибольшим числом появлений по полу
-- Определение мужского и женского персонажа с наибольшим количеством появлений
SELECT name, SEX, MAX(APPEARANCES) AS max_appearances
FROM MarvelCharacters
GROUP BY SEX;


-- Задача 17: Сравнение популярности персонажей по цвету волос и глаз
-- Сравнение количества появлений по комбинации цвета волос и глаз
-- SELECT HAIR, EYE, COUNT(*) AS appearances_count -- это количество строк
-- Сделаем сумму появлений
SELECT HAIR, EYE, SUM(APPEARANCES) AS appearances_count
FROM MarvelCharacters
GROUP BY HAIR, EYE
ORDER BY appearances_count DESC;


-- Задача 18: Персонажи с максимальным количеством появлений в десятилетие
-- Найти персонажа с максимальным количеством появлений в каждом десятилетии
SELECT name, (Year / 10) * 10 AS decade, MAX(APPEARANCES) AS max_appearances
FROM MarvelCharacters
GROUP BY decade;

-- Решение от Ивана
SELECT name, appearances, year/10 * 10  as dec_start,
    year/10 * 10 + 10 as dec_end
FROM MarvelCharacters
GROUP BY year/10



-- Задача 19: Герои и злодеи 80-х
-- Сравнение количества новых героев и злодеев 1980-х
SELECT ALIGN, COUNT(*) AS count
FROM MarvelCharacters
WHERE Year BETWEEN 1980 AND 1989
GROUP BY ALIGN
HAVING ALIGN IN ('Good Characters', 'Bad Characters');

-- Решение от Павла
SELECT ALIGN, COUNT(*), YEAR
FROM MarvelCharacters
WHERE ALIGN in ('Bad Characters', 'Good Characters')
AND YEAR between 1980 AND 1989
GROUP BY ALIGN, YEAR
ORDER BY YEAR


-- Задача 20: Самые популярные прически супергероев
-- Определение топ-3 причесок по общему количеству появлений
SELECT HAIR, SUM(APPEARANCES) AS total_appearances
FROM MarvelCharacters
GROUP BY HAIR
ORDER BY total_appearances DESC
LIMIT 3;