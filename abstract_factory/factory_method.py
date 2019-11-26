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


class Customer(metaclass=ABCMeta):
    def __init__(self):
        self.product = None
        self.create_product()

    @abstractmethod
    def create_product(self):
        pass

    def get_product(self):
        return self.product


class ConcreteCustomerA(Customer):
    def create_product(self):
        self.product = ConcreteProductA()


class ConcreteCustomerB(Customer):
    def create_product(self):
        self.product = ConcreteProductB()


# If a new customer that likes ConcreteProductB needs to be added...
class ConcreteCustomerC(Customer):
    # With abstract method, the Open/Closed principle is respected.
    def create_product(self):
        self.product = ConcreteProductB()


if __name__ == '__main__':
    customerA = ConcreteCustomerA()
    customerB = ConcreteCustomerB()
    customerC = ConcreteCustomerC()

    assert type(customerA.get_product()) == ConcreteProductA
    assert type(customerB.get_product()) == ConcreteProductB
    assert type(customerC.get_product()) == ConcreteProductB
