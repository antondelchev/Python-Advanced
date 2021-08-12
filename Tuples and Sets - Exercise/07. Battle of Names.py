n = int(input())

even_nums = set()
odd_nums = set()

for row in range(1, n + 1):
    name = input()
    current_sum = 0

    for letter in name:
        current_sum += ord(letter)
    after_division = int(current_sum / row)

    if after_division % 2 == 0:
        even_nums.add(after_division)
    else:
        odd_nums.add(after_division)

if sum(even_nums) == sum(odd_nums):
    union_values = list(odd_nums.union(even_nums))
    print(*union_values, sep=", ")
elif sum(odd_nums) > sum(even_nums):
    diff_values = list(odd_nums.difference(even_nums))
    print(*diff_values, sep=", ")
elif sum(even_nums) > sum(odd_nums):
    diff_sym_values = list(odd_nums.symmetric_difference(even_nums))
    print(*diff_sym_values, sep=", ")
