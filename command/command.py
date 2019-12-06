from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):
    def __init__(self, receiver):
        self.receiver = receiver

    @abstractmethod
    def execute(self):
        pass


class ConcreteCommand(Command):
    def execute(self):
        self.receiver.action()


class Receiver:
    def action(self):
        print("Receiver:: action()")


class Invoker:
    def __init__(self):
        self.cmd = None

    def command(self, command):
        self.cmd = command

    def execute(self):
        self.cmd.execute()


if __name__ == '__main__':
    r = Receiver()
    c = ConcreteCommand(r)
    i = Invoker()
    i.command(c)
    i.execute()
