class Subject:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_all(self, msg):
        for observer in self.observers:
            observer.notify(msg)


class Observer:
    def __init__(self, subject: Subject):
        self.subject = subject

    def notify(self, msg):
        print(
            """\nReceiving notify from subject"""
            f"""\nIt says: \'{msg}\'"""
        )


if __name__ == '__main__':
    s = Subject()
    o1 = Observer(s)
    o2 = Observer(s)
    o3 = Observer(s)

    # Nothing will happen here. Subject is not aware of observers
    s.notify_all("The subject is notifying!")

    for o in [o1, o2, o3]:
        s.add_observer(o)

    # Now it will work
    s.notify_all("The subject is notifying!")
