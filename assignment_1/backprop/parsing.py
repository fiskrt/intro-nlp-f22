import sys
import re
from pyparsing import *
import random

class Parser():

    def __init__(self, print_res: bool = False):

        self.print_res = print_res
        self.expr = self.infix_notation_parser()

    def parse(self, math_string: str, in_vars: dict = {}):
        """
        math_string: str describing math equation, e.g. 'z + sin(x^(2) + y * exp(z))'
        in_vars: optional dict of mapping between input variables and numbers
        RETURN: list of infix parsed string, returns dict of input used_vars
        """
        if self.print_res:
            print(f"\nproblem: {math_string} with input {in_vars}")
        in_vars = self.get_input_variables(math_string, in_vars)
        infix_list = self.expr.parseString(math_string).asList()[0]
        return infix_list, in_vars

    def infix_notation_parser(self, ):
        """
        RETURN: expr py_parse object
        """

        ppc = pyparsing_common

        ParserElement.enablePackrat()
        sys.setrecursionlimit(3000)

        integer = ppc.integer
        variable = Word(alphas, exact=1)
        operand = integer | variable

        expop = Literal("^")
        factop = Literal("!")
        ident = Word(alphas, alphanums + "_$")
        signop = oneOf("+ -")
        multop = oneOf("* /")
        plusop = oneOf("+ -")
        #e = CaselessKeyword("E")
        #pi = CaselessKeyword("PI")

        expr = infixNotation(
            operand,
            [
                (ident, 1, opAssoc.RIGHT),
                (factop, 1, opAssoc.LEFT),
                (expop, 2, opAssoc.RIGHT),
                (signop, 1, opAssoc.RIGHT),
                (multop, 2, opAssoc.LEFT),
                (plusop, 2, opAssoc.LEFT),
            ],
        )

        return expr


    def get_input_variables(self, math_string: str, in_vars: dict = {}):
        """
        math_string: str describing math equation, e.g. 'z + sin(x^(2) + y * exp(z))'
        in_vars: optional dict of mapping between input variables and numbers
        RETURN: returns dict of input used_vars
        """

        in_var_list = list(set(re.findall(r'(?i)(?<![a-z])[a-z](?![a-z])', math_string)))
        random_in_vars = {}

        filtered_in_vars = {}
        for in_var in in_var_list:
            if in_var not in in_vars.keys():
                random_in_vars[in_var] = float(random.randint(1, 3)) ## random input
            else:
                filtered_in_vars[in_var] = in_vars[in_var]

        if self.print_res:
            print(f"generated random input {random_in_vars} and kept {filtered_in_vars}")
        return {**filtered_in_vars, **random_in_vars}



if __name__ == '__main__':

    p = Parser()

    ## variables need to be single lower-case chars
    test = [
        'z + sin(x^(2) + y * exp(z))',
        'exp(y^(-x) - log(z)) + (y - z)^2 * log(v)',
        'exp(2) - 3',
        'exp(x) - (y * 2)'
    ]

    for t in test:
        print(t)
        print(p.parse(t, in_vars={"x": 2, "y":-2}))
        print("")