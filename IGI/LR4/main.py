def get_task_num() -> int:
    user_input = ""
    while user_input is not int:
        try:
          user_input = int(input("Enter the task number from 1 to 5. Enter 0 to exit the program"))
          if user_input < 0 or user_input > 5:
              raise ValueError
        except ValueError:
            print("Enter the correct task number")       
    return 