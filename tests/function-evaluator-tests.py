import unittest
from tokenizer import Tokenizer
from function import Function


class TokenizerTest(unittest.TestCase):
    def test_tokenization(self):
        tokens_list = list(map(str, Tokenizer.tokenize('2*sin(1/(cos(3*x)+1)')))
        self.assertEqual(tokens_list, ['2', '*', 'sin', '(', '1', '/', '(', 'cos', '(', '3', '*', 'x', ')',
                                       '+', '1', ')'])


class FunctionTest(unittest.TestCase):
    def test_simple_operations(self):
        self.assertEqual(Function('2+3-4-x+10-x').calc(2), 2+3-4-2+10-2)
        self.assertEqual(Function('3*14-9/3*x-x*x/2').calc(3), 3*14-9/3*3-3*3/2)
        # self.assertEqual(Function('-(4+5)/x-3*12+45/9').calc(4), (4+5)/4-3*12+45/9)


if __name__ == '__main__':
    unittest.main()
