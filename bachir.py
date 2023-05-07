import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

tfidf = TfidfVectorizer(stop_words='english', analyzer='word')

removeStopWordsFunc = tfidf.build_analyzer()
bow = removeStopWordsFunc("hello world from down street and welcome back")

# print(tfidf.fit_transform(bow))
print("hello")


# df = pd.read_csv("small/tmdb_5000_movies.csv")

# tfidf = TfidfVectorizer(stop_words='english')

# df['overview'] = df['overview'].fillna('')


# tfidf_matrix = tfidf.fit_transform(df['overview'])

# tfidfshow = pd.DataFrame(tfidf_matrix.toarray())
# # Import linear_kernel

# # Compute the cosine similarity matrix
# cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)


# indices = pd.Series(df.index, index=df['title']).drop_duplicates()


# # Function that takes in movie title as input and outputs most similar movies
# def get_recommendations(title, cosine_sim=cosine_sim):
#     # Get the index of the movie that matches the title
#     idx = indices[title]

#     # Get the pairwsie similarity scores of all movies with that movie
#     sim_scores = list(enumerate(cosine_sim[idx]))

#     # Sort the movies based on the similarity scores
#     sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

#     # Get the scores of the 10 most similar movies
#     sim_scores = sim_scores[1:11]

#     # Get the movie indices
#     movie_indices = [i[0] for i in sim_scores]

#     # Return the top 10 most similar movies
#     return df['title'].iloc[movie_indices]

# userInput = input("enter the movie's title: ")

# userInput = userInput.title()

# print(get_recommendations(userInput))

