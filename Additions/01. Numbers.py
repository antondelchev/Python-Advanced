first_expression = set(input().split())
second_expression = set(input().split())
num_of_commands = int(input())

for _ in range(num_of_commands):
    command_info = input().split()
    if command_info[0] == "Add":
        command, expression, *numbers = command_info
        numbers = set(numbers)
        if expression == "First":
            first_expression.update(numbers)
        elif expression == "Second":
            second_expression.update(numbers)

    elif command_info[0] == "Remove":
        command, expression, *numbers = command_info
        numbers = set(numbers)
        if expression == "First":
            first_expression = first_expression.difference(numbers)
        elif expression == "Second":
            second_expression = second_expression.difference(numbers)

    elif command_info[0] == "Check" and command_info[1] == "Subset":
        if first_expression.issubset(second_expression) and first_expression and second_expression:
            print("True")
        elif second_expression.issubset(first_expression) and first_expression and second_expression:
            print("True")
        else:
            print("False")

print(", ".join(sorted(first_expression)))
print(", ".join(sorted(second_expression)))
