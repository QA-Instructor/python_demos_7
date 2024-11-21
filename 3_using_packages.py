import food.burger
import food.pizza

meal1 = food.burger.make_burger()
print(meal1)

meal2 = food.pizza.make_pizza("Hawaiian")
print(meal2)

from food.pizza import make_pizza as mp

meal3 = mp("Margherita")
print(meal3)