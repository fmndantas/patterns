from abc import abstractmethod, ABCMeta


class State(metaclass=ABCMeta):
    @abstractmethod
    def handle(self):
        pass


class ConcreteStateA(State):
    def handle(self):
        print("ConcreteStateA::handle()")


class ConcreteStateB(State):
    def handle(self):
        print("ConcreteStateB::handle()")


class Context:
    def __init__(self):
        self.state = None

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def handle(self):
        self.state.handle()


if __name__ == '__main__':
    context = Context()
    context.set_state(ConcreteStateA())
    context.handle()

    context.set_state(ConcreteStateB())
    context.handle()
