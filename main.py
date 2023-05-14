import pandas as pd
import numpy as np
from functions import *

queries = pd.read_table("my-dataset/test/queries.txt")

my_queries = list(queries["query_text"])
my_queries_id = list(queries["query_id"])
# my_queries = ["Why doesn't the water fall off  earth if it's round?"]
# my_queries_id = [714612]

for i in range(len(my_queries)):
    query = my_queries[i]
    result = retrieval(query)

    docs = list(map(lambda e: e[0], result))[:30]
    query = [my_queries_id[i]] * len(docs)

    rels = []
    for i in range(len(docs)):
        rels.append(get_rel(query[i], docs[i]))

    rels = list(map(lambda e: e[0], rels))
    print(rels)
    exit()

    rel2 = pd.DataFrame({query[0]: query[1:], docs[0]: docs[1:], rels[0]: rels[1:]})

    file = open("rels3.txt", "a")
    file.write(rel2.to_csv(sep="\t", index=None))
