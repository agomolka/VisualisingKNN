import plotly.graph_objects as go
import numpy as np
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import webview
import plotly.express as px


class KnnVisualisation2dWithTestSet:

    def __init__(self, data, data_test, k):
        self.data_train = data
        self.data_test = data_test
        self.k = k

    def visualisation(self):
        # fig.show()
        # mesh_size = .02
        # margin = 0.25
        #
        # X = self.data_train[["X", "Y"]].values
        # y = self.data_train["class"].astype(int).values
        # # Load and split data
        # X_train = self.data_train.iloc[:, :-1].values
        # X_test = self.data_test.iloc[:, :-1].values
        # y_train_float = self.data_train.iloc[:, -1:].values
        # y_test_float = self.data_test.iloc[:, -1:].values
        #
        # a = y_train_float.astype(int)
        # y_train = a.astype('str').ravel()
        #
        # b = y_test_float.astype(int)
        # y_test = b.astype('str').ravel()
        #
        # # Create a mesh grid on which we will run our model
        # x_min, x_max = X[:, 0].min() - margin, X[:, 0].max() + margin
        # y_min, y_max = X[:, 1].min() - margin, X[:, 1].max() + margin
        # xrange = np.arange(x_min, x_max, mesh_size)
        # yrange = np.arange(y_min, y_max, mesh_size)
        # xx, yy = np.meshgrid(xrange, yrange)
        #
        # # Create classifier, run predictions on grid
        # clf = KNeighborsClassifier(self.k, weights='uniform')
        # clf.fit(X_train, y_train)
        # Z = clf.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1]
        # Z = Z.reshape(xx.shape)
        #
        # trace_specs = [
        #     [X_train, y_train, '0', 'Train', 'square'],
        #     [X_train, y_train, '1', 'Train', 'circle'],
        #     [X_test, y_test, '0', 'Test', 'square-dot'],
        #     [X_test, y_test, '1', 'Test', 'circle-dot']
        # ]
        #
        # fig = go.Figure(data=[
        #     go.Scatter(
        #         x=X[y == label, 0], y=X[y == label, 1],
        #         name=f'{split} Split, Label {label}',
        #         mode='markers', marker_symbol=marker
        #     )
        #     for X, y, label, split, marker in trace_specs
        # ])
        # fig.update_traces(
        #     marker_size=12,
        #     marker_line_width=1.5,
        #     # marker_color="lightyellow"
        # )
        #
        # fig.add_trace(
        #     go.Contour(
        #         x=xrange,
        #         y=yrange,
        #         z=Z,
        #         showscale=False,
        #         colorscale='RdBu',
        #         opacity=0.8,
        #         name='Score',
        #         hoverinfo='skip'
        #     )
        # )
        data_columns_values_list = self.data_train.columns.values.tolist()
        a = data_columns_values_list[0]
        b = data_columns_values_list[1]
        c = data_columns_values_list[2]
        d = data_columns_values_list[3]

        fig = px.scatter_3d(self.data_train, x=a, y=b, z=c, color=d)

        name = f'knn, k=' + str(self.k)
        webview.create_window(name, html=fig.to_html())


def main(k_array, data, data_test):
    data_train = pd.read_csv(data)
    data_test = pd.read_csv(data_test)
    for i in k_array:
        KnnVisualisation2dWithTestSet(data_train, data_test, i).visualisation()

    webview.start()


if __name__ == '__main__':
    main()
