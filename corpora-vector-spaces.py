import os
import logging
import string
import timeit
import pickle

from langdetect import detect

from pprint import pprint
from collections import defaultdict

from gensim import corpora, models, similarities
from nltk import word_tokenize
from nltk.corpus import stopwords

start = timeit.default_timer()

with open("courses.pkl", "rb") as f:
    courses = pickle.load(f)

stop_words_NOR = set(stopwords.words("norwegian"))
stop_words_ENG = set(stopwords.words("english"))

# Tokenization and removal of stopwords

documents = []

for course, info in courses.items():
    documents.append((course, [info["about"] + info["outcome"]]))

course_titles = [document[0] for document in documents]
course_info = [document[1] for document in documents]

course_info = [word_tokenize(info[0].lower()) for info in course_info]

course_info_NOR = []
course_info_ENG = []

for info in course_info:
    text = " ".join(info)

    if detect(text) == "no":
        course_info_NOR.append([word for word in info if word not in stop_words_NOR])
    else:
        course_info_ENG.append([word for word in info if word not in stop_words_ENG])

course_info = course_info_ENG + course_info_NOR


# Hyphen removal

word_frequencies = defaultdict(int)

for info in course_info:
    for token in info:
        word_frequencies[token] += 1

course_info = [[token for token in info if word_frequencies[token] > 1] for info in course_info]

# Removal of punctuation, empty lists and empty strings

punctuation_table = dict.fromkeys(map(ord, string.punctuation), None)

course_info = [[token.translate(punctuation_table) for token in info] for info in course_info]
course_info = [list(filter(None, info)) for info in course_info]
course_info = list(filter(None, course_info))

dictionary = corpora.Dictionary(course_info)
dictionary.save("course_dictionary.dict")

corpus = [dictionary.doc2bow(info) for info in course_info]
corpora.MmCorpus.serialize("corpus.mm", corpus)

end = timeit.default_timer()

print("Completed in", start-end, "seconds")
