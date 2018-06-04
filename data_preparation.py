import pickle

from sklearn.feature_extraction.text import TfidfVectorizer

with open('Data/courses.pkl', 'rb') as f:
    courses = pickle.load(f)

# Get descriptions and course titles separately
descriptions = [c[1] for c in courses]
titles = [c[0].split(' – ')[0] for c in courses]

# Vectorize the descriptions
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(descriptions)


def load_data():
    """ Returns the vectorized descriptions and titles as a tuple (in order to access these in other scripts) """
    return X, titles
