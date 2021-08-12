txt = [word for word in input().split(", ")]

[print(f"{el} -> {len(el)}", end=", ") if txt.index(el) < len(txt) - 1 else print(f"{el} -> {len(el)}") for el in txt]
