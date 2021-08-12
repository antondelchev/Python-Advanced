from collections import deque

clock_cycles = [int(el) for el in input().split(", ")]
index_check = int(input())
clock_cycles_sorted = deque(sorted(clock_cycles))

number_to_check = 0
done = False

for index, num in enumerate(clock_cycles):
    if index == index_check:
        number_to_check = num
        break

cycles_needed = clock_cycles[:index_check].count(number_to_check) * number_to_check

while clock_cycles_sorted:
    cycles_needed += clock_cycles_sorted[0]
    if clock_cycles_sorted[0] == number_to_check:
        break
    else:
        clock_cycles_sorted.popleft()

print(cycles_needed)
