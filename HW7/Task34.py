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
