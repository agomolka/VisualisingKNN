import pandas as pd
import webview
import plotly.express as px

class Visualisation3d:
    data = ""
    i = 1
    """
    Visualisation by plotly k-nn algorithm
    for three variables
    in new HTML interavtive window
    """
    def __init__(self, data, k):
        self.data = data
        self.k = k
        self.show_plot()

    def show_plot(self):
        data_columns_values_list = self.data.columns.values.tolist()
        a = data_columns_values_list[0]
        b = data_columns_values_list[1]
        c = data_columns_values_list[2]
        d = data_columns_values_list[3]
        f = data_columns_values_list[len(data_columns_values_list)-1]

        fig = px.scatter_3d(self.data, x=b, y=c, z=d, color=f)
        name = f'knn, k=' + str(self.k)
        webview.create_window(name, html=fig.to_html())

def main(data, k_array):
    data2 = pd.read_csv(data)
    for i in k_array:
        Visualisation3d(data2, i)
    webview.start()

if __name__ == '__main__':
    main()