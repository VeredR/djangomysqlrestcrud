from rest_framework import serializers
from restcrud.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'release_date', 'user_score', 'overview', 'image']

        extra_kwargs = {'id': {'required': False}}
