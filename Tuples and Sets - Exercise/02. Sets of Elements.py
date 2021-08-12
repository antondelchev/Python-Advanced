length_of_set_a, length_of_set_b = [int(el) for el in (input().split())]

a = set()
b = set()

for _ in range(1, length_of_set_a + 1):
    number_a = input()
    a.add(number_a)

for _ in range(1, length_of_set_b + 1):
    number_b = input()
    b.add(number_b)

unique_in_both = a.intersection(b)

print("\n".join(unique_in_both))
