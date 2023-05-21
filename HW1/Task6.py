ticket_number = input("Enter your ticket number: ")

is_lucky = sum(int(digit) for digit in ticket_number[:3]) == sum(int(digit) for digit in ticket_number[3:])

if is_lucky:
    print("yes")
else:
    print("no")
