from django.db.models import Count, Avg
from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalPermission
from movies.models import Movie
from movies.serializers import MovieSerializer, MovieListDetailSerializer
from reviews.models import Review


class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermission)
    queryset = Movie.objects.all()
    #serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        return MovieSerializer

class MovieRetriverUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermission)
    queryset = Movie.objects.all()
    

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        return MovieSerializer


class MoviesStatisticView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalPermission)
    queryset = Movie.objects.all()

    def get(self, request):
        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))
        total_reviews = Review.objects.count()
        avg_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']

        return response.Response(data={
            'total_movies': total_movies,
            'movies_by_genre': movies_by_genre,
            'total_reviews': total_reviews,
            'avg_stars': avg_stars if avg_stars else 0,  # If no reviews, return 0 as average star rating.  # noqa: E501
        }, status=status.HTTP_200_OK,)
