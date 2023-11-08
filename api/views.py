from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RecommendationSerializer
from django.shortcuts import render

# Import the recommend_movies_based_on_prompt function from the utils.py file
from .utils import recommend_movies_based_on_prompt, tfidf_vectorizer_overview, tfidf_matrix_overview, data

# This view will serve the HTML page
def recommendations_page(request):
    return render(request, 'index.html')


class MovieRecommendationView(APIView):
    def get(self, request, format=None):
        # Get the prompt from the request query parameters
        prompt = request.query_params.get('prompt', None)
        if prompt is None:
            return Response({'error': 'No prompt provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Use the recommendation function from the script to get recommendations
        recommendations = recommend_movies_based_on_prompt(prompt, data, tfidf_vectorizer_overview, tfidf_matrix_overview)
        
        # Serialize the recommendations
        serializer = RecommendationSerializer(data={'recommendations': recommendations})
        
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)