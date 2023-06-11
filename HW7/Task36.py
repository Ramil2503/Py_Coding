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
