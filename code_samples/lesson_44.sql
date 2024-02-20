-- Lesson 44 20.02.2024
-- Разбор hw_26 (Нормализация Marvel)
-- Виды отношений между таблицами
-- Повторение
    -- Один к одному
    -- Один ко многим
-- Многие ко многим


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
       ('Сидор', 'Петров');
       ('Анна', 'Иванова');
       ('Светлана', 'Никифорова');
       ('Дарья', 'Леонтьева');

-- Добавим учителей
INSERT INTO Teachers (name, last_name)
VALUES ('Сигимунд', 'Фрейд'),
       ('Карл', 'Ясперс'),
       ('Мартин', 'Хайдеггер');
       ('Фридрих', 'Ницше');
       ('Альберт', 'Камю');
       ('Жан-Поль', 'Сартр');

-- Добавим связи.
-- Что в нашем случае они будут представлять?
-- Вероятно проведенное занятие!

--INSERT INTO StudentsTeachers (student_id, teachers_id)
--VALUES (1, 1),
--       (2, 2),
--       (3, 3),
--       (4, 4),
--       (5, 5),
--       (6, 6);

-- Добавим одну запись, найдя данные по имени и фамилии студента, и имени и фамилии препода
INSERT INTO StudentsTeachers (student_id, teachers_id)
VALUES ((SELECT id FROM Students WHERE name = 'Иван' AND last_name = 'Николаев'),
        (SELECT id FROM Teachers WHERE name = 'Сигимунд' AND last_name = 'Фрейд'));