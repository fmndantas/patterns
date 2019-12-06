from abc import ABCMeta, abstractmethod


# Observer
class Subscriber(metaclass=ABCMeta):
    def __init__(self):
        self.subject = None

    def subscribe(self, subject: NewsPublisher): ...

    @abstractmethod
    def notify(self, *args, **kwargs): ...


# Concrete observer
class NewspaperReader(Subscriber):
    def subscribe(self, subject: NewsPublisher): ...

    def notify(self): ...


# Concrete observer
class CellphoneReader(Subscriber):
    def subscribe(self, subject: NewsPublisher): ...

    def notify(self): ...


# Concrete observer
class EmailReader(Subscriber):
    def subscribe(self, subject: NewsPublisher): ...

    def notify(self): ...


# Subject
class NewsPublisher:
    def __init__(self):
        self.readers = []
        self.last_news = None

    def attach(self, observer: Subscriber): ...

    def detach(self, observer: Subscriber): ...

    def set_last_news(self, news: str): ...

    def get_last_news(self): ...

    def notify_all(self): ...
