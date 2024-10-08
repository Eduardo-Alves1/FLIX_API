from django.db.models import Avg
from rest_framework import serializers
from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializer
from movies.models import Movie


class MovieListDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    genre = GenreSerializer()
    rate = serializers.SerializerMethodField(read_only=True)
    class Meta: 
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']
    
    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)
        
        return None


class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'


    def validate_release_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError("A data não pode ser anteriro a 1990.")
        return value
    
    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError("O resumo não pode exceder 200 caracteres.")
        return value
    
    def validate_title(self, value):
        if Movie.objects.filter(title=value).exists():
            raise serializers.ValidationError("Já existe um filme com esse título.")
        return value