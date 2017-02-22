import os
import logging
import pickle

from pprint import pprint
from gensim import corpora, models, similarities

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

dictionary = None
corpus = None

if os.path.exists("course_dictionary.dict"):
    dictionary = corpora.Dictionary.load("course_dictionary.dict")
    corpus = corpora.MmCorpus("corpus.mm")
else:
    print("Error")

with open("course_info.txt", "rb") as f:
    course_info = pickle.load(f)

lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=2)

print(course_info[0])
test_doc = course_info[0]
vec_bow = dictionary.doc2bow(test_doc)
vec_lsi = lsi[vec_bow]

index = similarities.MatrixSimilarity(lsi[corpus])
index.save("sim-index.index")

sims = index[vec_lsi]

sims = sorted(enumerate(sims), key=lambda item: -item[1])

print(sims)