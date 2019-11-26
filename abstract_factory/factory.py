from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    @abstractmethod
    def get_vertices(self):
        pass


class Square(Shape):
    def get_vertices(self):
        return 4


class Triangle(Shape):
    def get_vertices(self):
        return 3


class ShapeFactory:
    def factory_shape(self, name):
        return eval(name)()


if __name__ == '__main__':
    sf = ShapeFactory()

    t = sf.factory_shape('Triangle')
    assert t.get_vertices() == 3

    q = sf.factory_shape('Square')
    assert t.get_vertices() == 4
