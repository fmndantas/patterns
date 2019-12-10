from abc import ABCMeta, abstractmethod


class Product(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass


class ConcreteProductA(Product):
    def describe(self):
        print('This is a Product A')


class ConcreteProductB(Product):
    def describe(self):
        print('This is a Product B')


class Creator(metaclass=ABCMeta):
    def __init__(self):
        self.product = None
        self.factory_method()

    @abstractmethod
    def factory_method(self):
        pass

    def get_product(self):
        return self.product


class ConcreteCreatorA(Creator):
    def factory_method(self):
        self.product = ConcreteProductA()


class ConcreteCreatorB(Creator):
    def factory_method(self):
        self.product = ConcreteProductB()


# If a new customer that likes ConcreteProductB needs to be added...
class ConcreteCreatorC(Creator):
    # With abstract method, the Open/Closed principle is respected.
    def factory_method(self):
        self.product = ConcreteProductB()


if __name__ == '__main__':
    customerA = ConcreteCreatorA()
    customerB = ConcreteCreatorB()
    customerC = ConcreteCreatorC()

    assert type(customerA.get_product()) == ConcreteProductA
    assert type(customerB.get_product()) == ConcreteProductB
    assert type(customerC.get_product()) == ConcreteProductB
