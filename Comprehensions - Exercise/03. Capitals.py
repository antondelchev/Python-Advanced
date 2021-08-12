countries = [el for el in input().split(", ")]
capitals = [el for el in input().split(", ")]

all_items = {k: v for k, v in zip(countries, capitals)}
[print(f"{k} -> {v}") for k, v in all_items.items()]
