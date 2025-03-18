def parse_string():
    text = "So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy and stupid, whether the pleasure of making a daisy-chain would" 
    "be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her."
    words = text.replace(",","").split(" ")
    count_of_words = len(words)
    non_unique_words = set()
    for word in words:
        smallest_match_length = 2 >> 63 - 1
        smallest_word = "None";
        if len(word) % 2 == 1: 
            print(word)
        if word.startswith('i'):
            if len(word) < smallest_match_length:
                smallest_match_length = len(word)
                smallest_word = word     
        if words.count(word) > 1:
            non_unique_words.add(word)      
    print("Smallest word that starts with i: " + smallest_word)    
    print(f"Count of words in a string: {count_of_words}")    
    print("Non unique words: ")
    for word in non_unique_words:
        print(word)