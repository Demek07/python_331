-- Запрос на создание таблицы cards
--**Cards (Карточки)**
--   - `CardID`: INTEGER, PRIMARY KEY, AUTOINCREMENT
--   - `Question`: TEXT, NOT NULL
--   - `Answer`: TEXT, NOT NULL
--   - `AuthorID`: INTEGER, FOREIGN KEY (AuthorID) REFERENCES Users(UserID) default 1 по обновлению cascade, по удалению default
--   - `UploadDate`: DATETIME DEFAULT(datetime('now')
--   - `Views`: INTEGER DEFAULT 0
--   - `Adds`: INTEGER DEFAULT 0

-- Таблица с юзерами для приложения интервального повторения (Anki)
-- UserID - уникальный идентификатор пользователя
-- Name - имя пользователя NOT NULL

--1. **Users (Пользователи)**
--   - `UserID`: INTEGER, PRIMARY KEY, AUTOINCREMENT
--   - `FirstName`: TEXT


-- Создаем таблицу с юзерами если она не существует
CREATE TABLE IF NOT EXISTS Users (
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT NOT NULL
);

-- Добавим пользователя с id 1
--INSERT INTO Users (FirstName)
--VALUES ('Владимир');

-- Создаем таблицу с карточками
CREATE TABLE IF NOT EXISTS Cards (
    CardID INTEGER PRIMARY KEY AUTOINCREMENT,
    Question TEXT NOT NULL,
    Answer TEXT NOT NULL,
    AuthorID INTEGER DEFAULT 1,
    FOREIGN KEY (AuthorID) REFERENCES Users(UserID) ON UPDATE CASCADE ON DELETE SET DEFAULT,
    UploadDate DATETIME DEFAULT(datetime('now')),
    Views INTEGER DEFAULT 0,
    Adds INTEGER DEFAULT 0
);