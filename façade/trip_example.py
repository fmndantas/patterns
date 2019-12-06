class TripAssistant:  # Façade
    def __init__(self):
        print("\nTripAssistant was contacted")

    def plan_trip(self):
        print("\nLemme do the hard work for you...")
        Hotel().rent_room()
        Restaurant().order_food()
        Park().have_fun()


class Hotel:  # Subsystem
    def rent_room(self):
        print("The room is rented")


class Restaurant:  # Subsystem
    def order_food(self):
        print("The food is ordered")


class Park:  # Subsystem
    def have_fun(self):
        print("Let\'s have some fun!")


# Client should instantiate the Façade
class Myself:
    def __init__(self):
        self.trip_assistant = TripAssistant()

    def plan_trip(self):
        self.trip_assistant.plan_trip()


if __name__ == '__main__':
    me = Myself()
    me.plan_trip()
