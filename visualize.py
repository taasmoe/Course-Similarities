import matplotlib.pyplot as plt
import numpy as np

from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA

from data_preparation import load_data

# Load the data
features_titles_tuple = load_data()

X = features_titles_tuple[0]
titles = features_titles_tuple[1]


def visualize(clustering=False, plot_titles=False, pre_decomposition=False, save_svg=False):
    """
    Visualizes our vectorized data, with clustering, course titles, PCA demcoposition anc image saving as options
    """

    # The t-SNE model, reducing the dimensionality of a vector space to 2 dimensions.
    t_sne = TSNE(n_components=2,
                 random_state=0,
                 perplexity=45,
                 learning_rate=200)

    # Dense representation, needed for t-SNE.
    data_nd = X.toarray()

    if pre_decomposition is True:
        N = 100
        pca = PCA(n_components=N)
        data_nd = pca.fit_transform(data_nd)

        # Check wheter the decomposition preserves the variance of the original data
        print('Cumulative explained variation for ' + str(N) + ' components = ',
              np.sum(pca.explained_variance_ratio_))

    # 2D reperesantation of our original data
    descriptions_2d = t_sne.fit_transform(data_nd)

    # High figsize in order to interpret the plots better
    fig, ax = plt.subplots()
    plt.figure(figsize=(300, 300))

    # Assuming that one course often has a similar course, we cluster the data into about a half of the amount of
    # points in the space:
    if clustering is True:
        model = KMeans(n_clusters=140)
        model.fit(X)
        y = model.labels_
        label_set = list(set(model.labels_))
        target_ids = range(len(label_set))

        # Plotting these separately, with different colors.
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

    # Annotating each plot in correspondance with the course titles
    if plot_titles is True:
        for i, title in enumerate(titles):
            ax.annotate(title,
                        (descriptions_2d[:, 0][i],
                         descriptions_2d[:, 1][i]),
                        size=1)

    # Saves the image as an .svg file
    if save_svg is True:
        fig.savefig('courses.svg')

    plt.show()

# Example usage
visualize(plot_titles=True,
          save_svg=True,
          clustering=True)
