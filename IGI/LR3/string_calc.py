def string_calc() -> int:
    user_input = input("Enter a string: ")
    lowercase_characters_count = 0
    numbers_characters_count = 0
    for char in user_input:
        if ord(char) in range(ord('a'),ord('z')):
            lowercase_characters_count += 1
        if ord(char) in range(ord('0'),ord('9')):
            numbers_characters_count += 1
    print(f"Count of lowercase latin characters: {lowercase_characters_count}")
    print(f"Count of numerical characters: {numbers_characters_count}")