import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE

from data_preparation import load_data

features_titles_tuple = load_data()

X = features_titles_tuple[0]
titles = features_titles_tuple[1]


def visualize(clustering=False, titles=False, save=False):
    t_sne = TSNE(n_components=2,
                 random_state=0,
                 perplexity=50,
                 learning_rate=200)

    data_nd = X.toarray()

    descriptions_2d = t_sne.fit_transform(data_nd)

    if clustering is True:
        model = KMeans(n_clusters=145)

        model.fit(X)
        y = model.labels_
        label_set = list(set(model.labels_))
        target_ids = range(len(label_set))

        for i, label in zip(target_ids, label_set):
            plt.scatter(descriptions_2d[y == i, 0],
                        descriptions_2d[y == i, 1],
                        s=20)
    else:
        fig, ax = plt.subplots()
        plt.figure(figsize=(300, 300))

        ax.scatter(descriptions_2d[:, 0],
                   descriptions_2d[:, 1])

        if titles is True:
            for i, title in enumerate(titles):
                ax.annotate(title,
                            (descriptions_2d[:, 0][i],
                             descriptions_2d[:, 1][i]),
                            size=3)

    plt.show()

visualize(clustering=True)