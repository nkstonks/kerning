import split

def kern(phrase):

    list_of_letters = []

    for letter in split(phrase):
        list_of_letters.append(letter)
    
    # print(list_of_letters)
    try:
        new_phrase = ' '.join(list_of_letters)
    except TypeError:
        raise TypeError("Expected string, got something else.")

    # print(new_phrase)
    return new_phrase