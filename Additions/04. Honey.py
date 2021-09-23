from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

honey = 0

math_actions = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}

while bees and nectar:
    current_bee = bees.popleft()
    current_nectar = nectar.pop()
    if current_nectar >= current_bee:
        action = symbols.popleft()
        if action == "/" and current_nectar == 0:
            continue
        else:
            result = math_actions[action](current_bee, current_nectar)
            honey += abs(result)
    else:
        bees.appendleft(current_bee)

print(f"Total honey made: {honey}")

if bees:
    bees_left = ", ".join(str(x) for x in bees)
    print(f"Bees left: {bees_left}")
if nectar:
    nectar_left = ", ".join(str(x) for x in nectar)
    print(f"Nectar left: {nectar_left}")
