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

# file = open("my-dataset/collection.tsv", "r")

# lines = file.readlines()

# # result = []

# result = {}

# filtered_lines = []

# for line in lines:
#     if ((line.split("\t")[0]) in l):
#         filtered_lines.append(line)

# # print(lines)

# for line in lines:
#     if lines.count(line) == 2:
#         lines.pop(lines.index(line))

# file2 = open("my-dataset/collection2.tsv", "w")

# file2.writelines(filtered_lines)

# remove the blacklist queries from queries file

# blacklist = open("blacklist.txt", "r")

# queries_f_r = open("my-dataset/test/queries.txt", "r")

# b_queries = list(map(lambda e: e[:-1], blacklist.readlines()))
# queries = queries_f_r.readlines()

# queries_f_r.close()


# filtered_lines = list(filter(lambda e: not (e.split("\t")[0] in b_queries), queries))

# queries_f_w = open("my-dataset/test/queries.txt", "w")

# queries_f_w.writelines(filtered_lines)

# queries_f_w.close()

# exit()

# keep the documents related to the queries only (in qrels)
# import pandas as pd
# import re

# pd.read_table("my-dataset/test/queries.txt")

# qrels = open("my-dataset/test/qrels", "r")

# qrels_lines = qrels.readlines()
# qrels.close()

# queries = list(map(lambda e: str(e), pd.read_table("my-dataset/test/queries.txt")["query_id"]))


# lines_filtered = list(filter(lambda e: (e.split(" ")[0] in queries), qrels_lines))

# qrels_w = open("my-dataset/test/qrels", "w")
# qrels_w.writelines(lines_filtered)
# qrels_w.close()
