names = input().split(", ")

command = input()
heroes = {}

for name_order in names:
    heroes[name_order] = {}

while not command == "End":
    name, item, cost = command.split("-")
    cost = int(cost)

    if not heroes.get(name):
        heroes[name] = {}

    if not heroes[name].get(item):
        heroes[name].update({item: cost})

    command = input()

print(*[f"{name} -> Items: {len(inv)}, Cost: {sum([v for k, v in inv.items()])}" for name, inv in heroes.items()],
      sep="\n")
