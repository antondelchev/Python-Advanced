n = int(input())
unique_names = set()

for _ in range(1, n + 1):
    name = input()
    unique_names.add(name)

print("\n".join(unique_names))
