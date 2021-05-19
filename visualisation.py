import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets, neighbors
from mlxtend.plotting import plot_decision_regions


class KnnVisualisation2d:
    """
    Visualisation by mlxtend k-nn algorithm
    for two variables
    """

    train_set = ""
    data = ""
    k = 1

    def __init__(self, data, k):
        self.data = data
        self.k = k

    def knn_comparison(self):
        x = self.data[["X", "Y"]].values
        y = self.data["class"].astype(int).values
        clf = neighbors.KNeighborsClassifier(n_neighbors=self.k)
        clf.fit(x, y)
        # Plotting decision region
        plot_decision_regions(x, y, clf=clf, legend=2)
        # Adding axes annotations
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("k-NN with k=" + str(self.k))
        name = f'img/knn' + str(self.k) + '.png'
        plt.savefig(name)


def main(k_array, data):
    data2 = pd.read_csv(data)
    for i in k_array:
        window = KnnVisualisation2d(data2, i)
        window.knn_comparison()


if __name__ == '__main__':
    main()