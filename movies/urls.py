from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.MovieCreateListView.as_view(), name='movies-create-list'),
    path('movies/<int:pk>/', views.MovieRetriverUpdateDestroyView.as_view(), name='movies-detail-view'),
]