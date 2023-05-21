number = int(input("Enter any number: "))

digit_sum = sum(int(digit) for digit in str(number))

print("Sum of digits:", digit_sum)
