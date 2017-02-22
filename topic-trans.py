import os
import logging

from gensim import corpora, models, similarities

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

dictionary = None
corpus = None


if os.path.exists("course_dictionary.dict"):
    dictionary = corpora.Dictionary.load("course_dictionary.dict")
    corpus = corpora.MmCorpus("corpus.mm")
else:
    print("Error")

# TF-IDF Weighting

tfidf = models.TfidfModel(corpus)

corpus_tfidf = tfidf[corpus]

lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=2)
corpus_lsi = lsi[corpus_tfidf]
