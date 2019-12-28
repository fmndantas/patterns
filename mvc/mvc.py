class Model:
    def logic(self):
        print("Model::logic()")
        return "this is model data"


class View:
    def update(self, data):
        print(f"View::update(data = {data})")


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def interface(self):
        print("Controller::interface()")
        data = self.model.logic()
        self.view.update(data)


class Client:
    def __init__(self):
        self.controller = Controller()

    def interface(self):
        self.controller.interface()


if __name__ == '__main__':
    client = Client()
    client.interface()
