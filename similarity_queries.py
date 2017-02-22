import os
import logging

from pprint import pprint
from gensim import corpora, models, similarities

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

dictionary = None
corpus = None


if os.path.exists("course_dictionary.dict"):
    dictionary = corpora.Dictionary.load("dictionary.dict")
    corpus = corpora.MmCorpus("corpus.mm")
else:
    print("Error")

lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=2)

