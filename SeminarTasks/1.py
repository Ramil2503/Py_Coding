array_1 = []
array_2 = []
res_array = []

n = int(input("the number of elements in the first array: "))

input_array_1 = input("Enter array separated by space: ").split()

array_1 = list(map(int, input_array_1))

m = int(input("the number of elements in the second array: "))

input_array_2 = input("Enter array separated by space: ").split()

array_2 = list(map(int, input_array_2))

array_1.sort()
array_2.sort()
print(f'array 1:\n{array_1}')
print(f'array 2:\n{array_2}')

for i in range(n):
    found = False  # flag to check if the element is found in array_2
    for j in range(m):
        if array_1[i] == array_2[j]:
            found = True
            break
    if not found:
        res_array.append(array_1[i])

print(f'values which are in the first array but not in the second array:\n{res_array}')
