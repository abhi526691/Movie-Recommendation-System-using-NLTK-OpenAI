import openai
import numpy as np
# from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from openai.embeddings_utils import cosine_similarity, get_embedding


class SupportingFunc:
    def __init__(self):
        openai.api_key = ''

    def find_top_movies(self, query, df_movies, top_n=5):
        product_embedding = get_embedding(
            query,
            engine="text-embedding-ada-002"
        )

        df_movies["embedding"] = df_movies.embedding.apply(eval).apply(np.array)
        df_movies["similarity"] = df_movies.embedding.apply(
            lambda x: cosine_similarity(x, product_embedding))
        
        sorted_movies = df_movies.sort_values(by='similarity', ascending=False)
        return sorted_movies.head(top_n)



