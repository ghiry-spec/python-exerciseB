pizzas = ["pepperoni", "margherita", "pineapple", "keju", "veggie"]
friends_pizzas = pizzas[:]

pizzas.append("hawaiian")
friends_pizzas.append("bbq chicken")

print("Pizza favoritku adalah:")
for pizza in pizzas:
    print(pizza)

print("\nPizza favorit temanku adalah:")
for pizza in friends_pizzas:
    print(pizza)

