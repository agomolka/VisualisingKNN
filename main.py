import os
import wx


class Visualisation(wx.Frame):

    patch = ""

    def __init__(self, parent, title):
        super(Visualisation, self).__init__(parent, title=title)

        self.init()
        self.Centre()

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
        wildcard = "TXT and CSV files (*.txt; *.csv)|*.txt; *.csv"
        tc = wx.FilePickerCtrl(panel, message="Select file", wildcard=wildcard, style=wx.FLP_USE_TEXTCTRL, size=(390, 25))
        self.patch = tc.GetPath()
        hbox12.Add(tc, proportion=1)
        vbox.Add(hbox12, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        vbox.Add((-1, 10))

        hbox21 = wx.BoxSizer(wx.HORIZONTAL)
        st2 = wx.StaticText(panel, label='Choose test set (only .txt or .csv):')
        st2.SetFont(font)
        hbox21.Add(st2, flag=wx.RIGHT, border=8)
        vbox.Add(hbox21, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        hbox22 = wx.BoxSizer(wx.HORIZONTAL)
        wildcard = "TXT and CSV files (*.txt; *.csv)|*.txt; *.csv"
        tc2 = wx.FilePickerCtrl(panel, message="Select file", wildcard=wildcard, style=wx.FLP_USE_TEXTCTRL, size=(390, 25))
        hbox22.Add(tc2, proportion=1)
        vbox.Add(hbox22, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        vbox.Add((-1, 10))

        hbox31 = wx.BoxSizer(wx.HORIZONTAL)
        st_class = wx.StaticText(panel, label='How many classes:')
        st_class.SetFont(font)
        hbox31.Add(st_class, flag=wx.RIGHT, border=8)
        vbox.Add(hbox31, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        cb2 = wx.CheckBox(panel, label='2 class')
        cb2.SetFont(font)
        hbox3.Add(cb2, flag=wx.LEFT, border=10)
        cb3 = wx.CheckBox(panel, label='3 class')
        cb3.SetFont(font)
        hbox3.Add(cb3, flag=wx.LEFT, border=10)
        vbox.Add(hbox3, flag=wx.LEFT, border=10)

        vbox.Add((-1, 25))

        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        st3 = wx.StaticText(panel, label='Visualisation: ')
        st3.SetFont(font)
        hbox4.Add(st3, flag=wx.RIGHT, border=8)
        vbox.Add(hbox4, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        tc2 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        hbox5.Add(tc2, proportion=1, flag=wx.EXPAND)
        vbox.Add(hbox5, proportion=1, flag=wx.LEFT | wx.RIGHT | wx.EXPAND, border=10)

        vbox.Add((-1, 25))


        hbox6 = wx.BoxSizer(wx.HORIZONTAL)
        btn1 = wx.Button(panel, label='VISUALIZE', size=(90, 30))
        hbox6.Add(btn1)
        vbox.Add(hbox6, flag=wx.ALIGN_RIGHT | wx.RIGHT, border=10)

        panel.SetSizer(vbox)



def main():

    app = wx.App()
    ex = Visualisation(None, title='visualize')
    ex.Show()
    app.MainLoop()
    print("fff", Visualisation.patch, "vvvv")


if __name__ == '__main__':
    main()