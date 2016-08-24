#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from sklearn.cluster import KMeans
from sklearn.preprocessing import scale

import pandas as pd

DATA_FOLDER = 'data'

def main():
    """ Apply KMeans with different parameters of "K" and plotting data in 3D.

    """

    # reading data
    file_name = os.path.join(DATA_FOLDER, 'original-00_Uebung_Cluster_Normalisiert_Erste_Iteration.csv')
    df = pd.read_csv(file_name, sep=';', header=None)

    df_X = df[[1, 2, 3, 4]] # taking only
    df_X_np = df_X.as_matrix()
    df_X_np_scale = scale(df_X_np)

    X = df_X_np_scale


    estimators = {'k_means_iris_3': KMeans(n_clusters=3),
                  'k_means_iris_4': KMeans(n_clusters=4),
                  'k_means_iris_5': KMeans(n_clusters=5)
                  # ,'k_means_iris_bad_init': KMeans(n_clusters=3, n_init=1,
                  #                                 init='random')
                }


    colors = ['b', 'g', 'r', 'y', 'k']

    fignum = 1
    for name, est in estimators.items():
        fig = plt.figure(fignum, figsize=(4, 3))
        plt.clf()
        ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

        plt.cla()
        est.fit(X)
        labels = est.labels_

        colors_index = []

        for lb in labels.astype(np.float):
            colors_index.append(colors[int(lb)])

        ax.scatter(X[:, 0], X[:, 1], X[:, 3], c=colors_index)

        ax.w_xaxis.set_ticklabels([])
        ax.w_yaxis.set_ticklabels([])
        ax.w_zaxis.set_ticklabels([])
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')

        fignum = fignum + 1

    plt.show()

if __name__ == '__main__':

    main()
