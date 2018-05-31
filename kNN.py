from sklearn.neighbors import KNeighborsClassifier

from data_preparation import load_data

features_titles_tuple = load_data()

X = features_titles_tuple[0]
titles = features_titles_tuple[1]


def k_nearest_neighbor(course_id, k=5):
    try:
        index = titles.index(course_id)

        model = KNeighborsClassifier()
        model.fit(X, titles)

        neighbor_indices = model.kneighbors(X[index], n_neighbors=k)[1][0]

        return [titles[i] for i in neighbor_indices[1:]]

    except:
        raise

print(k_nearest_neighbor('INF3121', 5))
