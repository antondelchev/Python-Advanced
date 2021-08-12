from collections import deque

effects = deque([int(el) for el in input().split(", ")])
power = [int(el) for el in input().split(", ")]

palm = 0
willow = 0
crossette = 0
done = False

while effects and power:
    if effects[0] <= 0:
        effects.popleft()
        continue
    elif power[-1] <= 0:
        power.pop()
        continue

    if (effects[0] + power[-1]) % 3 == 0 and not (effects[0] + power[-1]) % 5 == 0:
        palm += 1
        effects.popleft(), power.pop()
    elif not (effects[0] + power[-1]) % 3 == 0 and (effects[0] + power[-1]) % 5 == 0:
        willow += 1
        effects.popleft(), power.pop()
    elif (effects[0] + power[-1]) % 3 == 0 and (effects[0] + power[-1]) % 5 == 0:
        crossette += 1
        effects.popleft(), power.pop()
    else:
        effects[0] -= 1
        effects.append(effects.popleft())

    if palm >= 3 and willow >= 3 and crossette >= 3:
        print("Congrats! You made the perfect firework show!")
        done = True
        break

if not done:
    print("Sorry. You can't make the perfect firework show.")

if effects:
    print("Firework Effects left: ", end="")
    print(*effects, sep=", ")
if power:
    print("Explosive Power left: ", end="")
    print(*power, sep=", ")

print(f"Palm Fireworks: {palm}")
print(f"Willow Fireworks: {willow}")
print(f"Crossette Fireworks: {crossette}")
