def stock_availability(inventory, command, *args):
    if command == "delivery":
        items = [el for el in args]
        inventory.extend(items)
        return inventory
    elif command == "sell":
        info = [el for el in args]
        if not info:
            inventory.pop(0)
        elif type(info[0]) == int:
            for _ in range(info[0]):
                if inventory:
                    inventory.pop(0)
        else:
            for el in args:
                while el in inventory:
                    inventory.remove(el)
        return inventory


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
