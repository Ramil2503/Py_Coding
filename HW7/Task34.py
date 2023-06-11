# Winnie the Pooh asked you to see if there is a rhythm in his poems. 
# Since his chants are not as easy to understand as he makes them easy to understand, 
# you should write a program. Winnie the Pooh believes that there is a rhythm 
# if the number of syllables (i.e. the number of vowels) in each phrase of the poem is the same. 
# A phrase can consist of one word, if there are several words in the phrase, then they are separated by hyphens. 
# Phrases are separated from each other by spaces. Poem Winnie the Pooh drives into the program from the keyboard. 
# In response, write “Param pam-pam” if the rhythm is okay and “Pam param” if the rhythm is not okay.

def check_rythm(poem):
    arr = []
    words = poem.split(" ")
    for word in words:
        number_of_vowels = word.count("а")
        arr.append(number_of_vowels)
    if (all(element == arr[0] for element in arr) == True):
        return "Парам пам-пам"
    else:
        return "Пам парам"
    

poem = input("Enter the string: ")

print(check_rythm(poem))
