from collections import deque

orders = deque([int(el) for el in input().split(", ")])
employee = [int(el) for el in input().split(", ")]

total_pizzas_cooked = 0

while orders and employee:
    if orders[0] > 10:
        orders.popleft()
    elif orders[0] <= 0:
        orders.popleft()
    elif orders[0] <= employee[-1]:
        total_pizzas_cooked += orders[0]
        orders.popleft(), employee.pop()
    elif orders[0] > employee[-1]:
        total_pizzas_cooked += employee[-1]
        orders[0] -= employee[-1]
        employee.pop()

if not orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas_cooked}")
    print(f"Employees: ", end="")
    print(*employee, sep=", ")
elif orders:
    print("Not all orders are completed.")
    print(f"Orders left: ", end="")
    print(*orders, sep=", ")
