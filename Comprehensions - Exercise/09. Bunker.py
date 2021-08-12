bunker = {category: [] for category in input().split(", ")}
n = int(input())
total_count = 0
total_quality = 0

for _ in range(n):
    category, food, data = input().split(" - ")
    quantity = int(data.split(";")[0].split(":")[1])
    quality = int(data.split(";")[1].split(":")[1])

    total_count += quantity
    total_quality += quality

    bunker[category].append(food)

print(f"Count of items: {total_count}")
print(f"Average quality: {total_quality / (len(bunker)):.2f}")
[print(f"{k} -> {', '.join(v)}") for k, v in bunker.items()]
