from rest_framework import generics
from genres.models import Genres
from genres.serializers import GenreSerializer
 



class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer



class GenreRetrieverUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer