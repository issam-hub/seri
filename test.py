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
import ir_datasets
dataset = ir_datasets.load("antique/test")
for qrel in dataset.qrels_iter():
    qrel
