from abc import ABCMeta, abstractmethod


# State
class State(metaclass=ABCMeta):
    @abstractmethod
    def handle(self):
        pass


# ConcreteState
class StartState(State):
    def handle(self):
        print("TV switching ON")


# ConcreteSTate
class StopState(State):
    def handle(self):
        print("TV switching OFF")


class TVContext:
    def __init__(self):
        self.state = None

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def handle(self):
        self.state.handle()


if __name__ == '__main__':
    context = TVContext()

    # The TV is initially OFF
    context.set_state(StartState())
    context.handle()

    # Now, the TV is ON
    context.set_state(StopState())
    context.handle()
