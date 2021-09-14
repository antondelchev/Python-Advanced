num_of_lines = int(input())
current_stack = []

for _ in range(num_of_lines):
    command = input().split()
    if command[0] == "1":
        number = command[1]
        current_stack.append(number)
    elif command[0] == "2":
        if current_stack:
            current_stack.pop()
    elif command[0] == "3":
        if current_stack:
            print(max(current_stack))
    elif command[0] == "4":
        if current_stack:
            print(min(current_stack))

result = []
while current_stack:
    result.append(current_stack.pop())

print(", ".join(result))
