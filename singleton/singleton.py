# Only one instance is returned, forever


class Singleton(object):
    def __new__(klass):
        if not hasattr(klass, 'instance'):
            klass.instance = super(Singleton, klass).__new__(klass)
        return klass.instance


class LazySingleton(object):
    """
    instance, que é o atributo que interessa, é None, inicialmente.
    get_instance transforma instance em uma instância de LazySingleton.
    A partir de agora, instance não é mais None e __init__ determina
    que instance do objeto seja sempre a mesma instância originalmente
    criada por get_instance.
    """
    __instance = None

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = super(LazySingleton, cls).__new__(cls)
        return cls.__instance


class Borg(object):
    shared = {'um': 1}

    def __init__(self):
        self.extra = 'Extra data'
        self.__dict__ = self.shared


def test_singleton():
    s1 = Singleton()
    s2 = Singleton()
    assert id(s1) == id(s2)


def test_lazy_singleton():
    l = LazySingleton()
    assert l._LazySingleton__instance is None
    LazySingleton.get_instance()
    l1 = LazySingleton()
    assert id(l1.get_instance()) == id(l.get_instance())


def test_borg():
    b = Borg()
    b1 = Borg()
    assert id(b) != id(b1)
    b1.extra = 'new extra data'
    assert b.extra == b1.extra


if __name__ == '__main__':
    test_singleton()
    test_lazy_singleton()
    test_borg()
