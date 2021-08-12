from collections import deque

n = int(input())
queue = deque()

for pump_num in range(1, n + 1):
    amount, distance = input().split()
    amount = int(amount)
    distance = int(distance)
    position = pump_num - 1

    queue.append([amount, distance, position])

for i in range(n):
    fuel = 0
    counter = 0

    for el in queue:
        current_pump = el
        gas = el[0]
        next_pump = el[1]

        fuel += gas
        if fuel < next_pump:
            break
        else:
            counter += 1
            fuel -= next_pump

    if counter == len(queue):
        print(queue[0][2])
        break
    else:
        queue.rotate(-1)
