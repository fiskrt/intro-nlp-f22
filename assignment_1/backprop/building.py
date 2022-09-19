from collections import defaultdict

class Builder():

    def __init__(self, infix: list, in_vars: dict = {}):
        """
        infix: list of infix notation parse, e.g. [['exp', 2], '-', 3]
        in_vars: dict of input variables to ensure they are not used as intermediate or output variables
        RETURN: computation graph in a data structure of your choosing
        """

        ## some alphabetical vars to use as intermediate and output variables minus the input vars to avoid duplicates
        avail_vars = list(map(chr, range(97, 123))) + list(map(chr, range(945, 969)))
        if len(in_vars.keys()) > 0:
            avail_vars = set(avail_vars) - set(in_vars)
        self.avail_vars = sorted(list(set(avail_vars)), reverse=True)

        self.infix = infix
        self.graph = None
        pass  ## ToDO: implement and set self.graph


if __name__ == '__main__':
   pass