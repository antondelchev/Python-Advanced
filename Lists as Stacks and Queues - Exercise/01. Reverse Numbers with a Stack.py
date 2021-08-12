nums = input().split()

nums_reversed = []

while nums:
    nums_reversed.append(nums.pop())

print(*nums_reversed)
