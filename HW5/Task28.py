# Write a recursive sum(a, b) function that returns the sum of two non-negative integers. 
# Of all the arithmetic operations, only +1 and -1 are allowed. You can't use loops either.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

def sum(a, b):
    if b == 0:
        return a
    else:
        return sum(a + 1, b - 1)

print(sum(a, b))
