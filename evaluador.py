class Evaluator:

    def __init__(self):
        self.variables = {}

    def visit(self, node):
        if isinstance(node, int):
            return node

        if node.__class__.__name__ == "Num":
            return node.value

        if node.__class__.__name__ == "BinOp":
            left = self.visit(node.left)
            right = self.visit(node.right)

            if node.op == "PLUS": return left + right
            if node.op == "MINUS": return left - right
            if node.op == "MULT": return left * right
            if node.op == "DIV": return left / right
            if node.op == "MOD": return left % right

        if node.__class__.__name__ == "Var":
            return self.variables.get(node.name, 0)
