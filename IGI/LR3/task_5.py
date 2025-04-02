def print_solver_list(solution_func):
    """
    Function for print out list of arguments in a solution function
     Parameters: solution_func (function which accepts a list of floats)
     Returns: Function which prints out elements before calling the solution function 
     Exceptions: -
    """
    def print_list(*args):
        for (index, item) in enumerate(args[0]):
            print(f"List item {index + 1} " + str(item))
        solution_func(*args)    
    return print_list        
            
def check_if_float(item: str) -> tuple[float, bool]:
        """
        Function for print out list of arguments in a solution function
         Parameters: solution_func (function which accepts a list of floats)
         Returns: Function which prints out elements before calling the solution function 
         Exceptions: -
        """
        try:
           item = float(item)
           return (item, True)
        except ValueError:
            return (0.0 ,False)
        
def enter_list() -> list[float]:
        """
        Function for entering a list of floats from stdin, of a given size
         Parameters: -
         Returns: entered list
         Exceptions: -
        """
        user_input = ''
        while user_input is not int:
            try:
                user_input = int(input('Enter the list size: '))
                break
            except ValueError:
             print('Please enter a valid integer value: ')
        floats_list = []
        for i in range(user_input):
         while user_input is not float:
            user_input = input('Enter the list element: ')
            value, ok = check_if_float(user_input)
            if not ok:
                print('Please enter a valid float value: ') 
                continue
            floats_list.append(value) 
            break
        return floats_list
    
@print_solver_list        
def solve_task_5(floats_list: list[float])->tuple[int,int]:         
        max = 0
        last_positive_index = 0
        for index, item in enumerate(floats_list):
            if abs(item) > max:
                max = item
            if item > 0:
                last_positive_index = index 
        sum = 0        
        for item in floats_list[:last_positive_index]:
            sum += item    
        print(f"Sum of elements until last positive: {sum}")
        print(f"Largest element by absolute value: {max}")