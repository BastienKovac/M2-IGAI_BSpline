from bspline import BSpline
from display import display


if __name__ == "__main__":
    # 2d
    b = BSpline([[2, 5], [3, 4], [5, 7], [1, 2], [1, 8], [7, 5]])
    display(b)

    # 3d
    b = BSpline([[2, 5, 5], [3, 4, 3], [5, 7, 4], [1, 2, 2], [1, 8, 3], [7, 5, 2]])
    display(b)
