from abc import ABCMeta, abstractmethod


# Command
class Order(metaclass=ABCMeta):
    """This is an interface to ConcreteCommands"""

    @abstractmethod
    def execute(self):
        pass


# ConcreteCommand
class BuyStockOrder(Order):
    """Actually implements the Order interface
    Knows the Receiver"""

    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.buy()


# ConcreteCommand
class SellStockOrder(Order):
    """Actually implements the Order interface
    Knows the Receiver"""

    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.sell()


# Receiver
class StockTrade:
    """Acts as the Receiver, knowing what to do with the Command"""

    def buy(self):
        print("StockTrade:: buy()")

    def sell(self):
        print("StockTrade:: sell()")


# Invoker
class Agent:
    """Queue the commands to execute their later"""

    def __init__(self):
        # ToDo: change to Stack
        self.__cmds = []

    def _queue(self, cmd):
        self.__cmds.append(cmd)

    def get_queue(self):
        return self.__cmds

    def command(self, cmd):
        cmd.execute()
        self._queue(cmd)

    def roll_back(self, steps):
        cmds = self.__cmds.copy()
        cmds.reverse()
        for i in range(steps):
            self.__cmds.remove(cmds[i])


if __name__ == '__main__':
    # The client creates the Receiver
    stock = StockTrade()

    # The client creates ConcreteCommand objects
    # and sets the Receiver to these objects
    buy = BuyStockOrder(stock)
    sell = SellStockOrder(stock)

    # The Invoker is created
    agent = Agent()

    # The client adds ConcreteCommand objects
    # to the Agent
    agent.command(buy)
    agent.command(buy)
    agent.command(sell)
    agent.command(sell)

    agent.roll_back(2)
    assert all(isinstance(i, BuyStockOrder) for i in agent.get_queue())
