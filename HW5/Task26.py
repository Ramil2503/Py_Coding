# Write a program that takes two numbers A and B as input and raises the number A to the integer power of B using recursion.

a = int(input("Enter the value for base: "))
b = int(input("Enter the value for power: "))

def power(a, b):
    if b == 0: 
        return 1
    else:
        return a * power(a, b - 1)

print(power(a, b))
