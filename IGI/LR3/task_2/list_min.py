from task_2.list_initialization import init_by_input, init_by_generator
def print_minimum_and_sum(func):
  """
  Function for decorating output of a find_minimum_and_sum_in_range function
     Parameters:
      func
           function which return a tuple of minimal value and sum of all values in range
     Returns: -
     Exceptions: -
  """
  def inner():  
    result_tuple = func()
    print(f"Minimal integer value: {result_tuple[1]}")
    print(f"Sum of all elements in a range: {result_tuple[0]}")
  return inner 

@print_minimum_and_sum
def find_minimum_and_sum_in_range() -> tuple[int,int]:
    """
    Function for getting minimum value and sum in range
     Parameters: -
     Returns: -
     Exceptions: -
    """
    min = 2 ** 63 - 1
    sum = 0
    input_type = ''
    while input_type is not int:
        try:
          input_type = int(input('Enter an input type (1 - custom input, 2 - via generator (i**2) until the given num ) '))
          if input_type != 1 and input_type != 2:
            raise ValueError
          break
        except ValueError:
         print('Please enter a valid integer value: ')
    range_list = []
    if input_type == 1:
      range_list = init_by_input(range_list)
    if input_type == 2:
      init_by_generator(range_list)
    for i in range_list:
      sum += i
      if i < min:
        min = i
    return (sum,min)