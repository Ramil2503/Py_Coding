# User input
a1 = int(input("Enter the first element of the progression: "))
d = int(input("Enter the difference of the progression: "))
n = int(input("Enter the number of elements: "))

# Creating and populating the array
progression = []
for i in range(n):
    element = a1 + i * d
    progression.append(element)

# Outputting the array
print("Array of arithmetic progression elements:")
for element in progression:
    print(element)
