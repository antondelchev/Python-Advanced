from collections import deque

expression = deque(input().split())

main = ["red", "yellow", "blue"]
secondary = ["orange", "purple", "green"]

colors_found = []

while expression:
    first = expression.popleft()
    last = expression.pop() if expression else ""
    color = first + last

    if color in main or color in secondary:
        colors_found.append(color)
        continue

    color = last + first
    if color in main or color in secondary:
        colors_found.append(color)
    else:
        first_edit = first[:-1]
        last_edit = last[:-1]

        if first_edit:
            expression.insert((len(expression) // 2), first_edit)
        if last_edit:
            expression.insert((len(expression) // 2), last_edit)

secondary_required = {
    "orange": ["red", "yellow"],
    "purple": ["red", "blue"],
    "green": ["blue", "yellow"],
}

for color in colors_found:
    if color in main:
        continue
    required = secondary_required[color]
    is_valid = all([x in colors_found for x in required])
    if not is_valid:
        colors_found.remove(color)

print(colors_found)
