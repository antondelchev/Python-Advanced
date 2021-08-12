def stock_availability(input_list, *args):
    if "delivery" in args:

        [input_list.append(el) for el in args if not el == "delivery"]

    elif "sell" in args:

        if len(args) == 1:
            input_list.pop(0)
        else:
            for el in args:
                if str(el).isdigit():
                    while el > 0:
                        if input_list:
                            input_list.pop(0)
                            el -= 1
                        else:
                            input_list = []
                            break
                elif not el == "sell":
                    while el in input_list:
                        input_list.remove(el)

    return input_list


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
