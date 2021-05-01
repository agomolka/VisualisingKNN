import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets, neighbors
from mlxtend.plotting import plot_decision_regions


class KnnVisualisation2d:
    train_set = ""
    data = ""
    k = 1

    def __init__(self, data, k):
        # super(KnnVisualisation2d, self).__init__(train_set, k)
        # self.test_set = test_set
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
        plt.title("Knn with K=" + str(self.k))
        plt.show()


def main():
    data2 = pd.read_csv("/Users/ola/Downloads/archive/concertriccir2.csv")
    for i in [1, 5, 20, 30, 40, 60]:
        o = KnnVisualisation2d(data2, i)
        o.knn_comparison()


if __name__ == '__main__':
    main()
