-- Lesson 44 20.02.2024
-- Разбор hw_26 (Нормализация Marvel)
-- Виды отношений между таблицами
-- Повторение
    -- Один к одному
    -- Один ко многим
-- Многие ко многим
-- Начали Триггеры


-- Многие ко многим - Many to Many
CREATE TABLE Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    last_name TEXT NOT NULL
    -- Другие поля, связанные со студентом
);

CREATE TABLE Teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    last_name TEXT NOT NULL
    -- Другие поля, связанные с учителем
);

-- Таблица связи
-- В ней могло бы быть гораздо больше данных, например
-- дата начала и окончания обучения, оценки, дополнительные занятия, аудитории, отзывы и т.д.

CREATE TABLE StudentsTeachers (
    student_id INTEGER,
    teachers_id INTEGER,
    PRIMARY KEY (student_id, teachers_id),
    FOREIGN KEY (student_id) REFERENCES Students (id)
        ON DELETE CASCADE
        ON UPDATE NO ACTION,
    FOREIGN KEY (teachers_id) REFERENCES Teachers (id)
        ON DELETE CASCADE
        ON UPDATE NO ACTION
);

-- Добавим студентов
INSERT INTO Students (name, last_name)
VALUES ('Иван', 'Николаев'),
       ('Петр', 'Сидоров'),
       ('Сидор', 'Петров'),
       ('Анна', 'Иванова'),
       ('Светлана', 'Никифорова'),
       ('Дарья', 'Леонтьева');

-- Добавим учителей
INSERT INTO Teachers (name, last_name)
VALUES ('Сигимунд', 'Фрейд'),
       ('Карл', 'Ясперс'),
       ('Мартин', 'Хайдеггер'),
       ('Фридрих', 'Ницше'),
       ('Альберт', 'Камю'),
       ('Жан-Поль', 'Сартр');

-- Добавим связи.
-- Что в нашем случае они будут представлять?
-- Вероятно проведенное занятие!

INSERT INTO StudentsTeachers (student_id, teachers_id)
VALUES (1, 1),
       (2, 2),
       (3, 3),
       (4, 4),
       (5, 5),
       (6, 6);

-- Добавим одну запись, найдя данные по имени и фамилии студента, и имени и фамилии препода
INSERT INTO StudentsTeachers (student_id, teachers_id)
VALUES ((SELECT id FROM Students WHERE name = 'Светлана' AND last_name = 'Никифорова'),
        (SELECT id FROM Teachers WHERE name = 'Фридрих' AND last_name = 'Ницше'));


-- Давайте выполним запрос и получим имена  и фамилии студентов и их учителей
SELECT Students.name AS Имя_студента, Students.last_name AS Фамилия_студента,
       Teachers.name AS Имя_препода, Teachers.last_name AS Фамилия_препода
FROM Students
JOIN StudentsTeachers ON Students.id = StudentsTeachers.student_id
JOIN Teachers ON Teachers.id = StudentsTeachers.teachers_id;

-- Добавим еще одного препода
INSERT INTO Teachers (name, last_name)
VALUES ('Карл', 'Густав Юнг');

-- Сидор Петров учился у Карла Густава Юнга
INSERT INTO StudentsTeachers (student_id, teachers_id)
VALUES ((SELECT id FROM Students WHERE name = 'Сидор' AND last_name = 'Петров'),
        (SELECT id FROM Teachers WHERE name = 'Карл' AND last_name = 'Густав Юнг'));

-- Студенты, у которых не преподавал юнг (имена и фамилии)
-- Выбираем из таблицы Students имя, фамилию студента
SELECT Students.name AS Имя_студента, Students.last_name AS Фамилия_студента
FROM Students
-- Где ID студента не входит в следующее выражение
WHERE Students.id NOT IN  -- Если убрать NOT, то получим студентов, у которых преподавал Юнг
    -- Выбираем из таблицы StudentsTeachers ID студента, где ID препода равен следующему выражению
    (SELECT student_id
    FROM StudentsTeachers
    -- Выбираем из таблицы Teachers ID препода, где имя и фамилия препода равны следующему выражению
    WHERE teachers_id = (
        SELECT id
        FROM Teachers
        WHERE name = 'Карл' AND last_name = 'Густав Юнг'));


------------------------------ Таблица для следующего урока ----------------
-- Карточки с вопросами и ответами для приложения интервального повторения (Anki)
-- CardID - уникальный идентификатор карточки
-- Question - вопрос NOT NULL
-- Answer - ответ NOT NULL
-- AuthorID - ID автора карточки DEFAULT(1) - ID автора по умолчанию 1 FOREIGN KEY
-- UploadDate - DATETIME DEFAULT(datetime('now', 'localtime')) - дата и время добавления карточки
-- Views - количество просмотров
-- Adds - количество добавлений в избранное

-- Делаем таблицу с авторами
CREATE TABLE Authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    last_name TEXT NOT NULL
);

-- Добавим автора с id 1
INSERT INTO Authors (name, last_name)
VALUES ('Владимир', 'Монин');

-- Создаем таблицу с карточками
CREATE TABLE Cards (
    CardID INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    author_id INTEGER DEFAULT(1),
    upload_date DATETIME DEFAULT(datetime('now')),
    views INTEGER DEFAULT(0),
    adds INTEGER DEFAULT(0),
    FOREIGN KEY (author_id) REFERENCES Authors(id)
);


-- Добавим 1 карточку
INSERT INTO Cards (question, answer)
VALUES ('Пайтон или Питон?', 'Python!');

-- Исправленное определение таблицы CardLogs
CREATE TABLE CardLogs (
    LogID INTEGER PRIMARY KEY AUTOINCREMENT,
    CardID INTEGER,
    ActionType TEXT,
    ActionDetails TEXT,
    AuthorID INTEGER,
    ActionDate DATETIME DEFAULT (datetime('now')),
    FOREIGN KEY (CardID) REFERENCES Cards(CardID), -- Исправлено на правильное имя столбца
    FOREIGN KEY (AuthorID) REFERENCES Authors(id) -- Ссылка на таблицу Authors
);


-- Триггер для логирования вставки новой карточки
CREATE TRIGGER LogInsertCard
AFTER INSERT ON Cards
FOR EACH ROW
BEGIN
    INSERT INTO CardLogs (CardID, ActionType, ActionDetails, AuthorID, ActionDate)
    VALUES (NEW.CardID, 'CREATE', 'Created a new card', NEW.author_id, datetime('now'));
END;

-- Триггер для логирования обновления карточки
CREATE TRIGGER LogUpdateCard
AFTER UPDATE ON Cards
FOR EACH ROW
BEGIN
    INSERT INTO CardLogs (CardID, ActionType, ActionDetails, AuthorID, ActionDate)
    VALUES (NEW.CardID, 'UPDATE', 'Updated a card. Question was: ' || OLD.question || '. Answer was: ' || OLD.answer, NEW.author_id, datetime('now'));
END;

-- Триггер для логирования удаления карточки
CREATE TRIGGER LogDeleteCard
AFTER DELETE ON Cards
FOR EACH ROW
BEGIN
    INSERT INTO CardLogs (CardID, ActionType, ActionDetails, AuthorID, ActionDate)
    VALUES (OLD.CardID, 'DELETE', 'Deleted a card. Question was: ' || OLD.question || '. Answer was: ' || OLD.answer, OLD.author_id, datetime('now'));
END;


-- Обновим запись с id 1
UPDATE Cards
SET answer = 'Точно не Питон!'
WHERE id = 1;