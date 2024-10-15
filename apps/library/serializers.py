from rest_framework import serializers

from .models import Author, Book, Genre

class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'