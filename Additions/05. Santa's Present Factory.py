from collections import deque

materials_boxes = [int(x) for x in input().split()]
magic_level = deque(int(x) for x in input().split())

presents = {}

while materials_boxes and magic_level:
    material = materials_boxes.pop()
    magic = magic_level.popleft()
    total_magic_level = material * magic

    if total_magic_level == 150:
        if presents.get("Doll"):
            presents["Doll"] += 1
        else:
            presents["Doll"] = 1
    elif total_magic_level == 250:
        if presents.get("Wooden train"):
            presents["Wooden train"] += 1
        else:
            presents["Wooden train"] = 1
    elif total_magic_level == 300:
        if presents.get("Teddy bear"):
            presents["Teddy bear"] += 1
        else:
            presents["Teddy bear"] = 1
    elif total_magic_level == 400:
        if presents.get("Bicycle"):
            presents["Bicycle"] += 1
        else:
            presents["Bicycle"] = 1

    elif total_magic_level < 0:
        materials_boxes.append(material + magic)
    elif total_magic_level > 0:
        materials_boxes.append(material + 15)
    elif total_magic_level == 0:
        if magic == 0 and material == 0:
            continue
        if magic == 0:
            materials_boxes.append(material)
        elif material == 0:
            magic_level.appendleft(magic)

if (presents.get("Doll") and presents.get("Wooden train")) or \
        (presents.get("Teddy bear") and presents.get("Bicycle")):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials_boxes:
    print(f"Materials left: {', '.join([str(x) for x in reversed(materials_boxes)])}")
if magic_level:
    print(f"Magic left: {', '.join([str(x) for x in magic_level])}")

sorted_presents = sorted(presents.items(), key=lambda k: k[0])

for name, count in sorted_presents:
    print(f"{name}: {count}")
