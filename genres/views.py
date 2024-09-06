from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalPermission
from genres.models import Genres
from genres.serializers import GenreSerializer
 

class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermission)
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer



class GenreRetrieverUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermission)
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer
