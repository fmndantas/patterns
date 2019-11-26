class AbstractNode:
    def __init__(self, data=None):
        self.data = data


class Node(AbstractNode):
    def __init__(self, data=None):
        super(Node, self).__init__(data)

    def get_data(self):
        return self.data

    def change_data(self, new_data):
        self.data = new_data


class ImutableNode(AbstractNode):
    def __init__(self, data=None):
        super(ImutableNode, self).__init__(data)

    def get_data(self, new_data):
        return self.data

    def change_data(self, *args):
        raise PermissionError('The node is imutable')


if __name__ == '__main__':
    node = Node(100)
    imutable_node = ImutableNode(-100)

    node.change_data(-100)
    print(node.get_data())

    imutable_node.change_data(100)
