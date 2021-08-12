nums_clean = [[sub for sub in item if not sub == " "] for item in [el.split() for el in input().split("|")]]
nums_clean.reverse()

[print(*el, end=" ") for el in nums_clean]
