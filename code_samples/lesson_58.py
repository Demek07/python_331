"""
Lesson 56 -
Разбор ДЗ
Metaclasses
Inner Classes
21.12.2023

"""


class BlogPost:
    # Вложенный класс Meta для хранения метаданных
    class Meta:
        # Предположим, у нас есть некоторые параметры конфигурации
        ordering = ['-date_published']
        db_table = 'blog_post'

    def __init__(self, title, content, date_published):
        self.title = title
        self.content = content
        self.date_published = date_published

    def save(self):
        # Здесь мог бы быть код для сохранения экземпляра в базу данных
        print(f"Saving '{self.title}' to table {self.Meta.db_table}")

    @classmethod
    def get_all_posts(cls):
        # Здесь мог бы быть код для получения всех постов из базы данных
        print(f"Getting all posts ordered by {cls.Meta.ordering[0]}")


# Создание и использование экземпляра BlogPost
post = BlogPost("My First Post", "Hello, world!", "2021-01-01")
post.save()  # Сохраняет пост, используя информацию из класса Meta
BlogPost.get_all_posts()  # Получает все посты, используя порядок из класса Meta
