from django.contrib import admin
from .models import Author, Book, Genre

# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'birthdate']
    list_filter = ['id', 'name', 'birthdate']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'publication_year', 'author']
    list_filter = ['id', 'title', 'publication_year', 'author']

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
