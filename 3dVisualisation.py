import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


class Visualisation3d():
    data = ""
    i = 1

    def __init__(self, data, i):
        self.data = data
        self.i = i

    def show_plot(self):

        feature_columns = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
        X = self.data[feature_columns].values
        y = self.data['Species'].values
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

        le = LabelEncoder()
        y = le.fit_transform(y)
        fig = plt.figure(1, figsize=(20, 15))
        ax = Axes3D(fig, elev=48, azim=134)
        ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y,
                   cmap=plt.cm.Set1, edgecolor='k', s=X[:, 3] * 50)

        for name, label in [('Virginica', 0), ('Setosa', 1), ('Versicolour', 2)]:
            ax.text3D(X[y == label, 0].mean(),
                      X[y == label, 1].mean(),
                      X[y == label, 2].mean(), name,
                      horizontalalignment='center',
                      bbox=dict(alpha=.5, edgecolor='w', facecolor='w'), size=25)

        ax.set_title("3D visualization", fontsize=40)
        ax.set_xlabel("Sepal Length [cm]", fontsize=25)
        ax.w_xaxis.set_ticklabels([])
        ax.set_ylabel("Sepal Width [cm]", fontsize=25)
        ax.w_yaxis.set_ticklabels([])
        ax.set_zlabel("Petal Length [cm]", fontsize=25)
        ax.w_zaxis.set_ticklabels([])

        plt.show()


def main():
    data = pd.read_csv("archive/Iris.csv")
    window = Visualisation3d(data, i)
    window.show_plot()

if __name__ == '__main__':
    main()