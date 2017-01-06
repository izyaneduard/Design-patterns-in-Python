class Pizza(object):
    def __init__(self):
        self._price = None

    def get_price(self):
        return self._price

class HamAndMushroomPizza(Pizza):
    def __init__(self):
        self._price = 9.8

class DeluxePizza(Pizza):
    def __init__(self):
        self._price = 4.8

class HawaiianPizza(Pizza):
    def __init__(self):
        self._price = 6.18

class PizzaFactory(object):
    counter = 0
    pizzas = {
                "HamAndMushroom": HamAndMushroomPizza,
                "Deluxe":DeluxePizza,
                "Hawaiian":HawaiianPizza,
            }
    @classmethod
    def create_pizza(cls,pizza_type):
        if pizza_type in cls.pizzas:
            cls.counter += 1
            return cls.pizzas.get(pizza_type)()


if __name__ == '__main__':
    for pizza_type in ('HamAndMushroom', 'Deluxe', 'Hawaiian'):
        print("Price of {0} is {1}".format(pizza_type,PizzaFactory.create_pizza(pizza_type).get_price()))
