import pandas as pd
# import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

tfidf = TfidfVectorizer(stop_words="english", analyzer="word")

removedWords = tfidf.build_analyzer()

result = removedWords("hello world from down street yeah baby that's what i'm talking about here right now hello")

