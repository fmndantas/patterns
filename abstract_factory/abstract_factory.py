from abc import ABCMeta, abstractmethod


class AbstractFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_concrete_product1(self):
        pass

    @abstractmethod
    def create_concrete_product2(self):
        pass


class ConcreteFactory1(AbstractFactory):
    def create_concrete_product1(self):
        ConcreteProduct1().create()

    def create_concrete_product2(self):
        ConcreteProduct2().create()


class ConcreteFactory2(AbstractFactory):
    def create_concrete_product1(self):
        AnotherConcreteProduct1().create()

    def create_concrete_product2(self):
        AnotherConcreteProduct2().create()


class AbstractProduct1(metaclass=ABCMeta):
    @abstractmethod
    def create(self):
        pass


class AbstractProduct2(metaclass=ABCMeta):
    @abstractmethod
    def create(self):
        pass


class ConcreteProduct1(AbstractProduct1):
    def create(self):
        print(f'Created {type(self).__name__}')


class ConcreteProduct2(AbstractProduct2):
    def create(self):
        print(f'Created {type(self).__name__}')


class AnotherConcreteProduct1(AbstractProduct1):
    def create(self):
        print(f'Created {type(self).__name__}')


class AnotherConcreteProduct2(AbstractProduct2):
    def create(self):
        print(f'Created {type(self).__name__}')
