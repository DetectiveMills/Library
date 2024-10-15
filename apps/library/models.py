from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=155, verbose_name='Имя автора')
    birthdate = models.DateField(verbose_name='День рождение')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Авторы"
        verbose_name_plural = "Автора"

class Book(models.Model):
    title = models.CharField(max_length=155, verbose_name='Название книги')
    publication_year = models.IntegerField(verbose_name='Год издания')
    author = models.ForeignKey(Author, null=True, blank=True, on_delete=models.SET_NULL, related_name='author_book')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Книги"
        verbose_name_plural = "Книгу"

class Genre(models.Model):
    name = models.CharField(max_length=155, verbose_name='Название жанра')
    books = models.ManyToManyField(Book, related_name='genre_book')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Жанры"
        verbose_name_plural = "Жанр" 

