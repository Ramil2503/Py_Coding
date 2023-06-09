import random

def find_indices(arr, minimum, maximum):
    indices = []
    for i in range(len(arr)):
        if minimum <= arr[i] <= maximum:
            indices.append(i)
    return indices

array_length = int(input("Enter the length of the array: "))
array = [random.randint(1, 100) for _ in range(array_length)]

print(array)

min_value = int(input("Enter the minimum value: "))
max_value = int(input("Enter the maximum value: "))

result = find_indices(array, min_value, max_value)
print("Indices of elements within the specified range:")
print(result)
