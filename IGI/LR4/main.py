from task_5.matrix_operator import solve_task_5
from task_4.shape import solve_task_4
from task_3.func_calculator import solve_task_3
from task_2.text_analyzer import solve_task_2
from task_1.serializer import solve_task_1

user_input = ""
while user_input != 0:
    while user_input is not int:
        try:
            user_input = int(
                input("Enter the task number from 1 to 5. Enter 0 to exit the program "))
            if user_input < 0 or user_input > 5:
                raise ValueError
        except ValueError:
            print("Enter the correct task number")
        if user_input == 1:
            solve_task_1()
        if user_input == 2:
            solve_task_2()
        if user_input == 3:
            solve_task_3()
        if user_input == 4:
            solve_task_4()
        if user_input == 5:
            solve_task_5()
        break

