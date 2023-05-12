# dataset documentation link: https://ir-datasets.com/antique.html#antique/test

# download docs
# import ir_datasets
# dataset = ir_datasets.load("antique/test")
# for doc in dataset.docs_iter():
#     doc  # namedtuple<query_id, text, tags>

# download queries
# import ir_datasets
# dataset = ir_datasets.load("antique/test")
# for query in dataset.queries_iter():
#     query

# download relevance
# import ir_datasets
# dataset = ir_datasets.load("antique/test")
# for qrel in dataset.qrels_iter():
#     qrel

# keep the documents of appearing in qrels
# import pandas as pd
# import numpy as np

# rels = pd.read_table("my-dataset/test/qrels")

# l = list(rels["doc_id"])

# file = open("my-dataset/collection.tsv", "w+")

# lines = file.readlines()

# result = []

# for line in lines:
#     if ((line.split("\t")[0]) in l):
#         result.append(line)

# file.writelines(result)
