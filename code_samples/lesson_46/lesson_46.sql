-- Старая структура БД
-- Тут нет тегов и категорий
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Таблица: Cards
CREATE TABLE IF NOT EXISTS Cards (
    CardID INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    user_id INTEGER DEFAULT(1),
    upload_date DATETIME DEFAULT(datetime('now')),
    views INTEGER DEFAULT(0),
    adds INTEGER DEFAULT(0),
    FOREIGN KEY (user_id) REFERENCES Users(UserID)
);

-- Таблица: Users
CREATE TABLE IF NOT EXISTS Users (
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT NOT NULL
);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;

-- Посчитать максимальную длину вопроса и ответа
SELECT MAX(LENGTH(question)), MAX(LENGTH(answer)) FROM Cards;

-- Посчитать среднюю длину вопроса и ответа
SELECT AVG(LENGTH(question)), AVG(LENGTH(answer)) FROM Cards;

-- Вывести карточку с максимальной длиной ответа
SELECT * FROM Cards WHERE LENGTH(answer) = (SELECT MAX(LENGTH(answer)) FROM Cards);

--------------------------------------------------------
-- Но для успешной работы нам нужно усложнить БД

PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Таблица: Users
CREATE TABLE IF NOT EXISTS Users (
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT NOT NULL
);

-- Таблица: Categories
CREATE TABLE IF NOT EXISTS Categories (
    CategoryID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL UNIQUE
);

-- Таблица: Tags
CREATE TABLE IF NOT EXISTS Tags (
    TagID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL UNIQUE
);

-- Таблица: Cards
CREATE TABLE IF NOT EXISTS Cards (
    CardID INTEGER PRIMARY KEY AUTOINCREMENT,
    Question TEXT NOT NULL UNIQUE,
    Answer TEXT NOT NULL UNIQUE,
    UserID INTEGER DEFAULT(1),
    CategoryID INTEGER,
    UploadDate DATETIME DEFAULT(datetime('now')),
    Views INTEGER DEFAULT(0),
    Favorites INTEGER DEFAULT(0),
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE SET DEFAULT ON UPDATE CASCADE,
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE SET NULL ON UPDATE CASCADE
);

-- Таблица: CardTags
CREATE TABLE IF NOT EXISTS CardTags (
    CardID INTEGER,
    TagID INTEGER,
    PRIMARY KEY (CardID, TagID),
    FOREIGN KEY (CardID) REFERENCES Cards(CardID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (TagID) REFERENCES Tags(TagID) ON DELETE CASCADE ON UPDATE CASCADE
);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
