import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


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

    plt.show()


def display(spline, step=0.01):
    points = spline.compute_range(step)

    if len(points) > 0:
        if len(points[0]) == 2:
            __display_2d(points, spline)
        elif len(points[0]) == 3:
            __display_3d(points, spline)
        else:
            print("Impossible to display this dimension: \n{}".format(points))
