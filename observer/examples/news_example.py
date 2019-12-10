from abc import ABCMeta, abstractmethod


# Observer
class Subscriber(metaclass=ABCMeta):
    def __init__(self):
        self.subject = None

    def subscribe(self, subject):
        subject.attach(self)
        self.subject = subject

    # notify should be abstract because we want
    # minimum coupling between subject and observer
    # therefore, all subject needs to know is that
    # notify is an interface
    @abstractmethod
    def notify(self, *args, **kwargs):
        pass


# Concrete observer
class NewspaperReader(Subscriber):
    def notify(self):
        print("\nNewspaperReader:: notifying via newspaper"
              f"\nMessage: '{self.subject.get_last_news()}'")


# Concrete observer
class CellphoneReader(Subscriber):
    def notify(self):
        print("\nCellphoneReader:: notifying via cellphone"
              f"\nMessage: '{self.subject.get_last_news()}'")


class EmailReader(Subscriber):
    def notify(self):
        print("\nEmailReader:: notifying via e-mail"
              f"\nMessage: '{self.subject.get_last_news()}'")


# Subject
class NewsPublisher:
    def __init__(self):
        self.readers = []
        self.last_news = None

    def attach(self, reader):
        self.readers.append(reader)

    def detach(self, reader):
        self.readers.remove(reader)

    def set_last_news(self, news):
        self.last_news = news

    def get_last_news(self):
        return self.last_news

    def notify_all(self):
        for reader in self.readers:
            reader.notify()


if __name__ == '__main__':
    np = NewsPublisher()

    nr = NewspaperReader()
    nr.subscribe(np)

    cr = CellphoneReader()
    cr.subscribe(np)

    er = EmailReader()
    er.subscribe(np)

    np.set_last_news("Fernando is learning to use Observer Pattern")
    np.notify_all()

    np.set_last_news("Fernando now thinks he got the idea")
    np.notify_all()

    np.detach(er)

    np.set_last_news("We have been losing subscribers. Are our news OK?")
    np.notify_all()
