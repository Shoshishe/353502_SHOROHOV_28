def init_by_input(list: list[int]) -> list[int]:
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
    return list         
            
def init_by_generator(list: list[int]) -> list[int]:
    count_of_elems = ''
    while count_of_elems is not int:
        try:
            count_of_elems = int(input('Enter the range size: '))
            break
        except ValueError:
            print("Enter a valid integer") 
    list = [i**2 for i in range(count_of_elems)]     
    return list           
            