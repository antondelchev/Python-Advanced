num_of_commands = int(input())
stack = []

while num_of_commands > 0:
    command = input().split()
    if command[0] == "1":
        stack.append(int(command[1]))
    elif command[0] == "2":
        if stack:
            stack.pop()
    elif command[0] == "3":
        if stack:
            print(max(stack))
    elif command[0] == "4":
        if stack:
            print(min(stack))

    num_of_commands -= 1

reversed_nums = []

while stack:
    reversed_nums.append(str(stack.pop()))

print(", ".join(reversed_nums))
