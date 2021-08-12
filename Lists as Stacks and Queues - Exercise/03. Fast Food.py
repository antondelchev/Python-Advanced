from collections import deque

food_quantity = int(input())
all_orders = deque(input().split())

flag = False
max_el = 0

for el in all_orders:
    if int(el) > max_el:
        max_el = int(el)

print(max_el)

while all_orders:
    if int(all_orders[0]) <= food_quantity:
        food_quantity -= int(all_orders[0])
        all_orders.popleft()
    else:
        print(f"Orders left: ", end="")
        for element in all_orders:
            print(element, end=" ")
        flag = True
        break

if not flag:
    print("Orders complete")
