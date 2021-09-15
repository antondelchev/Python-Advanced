expression = input()
opening_parenthesis = []
balanced = True

for el in expression:
    if el in "{[(":
        opening_parenthesis.append(el)
    else:
        if opening_parenthesis:
            if f"{opening_parenthesis.pop()}{el}" not in "(){}[]":
                balanced = False
                break
        else:
            balanced = False
            break

if balanced and not opening_parenthesis:
    print("YES")
else:
    print("NO")
