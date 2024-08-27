
from django.contrib import admin
from django.urls import path
from genres.views import GenreCreateView, GenreRetrieverUpdateView
from actors.views import ActorCreateListView, ActorRetriverUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('genres/',GenreCreateView.as_view() , name='genre-create'),
    path('genres/<int:pk>/',GenreRetrieverUpdateView.as_view(), name='genre-detail'),

    path('actors/', ActorCreateListView.as_view(), name='actor-create-list'),
    path('actors/<int:pk>/', ActorRetriverUpdateDestroyView.as_view(), name='actor-detail'),

]
    