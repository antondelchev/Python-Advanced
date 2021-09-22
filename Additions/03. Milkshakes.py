from collections import deque

chocolates = list((int(x) for x in input().split(", ")))
cups_of_milk = deque(int(x) for x in input().split(", "))

milkshakes_made = 0

while chocolates and cups_of_milk and milkshakes_made < 5:
    last_chocolate = chocolates.pop()
    first_cup = cups_of_milk.popleft()

    if last_chocolate <= 0 and first_cup <= 0:
        continue
    elif last_chocolate <= 0:
        cups_of_milk.appendleft(first_cup)
        continue
    elif first_cup <= 0:
        chocolates.append(last_chocolate)
        continue

    if last_chocolate == first_cup:
        milkshakes_made += 1
    else:
        chocolates.append(last_chocolate - 5)
        cups_of_milk.append(first_cup)

if milkshakes_made == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join([str(x) for x in chocolates])}")
else:
    print("Chocolate: empty")

if cups_of_milk:
    print(f"Milk: {', '.join([str(x) for x in cups_of_milk])}")
else:
    print("Milk: empty")
