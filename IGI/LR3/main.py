from task_2.list_min import find_minimum_and_sum_in_range
from task_1 import series
from task_3 import string_calc
from task_4 import parse_string
from task_5 import enter_list, solve_task_5


task_num = ''
while task_num != 0:
    while task_num is not int:
        try: 
            task_num = int(input("Enter the number of task (1-5) to solve. Print 0 to exit: "))
            if not (0 <= task_num and task_num <= 5):
                raise ValueError
            break
        except ValueError:
            print("Enter a valid number")    
    if task_num == 1:
        try:
          series()
        except TimeoutError:
            print("Time limit exceeded")     
    if task_num == 2:            
        find_minimum_and_sum_in_range()
    if task_num == 3:
        string_calc()
    if task_num == 4:
        parse_string()
    if task_num == 5:
        floats_list = enter_list()
        solve_task_5(floats_list)
        
