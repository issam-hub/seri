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
    result = retrieval(query)

    docs = list(map(lambda e: e[0], result))[:n_selected]
    query = [my_queries_id[i]] * len(docs)

    rels = []

    for k in range(len(docs)):
        rels.append(get_rel(query[k], docs[k])[0])

    n_doc_pert = rels.count(3) + rels.count(4)

    rappels = []
    precisions = []
    pertinant_select = 0
    for j in range(n_selected):
        if (rels[j] in [3, 4]):
            pertinant_select += 1
            rappels.append((pertinant_select/n_doc_pert).__round__(2))
            precisions.append((pertinant_select/(j+1)).__round__(2))
        else:
            rappels.append("")
            precisions.append("")

    print(i)
    print(rappels)
    print(precisions)
    rel2 = pd.DataFrame({query[0]: query[1:], docs[0]: docs[1:], rels[0]: rels[1:], rappels[0]: rappels[1:], precisions[0]: precisions[1:]})

    file = open("rels3.txt", "a")
    file.write(rel2.to_csv(sep="\t", index=None))
