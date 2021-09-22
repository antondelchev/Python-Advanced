first = set(int(x) for x in input().split())
second = set(int(x) for x in input().split())
n = int(input())

for _ in range(n):
    line = input().split()
    command = line[0]
    command_details = line[1]
    if command == "Add" and command_details == "First":
        [first.add(int(x)) for x in line[2:]]
    elif command == "Add" and command_details == "Second":
        [second.add(int(x)) for x in line[2:]]
    elif command == "Remove" and command_details == "First":
        numbers = set([int(x) for x in line[2:]])
        first = first.difference(numbers)
    elif command == "Remove" and command_details == "Second":
        numbers = set([int(x) for x in line[2:]])
        second = second.difference(numbers)
    else:
        print(first.issubset(second) or second.issubset(first))

print(", ".join([str(x) for x in sorted(first)]))
print(", ".join([str(x) for x in sorted(second)]))
