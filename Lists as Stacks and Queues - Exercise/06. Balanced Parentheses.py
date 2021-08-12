pattern = input()

opening = []
mirrored = {")": "(", "}": "{", "]": "["}

balanced = True

for el in pattern:
    if el in "({[":
        opening.append(el)
    elif el in ")}]":
        if not opening:
            balanced = False
            break
        else:
            last_opened = opening.pop()
            if not mirrored[el] == last_opened:
                balanced = False
                break

if balanced:
    print("YES")
else:
    print("NO")
