import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets, neighbors
from mlxtend.plotting import plot_decision_regions
import wx
import wxmplot


class KnnVisualisation2d:
    train_set = ""
    data = ""
    k = 1

    def __init__(self, data, k):
        # super(KnnVisualisation2d, self).__init__(data, k)
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
        plt.title("k-NN with k=" + str(self.k))
        plt.show()
        # pframe.Show()



def main():
    data2 = pd.read_csv("archive/concertriccir2.csv")
    for i in [1, 5, 20, 30, 40, 60]:
        window = KnnVisualisation2d(data2, i)
        window.knn_comparison()

if __name__ == '__main__':
    main()



class ShowVisualisation(wx.Frame):
    data = None
    i = 1

    def __init__(self, data, i):
        # super(ShowVisualisation, self).__init__(data, i)
        self.data = data
        self.i = i
        self.init()
        # self.Centre()

    def init(self):
        app = wx.App()
        # panel = wx.Panel(self)
        # vbox = wx.BoxSizer(wx.VERTICAL)
        # self.plot = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap("mincol.jpg", wx.BITMAP_TYPE_ANY))
        o = KnnVisualisation2d(self.data, self.i)
        pframe = wxmplot.PlotFrame()
        o.knn_comparison()
        pframe.o
        # plot = wx.Frame(panel, o.knn_comparison())
        # plot.SetPosition((20, 20))
        pframe.Show()
        # vbox.Add(pframe)
        # vbox.Add(plot)
        # panel.SetSizer(vbox)
        # panel.Show()
        app.MainLoop()