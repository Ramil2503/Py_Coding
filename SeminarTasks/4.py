import random

print(type_list := [(random.randint(1, 4), random.randint(1, 4)) for i in range(10)])

type_list = list(filter(lambda x: x[0] != x[1], type_list))
print(type_list := list(set(type_list)))

new_list = list(map(lambda x: 3.14 * x[0] * x[1], type_list))
print(new_list)

for i in type_list:
    if i[0] * i[1] * 3.14 == max(new_list):
        print(i, max(new_list))
        break
