nums = [int(el) for el in input().split()]
positive = [el for el in nums if el >= 0]
negative = [el for el in nums if el < 0]

print(sum(negative))
print(sum(positive))

if abs(sum(negative)) > sum(positive):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
