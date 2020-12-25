def split(word): 
    return [char for char in word]

def kern(phrase):

    list_of_letters = []

    for letter in split(phrase):
        list_of_letters.append(letter)
    
    # print(list_of_letters)
    try:
        new_phrase = ' '.join(list_of_letters)
    except TypeError:


    # print(new_phrase)
    return new_phrase