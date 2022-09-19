from abc import ABC, abstractmethod
import math

class Operator(ABC):

    @abstractmethod
    def f(self, a, b = None) -> float:
        raise NotImplementedError()
        return f_res

    @abstractmethod
    def df(self, a, b = None) -> list:
        raise NotImplementedError()
        return [df_res]


class Exp(Operator):

    def f(self, a, b = None):
        return math.exp(a)

    def df(self, a, b = None):
        return [math.exp(a)]


class Log(Operator):
    ## natural logarithm

    def f(self, a, b = None):
        pass ## ToDO: implement

    def df(self, a, b = None):
        pass ## ToDO: implement


class Mult(Operator):

    def f(self, a, b):
        return a * b

    def df(self, a, b=None):
        return [b, a]


class Div(Operator):

    def f(self, a, b):
        pass ## ToDO: implement

    def df(self, a, b):
        pass ## ToDO: implement

class Add(Operator):

    def f(self, a, b):
        pass ## ToDO: implement

    def df(self, a, b = None):
        pass ## ToDO: implement


class Sub(Operator):

    def f(self, a, b = None):
        pass ## ToDO: implement

    def df(self, a, b = None):
        pass ## ToDO: implement


class Pow(Operator):

    def f(self, a, b):
        return a**b

    def df(self, a, b):
        if a <= 0: ## work-around: treat as unary operation if -a^b
            return [b * (a ** (b - 1))]
        else:
            return [b * (a ** (b - 1)), (a ** b) * math.log(a)]


class Sin(Operator):

    def f(self, a, b=None):
        pass ## ToDO: implement

    def df(self, a, b=None):
        pass ## ToDO: implement


class Cos(Operator):

    def f(self, a, b=None):
        pass ## ToDO: implement

    def df(self, a, b=None):
        pass ## ToDO: implement



if __name__ == '__main__':
    pass
