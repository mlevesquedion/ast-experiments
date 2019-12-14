import ast


def fields(ast_node):
    if isinstance(ast_node, ast.List):
        return dir([])
    else:
        return []


class IllegalAttributeAccessVisitor(ast.NodeVisitor):
    def __init__(self):
        self.is_valid = True

    def visit_Attribute(self, node):
        value, attr = node.value, node.attr
        if attr not in fields(value):
            self.is_valid = False
        self.generic_visit(node)


def check(code):
    ast_ = ast.parse(code)
    visitor = IllegalAttributeAccessVisitor()
    visitor.visit(ast_)
    return visitor.is_valid
