box_of_clothes = input().split()
capacity_for_one_rack = int(input())

rack = []
num_of_racks = 1

while box_of_clothes:
    item = int(box_of_clothes[-1])

    if sum(rack) + item <= capacity_for_one_rack:
        rack.append(int(box_of_clothes.pop()))
    else:
        num_of_racks += 1
        rack.clear()
        rack.append(int(box_of_clothes.pop()))

print(num_of_racks)
