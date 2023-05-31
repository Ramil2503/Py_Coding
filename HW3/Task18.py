array_length = int(input("Print the length of the array: "))

input_array = input("Enter array separated by space: ").split()

array = list(map(int, input_array))

if len(array) != array_length:
    print("The array_length you provided is not similar to actual array length")
else:
    x = int(input("Print 'x' you are searching for in this array (if it will not be in array it will print the closest one): "))
    index = 0
    min_dif = abs(x - array[0])
    for i in range(array_length):
        if abs(x - array[i]) < min_dif:
            min_dif = abs(x - array[i])
            index = i
    print(f'the closest number in array to provided x = {x}, is {array[index]}')
