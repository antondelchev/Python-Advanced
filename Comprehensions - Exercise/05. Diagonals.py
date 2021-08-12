n = int(input())
matrix = [[int(el) for el in input().split(", ")] for _ in range(n)]

first = [matrix[index][index] for index in range(n)]
second = [matrix[index][n - 1 - index] for index in range(n)]

sum_first = sum(first)
sum_second = sum(second)

print(f"First diagonal: {', '.join([str(el) for el in first])}. Sum: {sum_first}")
print(f"Second diagonal: {', '.join([str(el) for el in second])}. Sum: {sum_second}")
