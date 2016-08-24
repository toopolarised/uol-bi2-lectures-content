# coding: utf-8
#!/usr/bin/env python

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

DATA_FOLDER = 'data'

def plot_clusters(ds, indexes, clusters):
    """ Plot given clusters.

    Arguments:
        ds {dict} -- DataFrame of pandas with data
        indexes {list} -- indexes to be processed
        clusters {list} -- list of clusters
    """

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    colors = ['b', 'g', 'r', 'y', 'b']

    for row in ds.iterrows():
        color_index = int(row[1][len(row[1])-1])
        ax.scatter(row[1][indexes[0]], row[1][indexes[1]], row[1][indexes[2]], c=colors[color_index])

    ax.set_xlabel('Label Index {0}'.format(str(indexes[0])))
    ax.set_ylabel('Label Index {0}'.format(str(indexes[1])))
    ax.set_zlabel('Label Index {0}'.format(str(indexes[2])))

    plt.show()

def main(file_name=None):


    #file_name = os.path.join(DATA_FOLDER,'00_Uebung_Cluster_Normalisiert_Erste_Iteration.csv')
    file_name = os.path.join(DATA_FOLDER, 'student_00_Uebung_Cluster_Normalisiert_Erste_Iteration.csv')

    df = pd.read_csv(file_name, sep=';', header=None)
    clusters = df[4].unique()

    plot_clusters(df, [0,1,2], clusters)
    #plot_clusters(df, [0,1,3], clusters)
    #plot_clusters(df, [1,2,3], clusters)

if __name__ == '__main__':
    main()
