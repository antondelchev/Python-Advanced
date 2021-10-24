# import sys
from collections import deque

from io import StringIO

# data = """105 20 30 25
# 120 60 11 400 10 1
# """
# 
# sys.stdin = StringIO(data)

materials = list(map(int, input().split()))
magic = deque(map(int, input().split()))

crafted = {
    "Diamond Jewellery": 0,
    "Gemstone": 0,
    "Gold": 0,
    "Porcelain Sculpture": 0,
}

while materials and magic:
    last_material = materials[-1]
    first_magic = magic[0]
    result = last_material + first_magic

    if 100 <= result <= 199:
        crafted["Gemstone"] += 1
        materials.pop()
        magic.popleft()
        continue
    elif 200 <= result <= 299:
        crafted["Porcelain Sculpture"] += 1
        materials.pop()
        magic.popleft()
        continue
    elif 300 <= result <= 399:
        crafted["Gold"] += 1
        materials.pop()
        magic.popleft()
        continue
    elif 400 <= result <= 499:
        crafted["Diamond Jewellery"] += 1
        materials.pop()
        magic.popleft()
        continue

    # second part
    new_sum = 0

    if result < 100 and result % 2 == 0:
        new_sum = (last_material * 2) + (first_magic * 3)
    elif result < 100 and not result % 2 == 0:
        new_sum = 2 * result

    if 100 <= new_sum <= 199:
        crafted["Gemstone"] += 1
        materials.pop()
        magic.popleft()
        continue
    elif 200 <= new_sum <= 299:
        crafted["Porcelain Sculpture"] += 1
        materials.pop()
        magic.popleft()
        continue
    elif 300 <= new_sum <= 399:
        crafted["Gold"] += 1
        materials.pop()
        magic.popleft()
        continue
    elif 400 <= new_sum <= 499:
        crafted["Diamond Jewellery"] += 1
        materials.pop()
        magic.popleft()
        continue

    # third part
    if result > 499:
        new_sum = result // 2

    if 100 <= new_sum <= 199:
        crafted["Gemstone"] += 1
        materials.pop()
        magic.popleft()
        continue
    elif 200 <= new_sum <= 299:
        crafted["Porcelain Sculpture"] += 1
        materials.pop()
        magic.popleft()
        continue
    elif 300 <= new_sum <= 399:
        crafted["Gold"] += 1
        materials.pop()
        magic.popleft()
        continue
    elif 400 <= new_sum <= 499:
        crafted["Diamond Jewellery"] += 1
        materials.pop()
        magic.popleft()
        continue

    materials.pop()
    magic.popleft()


if (crafted["Gemstone"] > 0 and crafted["Porcelain Sculpture"] > 0) \
        or (crafted["Gold"] > 0 and crafted["Diamond Jewellery"] > 0):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(map(str, materials))}")
if magic:
    print(f"Magic left: {', '.join(map(str, magic))}")

for k, v in crafted.items():
    if v > 0:
        print(f"{k}: {v}")
