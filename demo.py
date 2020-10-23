from tokenizer import Tokenizer
from function import Function

if __name__ == '__main__':
    func = Function('2+3*4-7+x')
    print(func.calc(10))
