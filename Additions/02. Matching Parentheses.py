expression = "1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5"
opening_indices = []

for index, el in enumerate(expression):
    if el == "(":
        opening_indices.append(index)
    elif el == ")":
        start_index = opening_indices.pop()
        end_index = index + 1
        print(expression[start_index:end_index])
