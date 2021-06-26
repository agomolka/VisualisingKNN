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

        mesh_size = .02
        margin = 0.25
        data_columns_values_list = self.data_train.columns.values.tolist()
        X = self.data_train.iloc[:, [0,1,2,3]].values
        y = self.data_train.iloc[:, [len(data_columns_values_list)-1]].values.ravel()
        # Load and split data
        X_train = self.data_train.iloc[:, :-1].values
        X_test = self.data_test.iloc[:, :-1].values
        y_train_float = self.data_train.iloc[:, -1:].values
        y_test_float = self.data_test.iloc[:, -1:].values

        a = data_columns_values_list[0]  # id
        b = data_columns_values_list[1]  # SepalLengthCm
        c = data_columns_values_list[2]  # SepalWidthCm
        d = data_columns_values_list[3]  # PetalLengthCm
        f = data_columns_values_list[len(data_columns_values_list)-1]  # Species

        if type(y_train_float[1, 0]) != str:
            a = y_train_float.astype(int)
            y_train = a.astype('str').ravel()
            b = y_test_float.astype(int)
            y_test = b.astype('str').ravel()
        else:
            y_train = y_train_float.ravel()
            y_test = y_test_float.ravel()

        # Create a mesh grid on which we will run our model
        x_min, x_max = X[:, 0].min() - margin, X[:, 0].max() + margin
        y_min, y_max = X[:, 1].min() - margin, X[:, 1].max() + margin
        xrange = np.arange(x_min, x_max, mesh_size)
        yrange = np.arange(y_min, y_max, mesh_size)
        xx, yy = np.meshgrid(xrange, yrange)

        # # Create classifier, run predictions on grid
        clf = KNeighborsClassifier(self.k, weights='uniform')
        clf.fit(X_train, y_train)
        pred = clf.predict_proba(X_test)

        # Generate the plot
        fig = px.scatter_3d(self.data_train, x=b, y=c, z=d, color=f)

        unique_target_value = self.data_train[f].unique()

        trace_specs = [
            [X_train, y_train, unique_target_value[0], 'Train', 'cross'],
            [X_train, y_train, unique_target_value[1], 'Train', 'diamond'],
            [X_train, y_train, unique_target_value[2], 'Train', 'circle'],
            [X_test, y_test, unique_target_value[0], 'Test', 'cross'],
            [X_test, y_test, unique_target_value[1], 'Test', 'diamond'],
            [X_test, y_test, unique_target_value[2], 'Test', 'circle']
        ]

        fig = go.Figure(data=[
            go.Scatter3d(
                x=X[y == label, 1],
                y=X[y == label, 2],
                z=X[y == label, 3],
                name=f'{split} Split, Label {label}',
                mode='markers',
                marker_symbol=marker
            )
            for X, y, label, split, marker in trace_specs
        ])
        fig.update_layout(scene=dict(
            xaxis_title=b,
            yaxis_title=c,
            zaxis_title=d),
            width=700,
            # margin=dict(r=20, b=10, l=10, t=10)
        )

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
