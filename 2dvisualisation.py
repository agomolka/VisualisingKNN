import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets, neighbors
from mlxtend.plotting import plot_decision_regions
import wx
import wxmplot
import seaborn as sns
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure


class KnnVisualisation2d(wx.Panel):
    train_set = ""
    data = ""
    k = 1


    def __init__(self, parent, data, k):
        # super(KnnVisualisation2d, self).__init__(data, k)
        # self.test_set = test_set
        wx.Panel.__init__(self, parent)
        self.data = data
        self.k = k
        plt.figure()
        self.figure = Figure()
        # self.ax = self.figure.add_subplot(111)
        self.ax = self.figure.add_subplot(111)
        # sns.pairplot(self.data, height=2, hue="class", markers=["o", "s"])
        sns.FacetGrid(self.data, size=5, hue="class").map(plt.scatter, "X", "Y").add_legend()
        self.canvas =FigureCanvas(self, -1, self.figure)
        # plt.show()
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.SetSizer(self.sizer)
        self.Fit()



def main():
    data2 = pd.read_csv("archive/concertriccir2.csv")
    for i in [1, 5, 20, 30, 40, 60]:
        app = wx.App()
        fr = wx.Frame(None, title='2d - knn', size=(800, 600))
        panel = KnnVisualisation2d(fr, data2, i)
        fr.Show()
        app.MainLoop()

if __name__ == '__main__':
    main()