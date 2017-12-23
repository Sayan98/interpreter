"""AST - Abstract Syntax Tree
"""

class AST:
    """Abstract base class for AST
    """
    pass


class BinOp:
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right


class Num:
    def __init__(self, token):
        self.token = token
        self.value = token.value