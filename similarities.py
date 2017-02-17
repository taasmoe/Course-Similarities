import nltk
import timeit
import pickle
import numpy as np


from pprint import pprint
from gensim import corpora

start = timeit.default_timer()

with open("courses.pkl", "rb") as f:
    courses = pickle.load(f)


for key, value in courses.items():
    if value["about"] == "":
        print(key, value)

end = timeit.default_timer()

print("Completed in", start-end, "seconds")
