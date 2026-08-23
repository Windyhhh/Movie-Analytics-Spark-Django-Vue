from django.urls import path
from . import views

urlpatterns = [
    path('api/genre/', views.get_genre_analysis, name='genre_analysis'),
    path('api/year/', views.get_year_analysis, name='year_analysis'),
    path('api/rating/', views.get_rating_analysis, name='rating_analysis'),
    path('api/movies/', views.get_all_movies, name='all_movies'),
    path('api/run-analysis/', views.run_analysis, name='run_analysis'),
]