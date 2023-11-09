from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "polls"
urlpatterns = [
    path("", views.MovieListView.as_view(), name="movie_list"),  # List of movies
    path("movie/<int:pk>/", views.MovieDetailView.as_view(), name="movie_detail"),  # Detail of a movie
    path("movie/<int:movie_id>/submit_review/", views.submit_review, name="submit_review"),  # Submit a review
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
