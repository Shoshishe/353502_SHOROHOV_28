def string_calc():
    """
    Function for printing out count of lowercase characters and count of numerical characters in a string from stdin
     Parameters: -
     Returns: -
     Exceptions: -
    """
    user_input = input("Enter a string: ")
    lowercase_characters_count = 0
    numbers_characters_count = 0
    for char in user_input:
        if char.islower():
            lowercase_characters_count += 1
        if ord(char) in range(ord('0'),ord('9')):
            numbers_characters_count += 1
    print(f"Count of lowercase latin characters: {lowercase_characters_count}")
    print(f"Count of numerical characters: {numbers_characters_count}")