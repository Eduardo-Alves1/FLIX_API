from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from genres.models import Genres
from genres.serializers import GenreSerializer
from genres.permissions import GenrePermissionView
 



class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GenrePermissionView)
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer



class GenreRetrieverUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GenrePermissionView)
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer