def print_upper_words(list, must_start_with):
    """Given a list of words, print out each word on a separate line. 
    Each word should be uppercased. 
    With the second argument, the function will only accept words that begin 
    with a specified letter or set of letters.
    """
    for word in list:
        if word.startswith(must_start_with):
            uppercased = word.upper()
            print(uppercased)


print_upper_words(list=['scarlett', 'sun', 'ludwig'], must_start_with="sc")
