from abc import ABCMeta, abstractmethod


class State:
    # name and allowed are static attributes
    # so that the following statements are valid
    # 1. State.name
    # 2. State.allowed
    # instead
    # 1. State().name
    # 2. State().allowed
    # resuming, the attributes may be accessed via class
    # and not via an class object
    name = None
    allowed = None

    def change(self, next_state):
        if next_state.name in self.allowed:
            print(f"{self.name} => {next_state.name}")

            # Here, the class of PCContext.state is being
            # altered on run time. Initially, the class
            # is initial_state, but it needs to change
            # according to the system state change
            setattr(self, '__class__', next_state)
        else:
            print(f"{self.name} =\> {next_state.name}")


class On(State):
    name = "on"
    allowed = ['off', 'suspend', 'hibernate']


class Off(State):
    name = "off"
    allowed = ['on']


class Hibernate(State):
    name = "hibernate"
    allowed = ['on']


class Suspend(State):
    name = "suspend"
    allowed = ['on']


class PCContext:
    def __init__(self, initial_state=Off):
        self.state = initial_state()

    def change(self, next_state):
        self.state.change(next_state)


if __name__ == '__main__':
    context = PCContext(Off)
    context.change(On)
    context.change(Suspend)
    context.change(Off)
    context.change(On)
    context.change(Off)
