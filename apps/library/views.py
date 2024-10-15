from django.shortcuts import render

from .serializers import AuthorSerializers, BookSerializers, GenreSerializers
from .models import Author, Book, Genre
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

# Create your views here.

class AuthorAPI(GenericViewSet,
              mixins.ListModelMixin):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers

class BookAPI(GenericViewSet,
              mixins.ListModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

class GenreAPI(GenericViewSet,
              mixins.ListModelMixin):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializers