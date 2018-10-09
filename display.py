import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from bspline import BSpline

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


def __get_x_y_z(points):
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    z = [p[2] for p in points]

    return x, y, z


def __display_3d(points, spline):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x, y, z = __get_x_y_z(points)

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
    n = splines[0].n
    k = splines[0].k

    for spline in splines:
        if spline.n != n or spline.k != k:
            raise ValueError('Dimensions of B-Splines do not match')

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    points = [__get_x_y_z(spline.compute_range(step)) for spline in splines]

    # Plot regular splines
    for spline_points in points:
        ax.plot(spline_points[0], spline_points[1], spline_points[2], 'r-')

    # Plot "normal" splines
    N = len(points[0][0])  # Number of points

    controls = [[(p[0][i], p[1][i], p[2][i]) for p in points] for i in range(N)]

    norm_splines = [BSpline(control, k) for control in controls]

    for spline in norm_splines:
        spline.close()
        x, y, z = __get_x_y_z(spline.compute_range(step))
        ax.plot(x, y, z, 'r-')

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
