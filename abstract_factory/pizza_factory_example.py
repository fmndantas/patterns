# The client uses an AbstractFactory to create ConcreteFactories, and the ConcreteFactories create ConcreteProducts,
# by using the AbstractProduct Interface

# Pizza example

from abc import ABCMeta, abstractmethod


class PizzaFactory(metaclass=ABCMeta):  # Abstract factory
    @abstractmethod
    def create_veg_pizza(self):
        pass

    @abstractmethod
    def create_non_veg_pizza(self):
        pass


class IndianPizzaFactory(PizzaFactory):  # Concrete factory 1
    def create_veg_pizza(self):
        return DeluxVeggiePizza()

    def create_non_veg_pizza(self):
        return ChickenPizza()


class USPizzaFactory(PizzaFactory):  # Concrete factory 2
    def create_veg_pizza(self):
        return MexicanVegPizza()

    def create_non_veg_pizza(self):
        return HamPizza()


class VegPizza(metaclass=ABCMeta):  # Abstract product 1
    @abstractmethod
    def prepare(self, veg_pizza):
        pass


class NonVegPizza(metaclass=ABCMeta):  # Abstract product 2
    @abstractmethod
    def serve(self, veg_pizza):
        pass


class DeluxVeggiePizza(VegPizza):  # Concrete product 1
    def prepare(self, veg_pizza):
        print(f"Prepare {self.__class__}")


class MexicanVegPizza(VegPizza):  # Concrete product 2
    def prepare(self, veg_pizza):
        print(f"Prepare {self.__class__}")


class ChickenPizza(NonVegPizza):
    def serve(self, veg_pizza):
        print(f"{self.__class__}, served with Chicken on top of {veg_pizza.__class__}")


class HamPizza(NonVegPizza):
    def serve(self, veg_pizza):
        print(f"{self.__class__}, served with Ham on top of {veg_pizza.__class__}")


if __name__ == '__main__':
    for factory in [IndianPizzaFactory(), USPizzaFactory()]:
        non_veg = factory.create_non_veg_pizza()
        veg = factory.create_veg_pizza()
        non_veg.serve(veg)
        veg.prepare(veg)
