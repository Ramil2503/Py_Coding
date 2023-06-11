# Write a function print_operation_table(operation, num_rows=6, num_columns=6) 
# that takes as an argument a function that calculates an element by row and column number. 
# The num_rows and num_columns arguments specify the number of table rows and columns to be printed. 
# The numbering of rows and columns starts from one (think why not from zero).

def print_operation_table(operation, num_rows=6, num_columns=6):
    for row in range(1, num_rows + 1):
        for column in range(1, num_columns + 1):
            x = row
            y = column
            result = eval(operation)
            print(f"{result:3} ", end=" ")
        print()

operation = input("Enter your operation, use x and y as variables: ")
print_operation_table(operation)
