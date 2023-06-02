import random

n = int(input("the number of elements in the first array: "))
m = int(input("the number of elements in the second array: "))

array_1 = []
array_2 = []
res_array = []

for i in range(n):
    array_1.append(random.randint(-99, 99))
for i in range(m):
    array_2.append(random.randint(-99, 99))

array_1.sort()
array_2.sort()
print(f'array 1:\n{array_1}')
print(f'array 2:\n{array_2}')

for i in range(n):
    for j in range(m):
        if (array_1[i] == array_2[j]):
            res_array.append(array_1[i])

unique_array = list(set(res_array))
print(f'values which can be found in both arrays:\n{unique_array}')
