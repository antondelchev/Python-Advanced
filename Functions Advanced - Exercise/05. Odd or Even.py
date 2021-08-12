command = input()
nums = [int(el) for el in input().split()]

even = [el for el in nums if el % 2 == 0]
odd = [el for el in nums if not el % 2 == 0]

if command == "Even":
    print(sum(even) * len(nums))
elif command == "Odd":
    print(sum(odd) * len(nums))
