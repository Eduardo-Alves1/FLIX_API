
from django.contrib import admin
from django.urls import path
from genres.views import GenreCreateListView, GenreRetrieverUpdateDestroyView
from actors.views import ActorCreateListView, ActorRetriverUpdateDestroyView
from movies.views import MovieCreateListView, MovieRetriverUpdateDestroyView
from reviews.views import ReviewCreateListView, ReviewRetriveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('genres/',GenreCreateListView.as_view() , name='genre-create-list'),
    path('genres/<int:pk>/',GenreRetrieverUpdateDestroyView.as_view(), name='genre-detail-view'),

    path('actors/', ActorCreateListView.as_view(), name='actor-create-list'),
    path('actors/<int:pk>/', ActorRetriverUpdateDestroyView.as_view(), name='actor-detail-view'),

    path('movies/', MovieCreateListView.as_view(), name='movie-create-list-view'),
    path('movies/<int:pk>/', MovieRetriverUpdateDestroyView.as_view(), name='movie-detail-view'),

    path('reviews/', ReviewCreateListView.as_view(), name='review-create-list-view'),
    path('reviews/<int:pk>/', ReviewRetriveUpdateDestroyView.as_view(), name='review-detail-view'),

]
    