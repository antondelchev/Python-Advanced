from collections import deque

data = input()
order = deque()

while not data == "End":
    if data == "Paid":
        while order:
            print(order.popleft())
    else:
        order.append(data)
    data = input()

print(f"{len(order)} people remaining.")
