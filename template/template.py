from abc import ABCMeta, abstractmethod


class AbstractClass(metaclass=ABCMeta):
    @abstractmethod
    def step_one(self):
        pass

    @abstractmethod
    def step_two(self):
        pass

    @abstractmethod
    def step_three(self):
        pass

    def template_method(self):
        self.step_one()
        self.step_two()
        self.step_three()


class ConcreteClass(AbstractClass):
    def step_one(self):
        print("ConcreteClass:: step_one()")

    def step_two(self):
        print("ConcreteClass:: step_two()")

    def step_three(self):
        print("ConcreteClass:: step_three()")


if __name__ == '__main__':
    # Client code
    cc = ConcreteClass()
    cc.template_method()