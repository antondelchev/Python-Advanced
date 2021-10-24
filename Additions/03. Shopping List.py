def shopping_list(budget, **kwargs):
    if budget >= 100:
        basket = {}
        for item in kwargs.items():
            name = item[0]
            price, quantity = item[1][0], item[1][1]
            if price * quantity <= budget:
                basket[name] = price * quantity
                budget -= price * quantity
            if len(basket) > 4:
                break
            if budget <= 0:
                break
        result = []

        for k, v in basket.items():
            result.append(f"You bought {k} for {v:.2f} leva.")
        return "\n".join(result)

    else:
        return "You do not have enough budget."


print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))
