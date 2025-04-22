import abc
import math
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.path import Path
from matplotlib.patches import PathPatch
from abc import ABC


class Shape(ABC):
    def __init__(self):
        print("Initializing object derived from shape")

    @abc.abstractmethod
    def square(self) -> float:
        pass
    pass


class Color:
    def __init__(self, color: str):
        self.__color = "black"
        if (color not in mcolors.CSS4_COLORS):
            raise ValueError(
                "Color name doesn't follow css4 naming conventions")
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    # Just for fun, rly
    @color.deleter
    def color(self):
        self.__color = ""


class Pentagon(Shape):
    __figure_name = "Pentagon"

    @classmethod
    def info(cls):
        print(f"The figure name is {cls.__figure_name}")

    def __init__(self, side: float, color: str):
        super().__init__()
        self.__side = side
        try:
            self.__color = Color(color)
        except ValueError:
            print("Invalid color name. Must follow css4 naming convention")
            self.__color = Color("black")

    @property
    def side(self) -> float:
        return self.__side

    @property
    def color(self) -> Color:
        return self.__color

    def square(self) -> float:
        return self.__side ** 2 / 4 * math.sqrt(25 + 10*math.sqrt(5))

    def get_params(self):
        return "The figure color: {%s},\n The figure square: {:.3f}".format(self.__color.color, self.square())


def input_info() -> tuple[Pentagon, str]:
    usr_input = ''
    length = 0.0
    while usr_input is not float:
        usr_input = input("Enter the length of one side of a pentagon: ")
        try:
            usr_input = float(usr_input)
            length = usr_input
            if usr_input > 100:
                length = 2
                print("The side value is too large, try from 1 to 100")
            if usr_input < 1:
                length = 2
                print("The side value is too small, try from 1 to 100")
            break
        except ValueError:
            print("The length must be a valid number")
    color = None
    while color is not Color:
        usr_input = input("Enter the color of a pentagon ")
        try:
            color = Color(usr_input)
            break
        except ValueError as err:
            print(err)
    penta = Pentagon(length, color=color.color)
    usr_input = input("Enter text to subscribe your painting with ")
    return (penta, usr_input)


def display_penta(penta: Pentagon, text: str):
    fig = plt.figure()
    ax = fig.add_subplot(111, aspect='equal')
    side = penta.side
    outer_angle = math.pi / 180 * 72
    points = [
        (Path.MOVETO, (0, 0)),
        (Path.LINETO, (side, 0)),
        (Path.LINETO, (side + side * math.cos(outer_angle), side*math.sin(outer_angle))),
        (Path.LINETO, (side/2, side*math.sin(outer_angle) + side*math.sin(outer_angle / 2))),
        (Path.LINETO, (0-side*math.cos(outer_angle), side*math.sin(outer_angle))),
        (Path.LINETO, (0, 0))
    ]
    codes, verts = zip(*points)
    path = Path(verts, codes)
    patch = PathPatch(path)
    ax.add_patch(patch)

    x, y = zip(*path.vertices)
    _ = ax.plot(x, y, color=penta.color.color)
    ax.fill_between(x, y, facecolor=penta.color.color)
    ax.text(side/2, side, text, bbox=dict(facecolor='red', alpha=0.5))
    ax.grid()
    ax.axis('equal')
    plt.show()


def solve_task_4():
    a = input_info()
    print("Figure square is: " + str(a[0].square()))
    display_penta(*a)


def main():
    solve_task_4()


if __name__ == "__main__":
    main()
