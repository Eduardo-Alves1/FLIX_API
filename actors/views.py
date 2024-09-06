from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalPermission
from actors.models import Actor
from actors.serializers import ActorSerializer


class ActorCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermission)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorRetriverUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermission)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
