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
