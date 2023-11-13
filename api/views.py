from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RecommendationSerializer
from django.shortcuts import render
from .utils import SupportingFunc
import pandas as pd

# Load the movies DataFrame once and reuse it
try:
    df_movies = pd.read_csv('csv/movies_with_embedding.csv')
except Exception as e:
    df_movies = pd.DataFrame()
    print(f"Error loading movies dataset: {e}")

# Instantiate SupportingFunc
support_func = SupportingFunc()

# View to serve the HTML page
def recommendations_page(request):
    return render(request, 'index.html')

class MovieRecommendationView(APIView):
    def get(self, request, format=None):
        prompt = request.query_params.get('prompt', None)
        if prompt is None:
            return Response({'error': 'No prompt provided'}, status=status.HTTP_400_BAD_REQUEST)

        if df_movies.empty:
            return Response({'error': 'Movies dataset not loaded'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Find top 5 similar movies
        top_movies = support_func.find_top_movies(prompt, df_movies)
        print("top_movies", top_movies)
        # Serialize the recommendations
        serializer = RecommendationSerializer(data={'recommendations': top_movies['title'].tolist()})

        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
