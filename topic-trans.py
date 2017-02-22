import os
import logging

from gensim import corpora, models

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

dictionary = None
corpus = None


if os.path.exists("Data/course_dictionary.dict"):
    dictionary = corpora.Dictionary.load("Data/course_dictionary.dict")
    corpus = corpora.MmCorpus("Data/corpus.mm")
else:
    print("Error")

# TF-IDF Weighting

tfidf = models.TfidfModel(corpus)

corpus_tfidf = tfidf[corpus]

lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=2)
corpus_lsi = lsi[corpus_tfidf]

lsi.save("Data/model.lsi")
lsi = models.LsiModel.load("Data/model.lsi")

tfidf_model = models.TfidfModel(corpus, normalize=True)
