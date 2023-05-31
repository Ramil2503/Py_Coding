array_length = int(input("Print the length of the array: "))

input_array = input("Enter array separated by space: ").split()

array = list(map(int, input_array))

if len(array) != array_length:
    print("The array_length you provided is not similar to actual array length")
else: 
    x = int(input("Print 'x' you are searching for in this array: "))
    cnt = 0
    for i in range(array_length):
        if x == array[i]:
            cnt += 1
print(f'number {x} appeared {cnt} times in your array')
