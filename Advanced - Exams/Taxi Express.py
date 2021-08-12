from collections import deque

customer_time_needed = deque([int(el) for el in input().split(", ")])
taxi_driving_time = [int(el) for el in input().split(", ")]

total_time = 0

while customer_time_needed and taxi_driving_time:

    if taxi_driving_time[-1] >= customer_time_needed[0]:
        total_time += customer_time_needed[0]
        taxi_driving_time.pop(), customer_time_needed.popleft()
    else:
        taxi_driving_time.pop()

if not customer_time_needed:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
else:
    print("Not all customers were driven to their destinations")
    print("Customers left: ", end="")
    print(*customer_time_needed, sep=", ")
