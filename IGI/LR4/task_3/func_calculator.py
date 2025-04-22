import math
import matplotlib.pyplot as plt


class FunctionCalculator:
    def __init__(self, x: float, eps: float):
        self.__x = x
        self.__eps = eps

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x

    @property
    def eps(self) -> float:
        return self.__eps

    @eps.setter
    def eps(self, eps: float):
        self.__eps = eps
        self.recalc_func()

    def recalc_func(self) -> float:
        sum = 0
        cur_diff = 1.1
        i = 1
        while abs(cur_diff) > self.__eps:
            cur_diff = self.__x**i * (-1)**(i + 1) / i
            sum += cur_diff
            i = i + 1
        return sum

    def median(self, seq: list[int]) -> float:
        return seq.sort()[len(seq) / 2]

    def arithmetic_mean(self, seq: list[int]):
        sum = 0
        for func in seq:
            sum += func
        return sum // len(seq)

    def mode(self, seq: list[int]) -> float:
        max_count = 0
        max_appearing = 0.0
        for func in seq:
            if seq.count(func) > max_count:
                max_count = seq.count(func)
                max_appearing = func
        return max_appearing

    def disperse(self, seq: list[int]) -> int:
        return max(seq) - min(seq)

    def __get_prec(self) -> int:
        cur_diff = 1.1
        i = 1
        while abs(cur_diff) > self.__eps:
            cur_diff = self.__x**i * (-1)**(i + 1) / i
            i = i + 1
        return i

    def plot_graphs(self):
        count_of_points = 7
        values = []
        true_values = []
        n_arr = []
        self.__x = 0
        for _ in range(count_of_points):
            value = self.recalc_func()
            true_value = math.log(1+self.__x, math.e)
            values.append(value)
            true_values.append(true_value)
            n_arr.append(self.__get_prec())
            self.__x += 1/count_of_points
        fig, ax = plt.subplots()
        ax.tick_params(
            axis='x',
            top=True,
            labeltop=True,
            bottom=False,
            labelbottom=False
        )
        ax.set_xlabel('x axis')
        ax.xaxis.set_label_position('top')
        ax.set_ylabel('y axis')
        ax.plot(true_values, label="real function")
        ax.plot(values, label="series")
        ax.annotate(r"Начальная точка", xy=(0, 0), xytext=(0, 0.1),
                    arrowprops=dict(facecolor='black', shrink=0.05))
        ax.legend()
        columns = ["x", "n", "F(x)", "Math F(x)", "eps"]
        cell_text = []
        for i in range(0, len(values)):
            cell_text.append(['{:.3f}'.format(i/count_of_points), '{:d}'.format(
                n_arr[i]-1), '{:.3f}'.format(values[i]), '{:.3f}'.format(true_values[i]), self.__eps])
        plt.table(colLabels=columns, cellText=cell_text, loc='bottom')
        fig.set_figheight(7.5)
        fig.subplots_adjust(left=0.2, bottom=0.35)
        plt.savefig(
            "/home/shosh/BSUIR projects/SCI/353502_SHOROHOV_28/IGI/LR4/txt_sources/out/plots.png")
        plt.show()


def solve_task_3():
    user_input = ''
    while user_input is not float:
        try:
            user_input = float(input("Enter the required precision: "))
            if user_input > 1 or user_input < 0:
                raise ValueError
            break
        except ValueError:
            print("Enter the valid float value")
    calc = FunctionCalculator(0.5, user_input)
    calc.plot_graphs()


def main():
    solve_task_3()


if __name__ == "__main__":
    main()
