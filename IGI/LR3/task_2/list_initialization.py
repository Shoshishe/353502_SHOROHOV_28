def init_by_input(list: list[int]):
    """
    Function for inputting into an integer list via stdin, where user defines both range and values
     Parameters
      list:  list[int]
           list where integer values will reside
     Returns: -
     Exceptions: -
    """
    user_input = ''
    while True:
      while user_input is not int:
        try:
            user_input = int(input('Enter the range element: '))
            break
        except ValueError:
            print("Enter a valid integer") 
      if user_input == 1:
          break  
      list.append(user_input)        
            
def init_by_generator(list: list[int]) -> list[int]:
    """
    Function for inputting into an integer list via generator , where user defines list range by stdin
     Parameters
      list:  list[int]
           list where integer values will reside
     Returns: -
     Exceptions: -
    """
    count_of_elems = ''
    while count_of_elems is not int:
        try:
            count_of_elems = int(input('Enter the range size: '))
            break
        except ValueError:
            print("Enter a valid integer") 
    #list_generator = (i**2 for i in range(count_of_elems))
    def gen_func(count_of_elems: int):
        for i in range(count_of_elems):
            yield(i**2)
    for elem in gen_func(count_of_elems):
        list.append(elem)                    