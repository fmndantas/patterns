"""
This example shows the application of Singleton Pattern
on the creation of a database access. The GenericMetaSingleton
class is allows only one instance of Database being shared among
all created Database objects
"""


class GenericMetaSingleton(type):
    # This metaclass works with any type
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(GenericMetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=GenericMetaSingleton):
    pass


def test_singleton_database():
    db1 = Database()
    db2 = Database()
    db3 = Database()
    assert id(db1) == id(db2)
    assert id(db2) == id(db3)


if __name__ == '__main__':
    test_singleton_database()
