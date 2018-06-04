![](https://raw.githubusercontent.com/taasmoe/Course-Similarities/master/Plots/example.png)

# Course-Similarities

A few experiments using t-SNE, k-means clustering, and kNN on the course descriptions from the [Department of Informatics](https://www.mn.uio.no/ifi/) at the Univeristy of Oslo.

Web scraping done with [requests](http://docs.python-requests.org/en/master/).

Vectorization, t-SNE, k-means clustering, and kNN are done with [scikit-learn](http://scikit-learn.org/stable/index.html)

## Data preparation

For these tasks I extract and vectorize all the course descriptions from UiO's webpages, using sckit-learns _TfIdfVectorizer_.

## t-SNE

t-SNE allow us to visualize the high-dimensional data in two dimensions.

![](https://raw.githubusercontent.com/taasmoe/Course-Similarities/master/Plots/t-sne.png)

## k-means

We can cluster the data, and visualize the results with t-SNE.

![](https://raw.githubusercontent.com/taasmoe/Course-Similarities/master/Plots/k-means.png)

## kNN

We can extract the k nearest neighbors of any course in our list.



```
k_nearest_neighbor('INF3121', 5)

> ['INF4121', 'UNIK9270', 'UNIK4270', 'IN2000']
```
