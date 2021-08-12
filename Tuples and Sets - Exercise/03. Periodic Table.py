n = int(input())
unique_elements = set()

for _ in range(1, n + 1):
    elements = input().split()

    for el in elements:
        unique_elements.add(el)

print("\n".join(unique_elements))
