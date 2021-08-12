n = int(input())

longest_intersection = set()

for _ in range(n):
    range_one_raw, range_two_raw = input().split("-")
    range_one = str(range_one_raw).split(",")
    range_two = str(range_two_raw).split(",")

    first_sequence = set()
    second_sequence = set()

    for num_one in range(int(range_one[0]), int(range_one[1]) + 1):
        first_sequence.add(int(num_one))

    for num_two in range(int(range_two[0]), int(range_two[1]) + 1):
        second_sequence.add(int(num_two))

    current_intersection = first_sequence.intersection(second_sequence)

    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")
