text = input()

all_symbols = {}

for el in text:
    if el not in all_symbols.keys():
        all_symbols[el] = 0
    all_symbols[el] += 1

sorted_elements = sorted(all_symbols.items(), key=lambda x: x[0])

for item in sorted_elements:
    print(f"{item[0]}: {item[1]} time/s")
