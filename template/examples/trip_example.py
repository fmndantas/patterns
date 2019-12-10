from abc import ABCMeta, abstractmethod


# Abstract class
class Trip(metaclass=ABCMeta):
    @abstractmethod
    def set_transport(self):
        pass

    @abstractmethod
    def day_one(self):
        pass

    @abstractmethod
    def day_two(self):
        pass

    @abstractmethod
    def day_three(self):
        pass

    @abstractmethod
    def return_home(self):
        pass

    def itinerary(self):
        self.set_transport()
        self.day_one()
        self.day_two()
        self.day_three()
        self.return_home()


class BrazilTrip(Trip):
    def set_transport(self):
        print("BrazilTrip, transport: bus")

    def day_one(self):
        print("BrazilTrip: Rio de Janeiro")

    def day_two(self):
        print("BrazilTrip: Salvador")

    def day_three(self):
        print("BrazilTrip: Minas Gerais")

    def return_home(self):
        print("BrazilTrip: returning home")


class EuropeanTrip(Trip):
    def set_transport(self):
        print("EuropeanTrip, transport: air-plain")

    def day_one(self):
        print("EuropeanTrip: Italy")

    def day_two(self):
        print("EuropeanTrip: Portugal")

    def day_three(self):
        print("EuropeanTrip: Spain")

    def return_home(self):
        print("EuropeanTrip: returning home")


if __name__ == '__main__':
    brazilian_guy = EuropeanTrip()
    european_guy = BrazilTrip()
    brazilian_guy.itinerary()
    european_guy.itinerary()
