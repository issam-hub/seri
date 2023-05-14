from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


def retrieval(query):
    df = pd.read_table("my-dataset/collection.tsv")

    tfidf = TfidfVectorizer(stop_words='english', analyzer="word")
    tfidf2 = TfidfVectorizer(stop_words='english', analyzer="word")

    # indexation of corpus
    tfidf_matrix = tfidf.fit_transform(df['doc_text'])

    doc_feature_names = list(tfidf.get_feature_names_out())

    # indexation of query
    queryTFIDF = TfidfVectorizer().fit(doc_feature_names)
    queryTFIDF = queryTFIDF.transform([query])

    cos_sim = cosine_similarity(queryTFIDF, tfidf_matrix).flatten()

    result = {df["doc_id"][i]: cos_sim[i] for i in range(len(cos_sim))}

    final_result = sorted(result.items(), key=lambda e: e[1], reverse=True)

    return final_result


def get_rel(query_id: int, doc_id):
    qrels = pd.read_table("my-dataset/test/qrels")

    arr = qrels[qrels["query_id"] == query_id]

    v = arr[arr["doc_id"] == doc_id]["rel"].values

    return v or [1]
