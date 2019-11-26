from abc import ABCMeta, abstractmethod


class CarFactory(metaclass=ABCMeta):
    @abstractmethod
    def make_sedan(self):
        pass

    @abstractmethod
    def make_hatch(self):
        pass


class FiatFactory(CarFactory):
    def make_sedan(self):
        return FiatSedan()

    def make_hatch(self):
        return FiatHatch()


class GMFactory(CarFactory):
    def make_sedan(self):
        return GMSedan()

    def make_hatch(self):
        return GMHatch()


class Car(metaclass=ABCMeta):
    @abstractmethod
    def deliver_car(self):
        pass


class FiatSedan(Car):
    def deliver_car(self):
        print('Fiat Sedan is delivered')


class FiatHatch(Car):
    def deliver_car(self):
        print('Fiat Hatch is delivered')


class GMSedan(Car):
    def deliver_car(self):
        print('GM Sedan is delivered')


class GMHatch(Car):
    def deliver_car(self):
        print('GM Hatch is delivered')


class Interface:
    def __init__(self):
        self.factories = [FiatFactory(), GMFactory()]

    def deliver_cars(self):
        for factory in self.factories:
            sedan = factory.make_sedan()
            hatch = factory.make_hatch()
            sedan.deliver_car()
            hatch.deliver_car()


if __name__ == '__main__':
    interface = Interface()
    interface.deliver_cars()
