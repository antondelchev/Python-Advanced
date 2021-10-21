# import sys
from collections import deque

# from io import StringIO

# data = """5, 6, 4, 16, 11, 5, 30, 2, 3, 27
# 1, 13, 5, 3, -7, 32, 19, 3, 5, 7, 22"""
#
# sys.stdin = StringIO(data)

effects = deque(list(map(int, input().split(", "))))
power = list(map(int, input().split(", ")))

fireworks = {
    "p": 0,
    "w": 0,
    "c": 0,
}

for_perfect = False

while not for_perfect:
    if not effects or not power:
        break

    if effects[0] <= 0:
        effects.popleft()
        continue
    if power[-1] <= 0:
        power.pop()
        continue

    first_effect = effects.popleft()
    last_power = power.pop()
    combined = first_effect + last_power

    if combined % 3 == 0 and combined % 5 == 0:
        fireworks["c"] += 1
    elif combined % 3 == 0 and not combined % 5 == 0:
        fireworks["p"] += 1
    elif not combined % 3 == 0 and combined % 5 == 0:
        fireworks["w"] += 1
    else:
        first_effect -= 1
        effects.append(first_effect)
        power.append(last_power)

    if fireworks["p"] >= 3 and fireworks["w"] >= 3 and fireworks["c"] >= 3:
        for_perfect = True

if for_perfect:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if effects:
    print(f"Firework Effects left: {', '.join(map(str, effects))}")
if power:
    print(f"Explosive Power left: {', '.join(map(str, power))}")

print(f"Palm Fireworks: {fireworks['p']}")
print(f"Willow Fireworks: {fireworks['w']}")
print(f"Crossette Fireworks: {fireworks['c']}")
