import matplotlib.pyplot as plt
import numpy as np

from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA

from data_preparation import load_data

features_titles_tuple = load_data()

X = features_titles_tuple[0]
titles = features_titles_tuple[1]


def visualize(clustering=False, plot_titles=False, pre_decomposition=False, save_svg=False):
    t_sne = TSNE(n_components=2,
                 random_state=0,
                 perplexity=45,
                 learning_rate=200)

    data_nd = X.toarray()

    if pre_decomposition is True:
        N = 100
        pca = PCA(n_components=N)
        data_nd = pca.fit_transform(data_nd)

        print('Cumulative explained variation for ' + str(N) + ' components = ',
              np.sum(pca.explained_variance_ratio_))

    descriptions_2d = t_sne.fit_transform(data_nd)
    print(descriptions_2d)

    fig, ax = plt.subplots()
    plt.figure(figsize=(300, 300))

    if clustering is True:
        model = KMeans(n_clusters=145)
        model.fit(X)
        y = model.labels_
        label_set = list(set(model.labels_))
        target_ids = range(len(label_set))

        for i, label in zip(target_ids, label_set):
            ax.scatter(descriptions_2d[y == i, 0],
                       descriptions_2d[y == i, 1],
                       marker='.',
                       s=1)
    else:
        ax.scatter(descriptions_2d[:, 0],
                   descriptions_2d[:, 1],
                   marker='.',
                   s=1)

    if plot_titles is True:
        for i, title in enumerate(titles):
            ax.annotate(title,
                        (descriptions_2d[:, 0][i],
                         descriptions_2d[:, 1][i]),
                        size=1)

    if save_svg is True:
        fig.savefig('courses.svg')

    plt.show()

visualize(plot_titles=True,
          save_svg=True)
