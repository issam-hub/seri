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

    # indexation of query
    query_tfidf_matrix = tfidf2.fit_transform([query])

    np.matrix(query_tfidf_matrix)
    query_tfidfshow = pd.DataFrame(query_tfidf_matrix.toarray(), columns=tfidf2.get_feature_names_out(query))

    doc_feature_names = list(tfidf.get_feature_names_out())
    query_feature_names = list(tfidf2.get_feature_names_out())

    arr = [0] * len(doc_feature_names)

    for query_word in query_feature_names:
        if doc_feature_names.__contains__(query_word):
            arr[doc_feature_names.index(query_word)] = query_tfidfshow[query_word][0]

    query_matrix = [arr]*len(df['doc_text'])

    cos_sim = cosine_similarity(query_matrix, tfidf_matrix)

    result = {df["doc_id"][i]: cos_sim[0][i] for i in range(len(cos_sim[0]))}

    final_result = sorted(result.items(), key=lambda e: e[1], reverse=True)

    return final_result


def get_rel(query_id: int, doc_id):
    qrels = pd.read_table("my-dataset/test/qrels")

    arr = rels[rels["query_id"] == query_id]

    return arr[arr["doc_id"] == doc_id]["rel"]
