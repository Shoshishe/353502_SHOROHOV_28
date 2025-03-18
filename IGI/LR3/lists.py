def print_list(list : list[float]):
        for (index, item) in enumerate(list):
            print(f"List item {index + 1} " + str(item))
            
def check_if_float(item: str) -> tuple[float, bool]:
        try:
           item = float(item)
           return (item, True)
        except ValueError:
            return (0.0 ,False)
        
def enter_list() -> list[float]:
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
        
def solve_task_5(floats_list: list[float]):               
        max = 0
        last_positive_index = 0
        for index, item in enumerate(floats_list):
            if abs(item) > max:
                max = item
            if item > 0:
                last_positive_index = index 
        sum = 0        
        for item in floats_list[:last_positive_index + 1]:
            sum += item
        print(f"Sum of elements until last positive: {sum}")
        print(f"Largest element by absolute value: {max}")