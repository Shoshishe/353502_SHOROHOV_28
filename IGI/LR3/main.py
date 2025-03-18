from task_2.list_min import find_minimum_and_sum_in_range
from series import series
from string_calc import string_calc
from string_parser import parse_string
from lists import enter_list, solve_task_5, print_list

    
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
        series()     
    if task_num == 2:            
        find_minimum_and_sum_in_range()
    if task_num == 3:
        string_calc()
    if task_num == 4:
        parse_string()
    if task_num == 5:
        floats_list = enter_list()
        solve_task_5(floats_list=floats_list)
        print_list(floats_list)
        
