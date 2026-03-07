from ast_nodes import *
from lexer import Lexer

class Parser:

    def __init__(self, text):
        self.lexer = Lexer(text)
        self.current_token = self.lexer.get_next_token()

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            raise Exception("Error sintáctico")

    def factor(self):
        token = self.current_token
        if token.type == "NUM":
            self.eat("NUM")
            return Num(token.value)
        elif token.type == "ID":
            self.eat("ID")
            return Var(token.value)
        elif token.type == "LPAREN":
            self.eat("LPAREN")
            node = self.expr()
            self.eat("RPAREN")
            return node

    def term(self):
        node = self.factor()
        while self.current_token.type in ("MULT", "DIV", "MOD"):
            token = self.current_token
            self.eat(token.type)
            node = BinOp(node, token.type, self.factor())
        return node

    def expr(self):
        node = self.term()
        while self.current_token.type in ("PLUS", "MINUS"):
            token = self.current_token
            self.eat(token.type)
            node = BinOp(node, token.type, self.term())
        return node

    def parse(self):
        return self.expr()
