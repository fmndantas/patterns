from abc import ABCMeta, abstractmethod


class Subject(metaclass=ABCMeta):
    @abstractmethod
    def do_thing(self):
        pass


class RealSubject(Subject):
    def do_thing(self):
        print("RealSubject:: doing thing")


class Proxy(Subject):
    def __init__(self, real_subject: RealSubject):
        self.real_subject = real_subject

    def do_thing(self):
        print("Proxy:: doing thing")
        self.real_subject.do_thing()


class Client:
    def __init__(self, proxy: Proxy):
        self.proxy = proxy

    def do_thing_with_proxy(self):
        self.proxy.do_thing()


if __name__ == '__main__':
    rs = RealSubject()
    p = Proxy(real_subject=rs)
    c = Client(proxy=p)
    c.do_thing_with_proxy()
