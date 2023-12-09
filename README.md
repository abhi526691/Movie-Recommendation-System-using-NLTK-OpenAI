# MyDjangoWebApp

Movie Recommendation Systsem is a web application built with Django that allows users to perform [Movie Search based on their requirement].

![Sample Output](

https://github.com/abhi526691/Movie-Recommendation-System-using-NLTK-OpenAI/assets/53704940/266a1678-76db-4ec9-932e-e5b6a4c3e8c5

)

## Other iterations of this model
- We tried TF-IDF vectorizer to get the vector of concatenated string to apply cosine similarity. However, this turned out to be inaccurate since the output was gave us random movies which did not provide the user requirements
- Therefore, we decided to move on to a different approach. We deicded to use [OpenAI Embeddings](https://platform.openai.com/docs/guides/embeddings) to embed our concatenated features as well as the user query to apply cosine similarity and provide an output. This was a more accurate result. However, the constraint with using OpenAI Embeddings was that it took a long time to process and provide an output. The reason for this could be due to the fact that OpenAI's Ada model creates a list of 2048 floating point for each concatenated feature.

## Further changes in the future

## Features

- Recommends movies based on embedded features
- Applies cosine similarity to provide an output based on the query asked by the user
- Using Content-Based Filtering to provide a Top 5 movie list to the users based on their preference
- [PPT](https://azureloyalistcollege-my.sharepoint.com/:p:/g/personal/baldeepsingharora_loyalistcollege_com/EWxViRIabrVPvr6d3C6HXyUBGrEU82lyQY389OryytQ2yA?e=V2419i)

## Quick Start

Follow these instructions to get this project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8+
- pip
- Virtualenv (optional)

### Installation

1. Clone the repository to your local machine:
   ```
   https://github.com/abhi526691/Movie-Recommendation-System-using-NLTK.git
   ```

2. Navigate to the project directory:
   ```
   cd Movie-Recommendation-System-using-NLTK
   ```

3. Create a virtual environment (optional):
   ```
   virtualenv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```


7. Run the server:
   ```
   python manage.py runserver
   ```

## Built With

- [Django](https://www.djangoproject.com/) - The web framework used
- [NLTK](https://www.nltk.org/) - Model framework
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) - Frontend framework
- [OpenAI](https://platform.openai.com/docs/guides/embeddings) - OpenAI Embedding



## Contributor

<p align="center">

|                                                                                                                                                                                                                   <a href="https://github.com/abhi526691"><img src="https://avatars.githubusercontent.com/abhi526691" width="150px" height="150px" /></a>                                                                                                                                                                                                                    |
| :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|                                                                                                                                                                                                                                                             **[Abhishek Pandey](https://github.com/abhi526691)**                                                                                                                                                                                                                                                              |
| <a href="https://github.com/abhi526691"><img src="https://cdn.iconscout.com/icon/free/png-256/github-108-438008.png" width="32px" height="32px"></a> <a href="https://www.instagram.com/_abhishek__pandey___/"><img src="https://cdn.iconscout.com/icon/free/png-512/free-instagram-216-721958.png" width="32px" height="32px"></a> <a href="https://www.linkedin.com/in/abhishek-pandey-1515aa171/"><img src="https://i.ibb.co/Kx2GSrT/linkedin.png" width="32px" height="32px"></a><a href="https://www.facebook.com/abhishek10548"><img src="https://cdn.iconscout.com/icon/free/png-512/free-facebook-263-721950.png" width="32px" height="32px"></a> |

<hr/>

See also the list of [contributors](https://github.com/yourusername/mydjangowebapp/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
