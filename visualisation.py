import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets, neighbors
from mlxtend.plotting import plot_decision_regions
import wx


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


class ShowVisualisation(wx.Frame):

    def __init__(self):
        super(ShowVisualisation, self).__init__(parent, title=title, size=(350, 300))

        self.init()
        self.Centre()

    def init(self):
        panel = wx.Panel(self)

        # self.plot = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap("mincol.jpg", wx.BITMAP_TYPE_ANY))
        o = KnnVisualisation2d(self.data, self.k)
        o.knn_comparison()
        plot = wx.Frame(panel, KnnVisualisation2d(self.data, self.k))

        plot.SetPosition((20, 20))



def main():
    data2 = pd.read_csv("/Users/ola/Downloads/archive/concertriccir2.csv")
    for i in [1, 5, 20, 30, 40, 60]:
        o = ShowVisualisation(data2, i)


if __name__ == '__main__':
    main()
