from tokenizer import Tokenizer
import math


class Function:
    def __init__(self, formula):
        self.tokens = Tokenizer.tokenize(formula)
        self.precedence = {
            '!': 9,
            '*': 8,
            '/': 8,
            '+': 6,
            '-': 6,
            '(': -1,
        }
        self.constants = {
            'PI': math.pi,
            'E': math.e
        }

    def calc(self, val):
        out = []
        ops = []
        for token in self.tokens:
            if token.kind == 'number':
                out.append(float(token.text))
            elif token.kind == 'variable':
                out.append(val)
            elif token.kind == 'constant':
                out.append(self.constants[token.text])
            elif token.kind == 'function':
                ops.append(token)
            elif token.text == ',':
                while len(ops) > 0:
                    if ops[-1].text == '(':
                        break
                    else:
                        self.apply_operation(ops.pop().text, out)
                else:
                    raise ValueError(f'Opening parenthesis or comma is missing')
            elif token.text == '(':
                ops.append(token)
            elif token.text == ')':
                while len(ops) > 0:
                    if ops[-1].text == '(':
                        ops.pop()
                        break
                    else:
                        self.apply_operation(ops.pop().text, out)
                else:
                    raise ValueError(f'Opening parenthesis is missing for \')\' at position {token.index}')
            else:
                while len(ops) > 0 and (ops[-1].kind == 'function' or
                                        self.precedence[ops[-1].text] >= self.precedence[token.text]):
                    self.apply_operation(ops.pop().text, out)
                ops.append(token)
        while len(ops) > 0:
            token = ops.pop()
            if token.text == '(':
                raise ValueError(f'Closing parenthesis is missing for \'(\' at position {token.index}')
            self.apply_operation(token.text, out)
        return out[0]

    def apply_operation(self, operation, out):
        if operation == '!':
            out.append(-out.pop())
        if operation == '+':
            out.append(out.pop() + out.pop())
        if operation == '-':
            op1 = out.pop()
            op2 = out.pop()
            out.append(op2 - op1)
        if operation == '*':
            out.append(out.pop() * out.pop())
        if operation == '/':
            op1 = out.pop()
            op2 = out.pop()
            out.append(op2 / op1)
        if operation == 'pow':
            op1 = out.pop()
            op2 = out.pop()
            out.append(op2 ** op1)
        if operation == 'sin':
            out.append(math.sin(out.pop()))
        if operation == 'cos':
            out.append(math.cos(out.pop()))
        if operation == 'tg':
            out.append(math.tan(out.pop()))
        if operation == 'abs':
            out.append(abs(out.pop()))
        if operation == 'sqrt':
            out.append(math.sqrt(out.pop()))
        if operation == 'exp':
            out.append(math.e ** out.pop())
