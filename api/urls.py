
from django.urls import path
from .views import MovieRecommendationView, recommendations_page

urlpatterns = [
    path('recommend/', MovieRecommendationView.as_view(), name='movie-recommendation'),
    path('', recommendations_page, name='recommendations-page'),
]
