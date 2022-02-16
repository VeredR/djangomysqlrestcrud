from rest_framework import serializers
from restcrud.models import Movies, Users, Rentals


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ['name', 'release_date', 'score', 'overview', 'image']


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'username', 'email', 'password']


class RentalsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rentals
        fields = ['id', 'user', 'movie', 'ttl']
        extra_kwargs = {'id': {'required': False}}

