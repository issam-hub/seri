from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt


def interpolation(rappels: list, precisions: list) -> list:
    precision_i = []

    for rj in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]:
        print(rj)
        rappel_after_rj = []
        precision_after_rj = []
        for i in range(len(rappels)):
            rappel = rappels[i]
            precision = precisions[i]
            if (rappel >= rj):
                rappel_after_rj.append(rappel)
                precision_after_rj.append(precision)
                print(precision_after_rj)
        if (len(precision_after_rj) > 0):
            precision_i.append(max(precision_after_rj))
        else:
            precision_i.append(0)

    return precision_i


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


def evaluation_file():
    n_selected = 30

    qrels = pd.read_table("my-dataset/test/qrels")

    queries = pd.read_table("my-dataset/test/queries.txt")

    my_queries = list(queries["query_text"])
    my_queries_id = list(queries["query_id"])

    for i in range(len(my_queries)):
        query = my_queries[i]
        query_id = my_queries_id[i]
        result = retrieval(query)

        arr = qrels[qrels["query_id"] == query_id]

        n_doc_pert = len(arr[arr["rel"] == 3])
        n_doc_pert += len(arr[arr["rel"] == 4])

        # to calculate precision for our SRI
        docs = list(map(lambda e: e[0], result))[:n_selected]
        query = [my_queries_id[i]] * len(docs)

        rels = []

        for k in range(len(docs)):
            rels.append(get_rel(query[k], docs[k])[0])

        # n_doc_pert = rels.count(3) + rels.count(4)

        rappels = []
        plt_rappels = []
        precisions = []
        plt_precisions = []
        pertinant_select = 0
        for j in range(n_selected):
            if (rels[j] in [3, 4]):
                pertinant_select += 1
                rappels.append(pertinant_select/n_doc_pert)
                precisions.append(pertinant_select/(j+1))
                plt_rappels.append(pertinant_select/n_doc_pert)
                plt_precisions.append(pertinant_select/(j+1))
            else:
                rappels.append("")
                precisions.append("")

        plt.plot([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1], interpolation(plt_rappels, plt_precisions))
        plt.xlabel("rappel")
        plt.ylabel("precision")
        # plt.show()

        file = open("rels3.txt", "a")
        rel2 = pd.DataFrame({query[0]: query[1:], docs[0]: docs[1:], rels[0]: rels[1:], rappels[0]: rappels[1:], precisions[0]: precisions[1:]})

        for line_i in range(n_selected):
            file.write("{}\t{}\t{}\t{}\t{}\n".format(query[line_i], docs[line_i], rels[line_i], rappels[line_i], precisions[line_i]))


def evaluation_SRI_reference_file():
    n_selected = 30

    qrels = pd.read_table("my-dataset/test/qrels")

    queries = pd.read_table("my-dataset/test/queries.txt")

    my_queries = list(queries["query_text"])
    my_queries_id = list(queries["query_id"])
    print(len(my_queries))
    print(len(my_queries_id))

    for i in range(len(my_queries)):
        query = my_queries[i]
        query_id = my_queries_id[i]

        arr = qrels[qrels["query_id"] == query_id]
        n_doc_pert = len(arr[arr["rel"] == 3])
        n_doc_pert += len(arr[arr["rel"] == 4])

        # to calculate precision for reference SRI
        docs = list(arr["doc_id"])[:n_selected]
        query = [query_id] * len(docs)
        # print(len(docs))
        # continue
        rels = []

        for k in range(len(docs)):
            rels.append(get_rel(query[k], docs[k])[0])

        # n_doc_pert = rels.count(3) + rels.count(4)

        rappels = []
        plt_rappels = []
        precisions = []
        plt_precisions = []
        pertinant_select = 0
        for j in range(len(docs)):
            if (rels[j] in [3, 4]):
                pertinant_select += 1
                rappels.append(pertinant_select/n_doc_pert)
                precisions.append(pertinant_select/(j+1))
                plt_rappels.append(pertinant_select/n_doc_pert)
                plt_precisions.append(pertinant_select/(j+1))
            else:
                rappels.append("")
                precisions.append("")

        plt.plot([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1], interpolation(plt_rappels, plt_precisions))
        plt.xlabel("rappel")
        plt.ylabel("precision")
        # plt.show()

        file = open("rels_SRI.txt", "a")
        # rel2 = pd.DataFrame({query[0]: query[1:], docs[0]: docs[1:], rels[0]: rels[1:], rappels[0]: rappels[1:], precisions[0]: precisions[1:]})
        print(len(docs))
        for line_i in range(len(docs)):
            file.write("{}\t{}\t{}\t{}\t{}\n".format(query[line_i], docs[line_i], rels[line_i], rappels[line_i], precisions[line_i]))
