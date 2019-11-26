class MetaString(type):
    def __call__(cls, *args, **kwargs):
        print(f'argstr: {args[0]}')
        return type.__call__(cls, *args, **kwargs)


class MyString(metaclass=MetaString):
    def __init__(self, string):
        self.string = string


def test_metaclass():
    # Sem uma metaclasse, o objeto é criado com
    # type(cls, bases, dict)
    # Com uma metaclasse, o objeto é criado com
    # metaclasse(cls, bases, dict)
    mystr = MyString('Fernando')
    mystr2 = str('Fernando')


if __name__ == '__main__':
    test_metaclass()
