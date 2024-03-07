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
    Question TEXT NOT NULL,  
    Answer TEXT NOT NULL,  
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


-- Получить полные данные по карточке по ID, включая категории и теги
-- Получается не очень
SELECT Cards.CardID, Cards.Question, Cards.Answer, Categories.Name, Tags.Name
FROM Cards
LEFT JOIN Categories ON Cards.CategoryID = Categories.CategoryID
LEFT JOIN CardTags ON Cards.CardID = CardTags.CardID
LEFT JOIN Tags ON CardTags.TagID = Tags.TagID
WHERE Cards.CardID = 1;

-- Улучшим это
SELECT 
    Cards.CardID, 
    Cards.Question, 
    Cards.Answer, 
    Categories.Name AS CategoryName,
    GROUP_CONCAT(Tags.Name, ', ') AS Tags
FROM 
    Cards
LEFT JOIN 
    Categories ON Cards.CategoryID = Categories.CategoryID
LEFT JOIN 
    CardTags ON Cards.CardID = CardTags.CardID
LEFT JOIN 
    Tags ON CardTags.TagID = Tags.TagID
WHERE 
    Cards.CardID = 1

