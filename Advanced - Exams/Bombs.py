from collections import deque

effects = deque([int(el) for el in input().split(", ")])
casings = [int(el) for el in input().split(", ")]

datura = 0
cherry = 0
smoke = 0
full = False

while effects and casings:
    created = False
    if effects[0] + casings[-1] == 40:
        datura += 1
        created = True
        effects.popleft(), casings.pop()
    elif effects[0] + casings[-1] == 60:
        cherry += 1
        created = True
        effects.popleft(), casings.pop()
    elif effects[0] + casings[-1] == 120:
        smoke += 1
        created = True
        effects.popleft(), casings.pop()

    if not created:
        casings[-1] -= 5
        if casings[-1] <= 0:
            casings.pop()

    if datura >= 3 and cherry >= 3 and smoke >= 3:
        print("Bene! You have successfully filled the bomb pouch!")
        print(f"Bomb Effects: ", end="")
        print(*effects, sep=", ")
        print(f"Bomb Casings: ", end="")
        print(*casings, sep=", ")
        full = True
        break

if not full:
    print("You don't have enough materials to fill the bomb pouch.")
    if effects:
        print(f"Bomb Effects: ", end="")
        print(*effects, sep=", ")
    else:
        print("Bomb Effects: empty")

    if casings:
        print(f"Bomb Casings: ", end="")
        print(*casings, sep=", ")
    else:
        print("Bomb Casings: empty")

print(f"Cherry Bombs: {cherry}")
print(f"Datura Bombs: {datura}")
print(f"Smoke Decoy Bombs: {smoke}")
