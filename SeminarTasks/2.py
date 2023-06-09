import random

array = []
for i in range(5):
    array.append(random.randint(1, 10))

print(array)

def function(array):
    for i in range(len(array)):
        if (array[i - 1] < array[i] and array[i + 1] < array[i]):
            return array[i]

print(function(array))
