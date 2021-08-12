nums = list(map(int, input().split(", ")))

positive = [str(el) for el in nums if el >= 0]
negative = [str(el) for el in nums if el < 0]
even = [str(el) for el in nums if el % 2 == 0]
odd = [str(el) for el in nums if not el % 2 == 0]

print(f"Positive: {', '.join(positive)}")
print(f"Negative: {', '.join(negative)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")
