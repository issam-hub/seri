import pandas as pd
import numpy as np
import math
from functions import *


# my_queries = ["Why doesn't the water fall off  earth if it's round?"]
# my_queries_id = [714612]


# evaluation_SRI_reference_file()
evaluation_file()

our_avg_precisions = [0] * 11
reference_avg_precisions = [0] * 11

# make graphs to compare queries (each with each)

queries = pd.read_table("my-dataset/test/queries.txt")
queries_id = pd.read_table("my-dataset/test/queries.txt")["query_id"]
reference_rel = pd.read_table("rels_SRI.txt")
our_rel = pd.read_table("rels3.txt")

for query_id in queries_id:
    our_rappels = list(filter(lambda e: not math.isnan(e), our_rel[our_rel["query_id"] == query_id]["rappel"]))
    our_precisions = list(filter(lambda e: not math.isnan(e), our_rel[our_rel["query_id"] == query_id]["precision"]))
    reference_rappels = list(filter(lambda e: not math.isnan(e), reference_rel[reference_rel["query_id"] == query_id]["rappel"]))
    reference_precisions = list(filter(lambda e: not math.isnan(e), reference_rel[reference_rel["query_id"] == query_id]["precision"]))

    our_precisions = interpolation(our_rappels, our_precisions)
    reference_precisions = interpolation(reference_rappels, reference_precisions)

    title = queries[queries["query_id"] == query_id]["query_text"].values[0]
    # compare_preformance(title, our_precisions, reference_precisions)

    for i in range(11):
        our_avg_precisions[i] += our_precisions[i]
        reference_avg_precisions[i] += reference_precisions[i]

# make graphs to compare queries (avg_graphe)

our_avg_precisions = list(map(lambda e: e/len(queries_id), our_avg_precisions))
reference_avg_precisions = list(map(lambda e: e/len(queries_id), reference_avg_precisions))

title = "avg"
compare_preformance(title, our_avg_precisions, reference_avg_precisions)
