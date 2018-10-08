import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np


def __display_2d(points, spline):
    fig, ax = plt.subplots()

    x = [p[0] for p in points]
    y = [p[1] for p in points]
    ax.plot(x, y, 'r-')

    x = [p[0] for p in spline.controls]
    y = [p[1] for p in spline.controls]
    ax.scatter(x, y, marker=u'+')

    for i, p in enumerate(spline.controls):
        text = "P{} ({}, {})".format(i, p[0], p[1])
        ax.annotate(text, p, xytext=(6, - 12), textcoords='offset points')

    ax.set_xlim((ax.get_xlim()[0] - 1, ax.get_xlim()[1] + 1))
    ax.set_ylim((ax.get_ylim()[0] - 1, ax.get_ylim()[1] + 1))

    plt.show()


def __display_3d(points, spline):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = [p[0] for p in points]
    y = [p[1] for p in points]
    z = [p[2] for p in points]
    ax.plot(x, y, z, 'r-')

    x = [p[0] for p in spline.controls]
    y = [p[1] for p in spline.controls]
    z = [p[2] for p in spline.controls]

    ax.scatter(x, y, z, marker=u'+')
    for i, p in enumerate(spline.controls):
        text = "P{} ({}, {}, {})".format(i, p[0], p[1], p[2])
        ax.text(p[0], p[1], p[2], text, 'x')

    ax.set_xlabel('$X$')
    ax.set_ylabel('$Y$')
    ax.set_zlabel('$Z$')

    plt.show()


def __display_tensor(splines, step=0.01):
    all_splines = [spline.compute_range() for spline in splines]
    if not all(len(spline) == len(all_splines[0]) for spline in all_splines):
        raise ValueError("All B-Spline must have the same number of points")

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    X, Y, Z = [], [], []
    for spline in all_splines:
        X.append([p[0] for p in spline])
        Y.append([p[1] for p in spline])
        Z.append([p[2] for p in spline])

    X = np.array(X)
    Y = np.array(Y)
    Z = np.array(Z)

    ax.plot_surface(X, Y, Z)

    ax.set_xlabel('$X$')
    ax.set_ylabel('$Y$')
    ax.set_zlabel('$Z$')

    plt.show()


def display(spline, step=0.01):
    if isinstance(spline, list):
        __display_tensor(spline, step)
    else:
        points = spline.compute_range(step)

        if len(points) > 0:
            if len(points[0]) == 2:
                __display_2d(points, spline)
            elif len(points[0]) == 3:
                __display_3d(points, spline)
            else:
                print("Impossible to display this dimension: \n{}".format(points))
