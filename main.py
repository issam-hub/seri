import pandas as pd
import numpy as np
from functions import *

n_selected = 30

queries = pd.read_table("my-dataset/test/queries.txt")

my_queries = list(queries["query_text"])
my_queries_id = list(queries["query_id"])
# my_queries = ["Why doesn't the water fall off  earth if it's round?"]
# my_queries_id = [714612]


for i in range(len(my_queries)):
    query = my_queries[i]
    query_id = my_queries_id[i]
    result = retrieval(query)

    qrels = pd.read_table("my-dataset/test/qrels")
    arr = qrels[qrels["query_id"] == query_id]

    n_doc_pert = len(arr[arr["rel"] == 3])
    n_doc_pert += len(arr[arr["rel"] == 4])

    docs = list(map(lambda e: e[0], result))[:n_selected]
    query = [my_queries_id[i]] * len(docs)

    rels = []

    for k in range(len(docs)):
        rels.append(get_rel(query[k], docs[k])[0])

    # n_doc_pert = rels.count(3) + rels.count(4)

    rappels = []
    precisions = []
    pertinant_select = 0
    for j in range(n_selected):
        if (rels[j] in [3, 4]):
            pertinant_select += 1
            rappels.append(pertinant_select/n_doc_pert)
            precisions.append(pertinant_select/(j+1))
        else:
            rappels.append("")
            precisions.append("")

    print(i)
    print(rappels)
    print(precisions)
    print(query)

    file = open("rels3.txt", "a")
    # rel2 = pd.DataFrame({query[0]: query[1:], docs[0]: docs[1:], rels[0]: rels[1:], rappels[0]: rappels[1:], precisions[0]: precisions[1:]})

    for line_i in range(n_selected):
        file.write("{}\t{}\t{}\t{}\t{}\n".format(query[line_i], docs[line_i], rels[line_i], rappels[line_i], precisions[line_i]))
