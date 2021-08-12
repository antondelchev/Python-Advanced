from collections import deque

males = [int(el) for el in input().split()]
females = deque([int(el) for el in input().split()])

matches_counter = 0

while males and females:
    if males[-1] == 0:
        males.pop()
        continue
    if females[0] == 0:
        females.popleft()
        continue

    if females[0] % 25 == 0:
        females.popleft()
        females.popleft()
        continue

    if males[-1] % 25 == 0:
        males.pop()

    if females[0] == males[-1]:
        matches_counter += 1
        females.popleft(), males.pop()
    else:
        females.popleft()
        males[-1] -= 2
        if males[-1] <= 0:
            males.pop()

print(f"Matches: {matches_counter}")

if males:
    print("Males left: ", end="")
    print(*reversed(males), sep=", ")
else:
    print("Males left: none")

if females:
    print("Females left: ", end="")
    print(*females, sep=", ")
else:
    print("Females left: none")
