# lexer.py

class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current = text[self.pos] if text else None

    def advance(self):
        self.pos += 1
        self.current = self.text[self.pos] if self.pos < len(self.text) else None

    def skip_whitespace(self):
        while self.current and self.current.isspace():
            self.advance()

    def number(self):
        result = ""
        while self.current and self.current.isdigit():
            result += self.current
            self.advance()
        return Token("NUM", int(result))

    def identifier(self):
        result = ""
        while self.current and (self.current.isalnum() or self.current == "_"):
            result += self.current
            self.advance()
        return Token("ID", result)

    def get_next_token(self):
        while self.current:
            if self.current.isspace():
                self.skip_whitespace()
                continue
            if self.current.isdigit():
                return self.number()
            if self.current.isalpha():
                return self.identifier()

            char = self.current
            self.advance()

            if char == '+': return Token("PLUS", char)
            if char == '-': return Token("MINUS", char)
            if char == '*': return Token("MULT", char)
            if char == '/': return Token("DIV", char)
            if char == '%': return Token("MOD", char)
            if char == '(': return Token("LPAREN", char)
            if char == ')': return Token("RPAREN", char)
            if char == '=': return Token("ASSIGN", char)
            if char == ';': return Token("SEMICOL", char)

            raise Exception("Error léxico")

        return Token("EOF", None)