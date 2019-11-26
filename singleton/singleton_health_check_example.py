class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class HealthCheck(metaclass=MetaSingleton):
    def __init__(self):
        self.servers = []

    def add_server(self, key):
        self.servers.append(key)

    def remove_server(self, key):
        pos = self.servers.index(key)
        self.servers.pop(pos)

    def get_current_servers(self):
        return self.servers


def test_health_check():
    h1 = HealthCheck()
    h2 = HealthCheck()

    assert id(h1) == id(h2)

    h1.add_server('A')
    h1.add_server('B')

    assert h2.get_current_servers() == ['A', 'B']

    h2.remove_server('B')
    h2.add_server('C')
    h2.add_server('D')

    assert h1.get_current_servers() == ['A', 'C', 'D']


if __name__ == '__main__':
    test_health_check()
