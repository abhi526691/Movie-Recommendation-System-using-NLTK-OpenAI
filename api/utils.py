import pandas as pd
import ast  # For converting string representations of lists into actual lists
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Ensure that NLTK has the necessary data for processing
nltk.download('punkt')
nltk.download('stopwords')

# Load the CSV file
file_path = 'csv/final_dataset.csv'  # Update this path to where the CSV file is located
data = pd.read_csv(file_path)

# Function to convert string representations of lists into actual lists
def parse_list_string(list_string):
    try:
        return ast.literal_eval(list_string)
    except ValueError:
        return []  # Return an empty list if there is a parsing error

# Apply the parsing function to the list-like columns
list_columns = ['genres', 'keywords', 'production_companies', 'cast']
for column in list_columns:
    data[column] = data[column].apply(parse_list_string)

# Define the preprocessing function for text fields
def preprocess_text(text):
    # Tokenize the text
    tokens = word_tokenize(text.lower())
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    # Return the preprocessed text
    return " ".join([token for token in tokens if token not in stop_words])

# Preprocess the overviews and taglines
data['processed_overview'] = data['overview'].apply(preprocess_text)
data['processed_tagline'] = data['tagline'].apply(preprocess_text)

# Initialize TF-IDF Vectorizer for overviews
tfidf_vectorizer_overview = TfidfVectorizer()
# Fit and transform the processed overviews to create the feature matrix
tfidf_matrix_overview = tfidf_vectorizer_overview.fit_transform(data['processed_overview'])

# If you want to use taglines for recommendations, initialize another TF-IDF Vectorizer for taglines
# tfidf_vectorizer_tagline = TfidfVectorizer()
# tfidf_matrix_tagline = tfidf_vectorizer_tagline.fit_transform(data['processed_tagline'])


# Define the recommendation function
def recommend_movies_based_on_prompt(prompt, data, tfidf_vectorizer, tfidf_matrix, top_n=5):
    # Preprocess the prompt
    preprocessed_prompt = preprocess_text(prompt)
    # Transform the prompt into the same feature space as the overviews
    prompt_tfidf_vector = tfidf_vectorizer.transform([preprocessed_prompt])
    # Compute cosine similarity between the prompt and all movie overviews
    cosine_similarities = cosine_similarity(prompt_tfidf_vector, tfidf_matrix)
    # Get the top n similar movies
    similar_movies_idx = cosine_similarities[0].argsort()[:-top_n-1:-1]
    # Get the titles of the recommended movies
    recommended_movies = data.iloc[similar_movies_idx]['title'].values
    return recommended_movies
