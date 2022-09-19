from operations import *

class Executor():

    def __init__(self, graph: dict, in_vars: dict = {}):
        """
        graph: computation graph in a data structure of your choosing
        in_vars: dict of input variables, e.g. {"x": 2.0, "y": -1.0}
        """
        self.graph = graph
        self.in_vars = in_vars
        self.fn_map = {"log": Log(), "exp": Exp(), "+": Add(), "-": Sub(), "^": Pow(), "sin": Sin(), "*": Mult(), "/": Div()}
        self.output = -1
        self.derivative = {}

    ## forward execution____________________________

    def forward(self, ):
        pass  ## ToDO: implement and set self.output
        self.output = -1

    ## backward execution____________________________

    def backward(self, ):
        pass  ## ToDO: implement and set self.derivative
        self.derivative = {}



if __name__ == '__main__':
    pass