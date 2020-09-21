#Create a function that takes a string txt and censors any word from a given list lst.
#The text removed must be replaced by the given character char.

def censor_string(txt, lst, char):
    for word in lst:
        txt = txt.replace(word, char*len(word))
    return txt

print(censor_string("Salut à tous",["a", "t"], "-"))
        