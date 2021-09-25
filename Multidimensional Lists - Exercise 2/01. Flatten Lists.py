line = input().split("|")
result = []

for sub in line[::-1]:
    elements = sub.split()
    for el in elements:
        result.append(el)

print(*result)
