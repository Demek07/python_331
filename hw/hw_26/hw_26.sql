-- Шаг 1. Создать таблицу MarvelCharacters
--CREATE TABLE MarvelCharacters (
--    page_id          INTEGER,
--    name             TEXT,
--    urlslug          TEXT,
--    identify         TEXT,
--    ALIGN            TEXT,
--    EYE              TEXT,
--    HAIR             TEXT,
--    SEX              TEXT,
--    GSM              TEXT,
--    ALIVE            TEXT,
--    APPEARANCES      INTEGER,
--    FIRST_APPEARANCE TEXT,
--    Year             INTEGER
--);


-- Шаг 2: Создаем новую таблицу с дополнительным столбцом id
CREATE TABLE MarvelCharacters_new (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    page_id INTEGER,
    name TEXT,
    urlslug TEXT,
    identify TEXT,
    ALIGN TEXT,
    EYE TEXT,
    HAIR TEXT,
    SEX TEXT,
    GSM TEXT,
    ALIVE TEXT,
    APPEARANCES INTEGER,
    FIRST_APPEARANCE TEXT,
    Year INTEGER
);

-- Шаг 3: Копируем данные из старой таблицы в новую
INSERT INTO MarvelCharacters_new (page_id, name, urlslug, identify, ALIGN, EYE, HAIR, SEX, GSM, ALIVE, APPEARANCES, FIRST_APPEARANCE, Year)
SELECT page_id, name, urlslug, identify, ALIGN, EYE, HAIR, SEX, GSM, ALIVE, APPEARANCES, FIRST_APPEARANCE, Year FROM MarvelCharacters;

-- Шаг 3: Удаляем старую таблицу
DROP TABLE MarvelCharacters;

-- Шаг 4: Переименовываем новую таблицу
ALTER TABLE MarvelCharacters_new RENAME TO MarvelCharacters;



-- Шаг 5: Создаем таблицы для уникальных значений SEX (пол), EYE (цвет глаз), HAIR (цвет волос), ALIGN (выравнивание), ALIVE (живой/мертвый), IDENTIFY (идентификация)

CREATE TABLE Sex (
    sex_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
);

CREATE TABLE EyeColor (
    eye_id INTEGER PRIMARY KEY AUTOINCREMENT,
    color TEXT UNIQUE
);

CREATE TABLE HairColor (
    hair_id INTEGER PRIMARY KEY AUTOINCREMENT,
    color TEXT UNIQUE
);

CREATE TABLE Alignment (
    align_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
);

CREATE TABLE LivingStatus (
    status_id INTEGER PRIMARY KEY AUTOINCREMENT,
    status TEXT UNIQUE
);

CREATE TABLE Identity (
    identity_id INTEGER PRIMARY KEY AUTOINCREMENT,
    identity TEXT UNIQUE
);

-- Шаг 6: Наполняем эти таблицы уникальными значениями из таблицы MarvelCharacters

INSERT INTO Sex (name)
SELECT DISTINCT SEX FROM MarvelCharacters;

INSERT INTO EyeColor (color)
SELECT DISTINCT EYE FROM MarvelCharacters;

INSERT INTO HairColor (color)
SELECT DISTINCT HAIR FROM MarvelCharacters;

INSERT INTO Alignment (name)
SELECT DISTINCT ALIGN FROM MarvelCharacters;

INSERT INTO LivingStatus (status)
SELECT DISTINCT ALIVE FROM MarvelCharacters;

INSERT INTO Identity (identity)
SELECT DISTINCT identify FROM MarvelCharacters;

-- Шаг 7: Создаем таблицу с персонажами и вместо полных названий столбцов - внешние ключи

CREATE TABLE MarvelCharacters_New (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    page_id INTEGER,
    name TEXT,
    urlslug TEXT,
    identity_id INTEGER,
    align_id INTEGER,
    eye_id INTEGER,
    hair_id INTEGER,
    sex_id INTEGER,
    status_id INTEGER,
    APPEARANCES INTEGER,
    FIRST_APPEARANCE TEXT,
    Year INTEGER,
    FOREIGN KEY (identity_id) REFERENCES Identity(identity_id),
    FOREIGN KEY (align_id) REFERENCES Alignment(align_id),
    FOREIGN KEY (eye_id) REFERENCES EyeColor(eye_id),
    FOREIGN KEY (hair_id) REFERENCES HairColor(hair_id),
    FOREIGN KEY (sex_id) REFERENCES Sex(sex_id),
    FOREIGN KEY (status_id) REFERENCES LivingStatus(status_id)
);

-- Открываем транзакцию
BEGIN TRANSACTION;


-- Шаг 8: Наполняем новую таблицу с персонажами данными

--INSERT INTO MarvelCharacters_New (page_id, name, urlslug, identity_id, align_id, eye_id, hair_id, sex_id, status_id, APPEARANCES, FIRST_APPEARANCE, Year)
--SELECT mc.page_id, mc.name, mc.urlslug,
--       id.identity_id, al.align_id, ec.eye_id, hc.hair_id, s.sex_id, ls.status_id,
--       mc.APPEARANCES, mc.FIRST_APPEARANCE, mc.Year
--FROM MarvelCharacters mc -- назначение псевдонима для таблицы MarvelCharacters
--LEFT JOIN Identity id ON mc.identify = id.identity
--LEFT JOIN Alignment al ON mc.ALIGN = al.name
--LEFT JOIN EyeColor ec ON mc.EYE = ec.color
--LEFT JOIN HairColor hc ON mc.HAIR = hc.color
--LEFT JOIN Sex s ON mc.SEX = s.name
--LEFT JOIN LivingStatus ls ON mc.ALIVE = ls.status;

-- Отчасти решает проблему сохранения данных, но не полностью
-- Null значения подставляются в виде Null, а не в виде соответствующего ID из своих таблиц
-- Можно пробежаться по этим столбцам и заменить Null на соответствующие ID из своих таблиц через подзапросы

-- Или выбрать иной подход для решения этой проблемы
INSERT INTO
MarvelCharacters_New
    (page_id, name, urlslug, identity_id, Align_id, Eye_id,
    Hair_id, Sex_id, status_id, APPEARANCES, FIRST_APPEARANCE, Year)
SELECT
    m.page_id, m.name, m.urlslug, i.identity_id, a.Align_id, e.Eye_id,
    h.Hair_id, s.Sex_id, l.status_id, m.APPEARANCES, m.FIRST_APPEARANCE, m.Year
FROM     MarvelCharacters m
LEFT JOIN
    Alignment a ON m.ALIGN = a.name or (m.ALIGN IS NULL and a.name IS NULL),
    EyeColor e ON m.EYE = e.color or (m.EYE IS NULL and e.color IS NULL),
    HairColor h ON m.HAIR = h.color or (m.HAIR IS NULL and h.color IS NULL),
    Identity i ON m.identify = i.identity or (m.identify IS NULL and i.identity IS NULL),
    LivingStatus l ON m.ALIVE = l.status or (m.ALIVE IS NULL and l.status IS NULL),
    Sex s ON m.SEX = s.name or (m.SEX IS NULL and s.name IS NULL);


-- Шаг 9: Удаляем старую таблицу MarvelCharacters

DROP TABLE MarvelCharacters;

-- Шаг 10: Переименовываем новую таблицу MarvelCharacters_New в MarvelCharacters
ALTER TABLE MarvelCharacters_New RENAME TO MarvelCharacters;