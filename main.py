import os
import wx
import VisualisationThreeVarTest
import visualisation
import VisualisationThreeVar
import VisualisationTwoTest
import pandas as pd


class OtherFrame(wx.Frame):
    """
    Class used for creating frames other than the main one
    """

    def __init__(self, title, parent=None):
        wx.Frame.__init__(self, parent=parent, title=title)
        self.Show()


class Visualisation(wx.Frame):
    """
    Show main window of application: apply set, and visualize
    """
    k_array = [1, 5, 20, 60]

    def __init__(self, parent, title):
        super(Visualisation, self).__init__(parent, title=title)
        self.init()
        self.Centre()
        self.Bind(wx.EVT_CLOSE, self.closeWindow)  # Bind the EVT_CLOSE event to closeWindow()

    def closeWindow(self, event):
        self.Destroy()
        # self.Destroy()  # This will close the app window.

    def init(self):
        panel = wx.Panel(self)
        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)
        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox11 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(panel, label='Choose training set (only .txt or .csv):')
        st1.SetFont(font)
        hbox11.Add(st1, flag=wx.RIGHT, border=8)
        vbox.Add(hbox11, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        hbox12 = wx.BoxSizer(wx.HORIZONTAL)
        wildcard = "CSV file (*.csv)|*.csv|Txt file (*.txt)|*.txt||"
        self.tc = wx.FilePickerCtrl(panel, message="Select training set", wildcard=wildcard, style=wx.FLP_USE_TEXTCTRL, size=(390, 25))
        hbox12.Add(self.tc, proportion=1)
        vbox.Add(hbox12, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        vbox.Add((-1, 10))

        hbox21 = wx.BoxSizer(wx.HORIZONTAL)
        st2 = wx.StaticText(panel, label='Choose testing set (only .txt or .csv):')
        st2.SetFont(font)
        hbox21.Add(st2, flag=wx.RIGHT, border=8)
        vbox.Add(hbox21, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        hbox22 = wx.BoxSizer(wx.HORIZONTAL)
        wildcard = "CSV file (*.csv)|*.csv|Txt file (*.txt)|*.txt||"
        self.tc2 = wx.FilePickerCtrl(panel, message="Select testing set", wildcard=wildcard, style=wx.FLP_USE_TEXTCTRL, size=(390, 25))
        hbox22.Add(self.tc2, proportion=1)
        vbox.Add(hbox22, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        vbox.Add((-1, 10))

        #Visualize button
        hbox6 = wx.BoxSizer(wx.HORIZONTAL)
        btn1 = wx.Button(panel, label='VISUALIZE', size=(90, 30))
        # which k are choosen for iteration in k-nn
        btn1.Bind(wx.EVT_BUTTON, self.on_new_frame)
        self.frame_number = len(self.k_array)
        hbox6.Add(btn1)
        vbox.Add(hbox6, flag=wx.ALIGN_RIGHT | wx.RIGHT, border=10)
        vbox.Add((-1, 25))
        panel.SetSizer(vbox)

    def on_new_frame(self, event):
        """
        Checking is there test and train set and starting right algorithm
        """
        path = self.tc.GetPath()
        patch_test = self.tc2.GetPath()
        data = pd.read_csv(path)
        if patch_test == "":
            if len(data.columns) <= 3:
                visualisation.main(self.k_array, path)
                for i in range(0, len(self.k_array)):
                    title = 'k-nn with k={}'.format(str(self.k_array[i]))
                    frame = OtherFrame(title=title)
                    self.frame_number += 1
                    image_file = f'img/knn' + str(self.k_array[i]) + '.png'
                    png = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
                    wx.StaticBitmap(frame, -1, png, size=(png.GetWidth(), png.GetHeight()))
            else:
                VisualisationThreeVar.main(path, self.k_array)
        else:
            if len(data.columns) <= 3:
                VisualisationTwoTest.main(self.k_array, path, patch_test)
            else:
                VisualisationThreeVarTest.main(self.k_array, path, patch_test)
def main():
    app = wx.App()
    ex = Visualisation(None, title='k-NN Visualizator')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()


