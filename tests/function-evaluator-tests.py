import unittest
import math
from tokenizer import Tokenizer
from function import Function


class TokenizerTest(unittest.TestCase):
    def test_tokenization(self):
        tokens_list = list(map(str, Tokenizer.tokenize('2*sin(1/(cos(3*x)+1)')))
        self.assertEqual(tokens_list, ['2', '*', 'sin', '(', '1', '/', '(', 'cos', '(', '3', '*', 'x', ')',
                                       '+', '1', ')'])


class FunctionTest(unittest.TestCase):
    def test_operations(self):
        self.assertEqual(Function('2+3-4-x+10-x').calc(2), 2+3-4-2+10-2)
        self.assertEqual(Function('3*14-9/3*x-x*x/2').calc(3), 3*14-9/3*3-3*3/2)
        self.assertEqual(Function('-(4+5)/x-3*12+45/9').calc(4), -(4+5)/4-3*12+45/9)
        self.assertEqual(Function('pow((47.259*10-100)/10,x)').calc(2), math.pow((47.259*10-100)/10, 2))


    def test_functions(self):
        self.assertEqual(Function('2*sin(1/(exp(3*x)+1)-tg(x+PI/2))').calc(3),
                         2*math.sin(1/(math.exp(3*3)+1)-math.tan(3+math.pi/2)))
        self.assertEqual(Function('pow(x,pow(2,3))').calc(2),
                         2**2**3)
        self.assertEqual(Function('pow(pow(pow(-(1*2/x)-(-(-(1-2+3)))-(-1+-2+-3)+(-(-1-2-3)),1),1),1)').calc(2),
                                  -(1*2/2)-(-(-(1-2+3)))-(-1+-2+-3)+(-(-1-2-3))**1**1**1**1**1)
        self.assertEqual(Function('sin(sin(-0.2+sin(cos(0.1-cos(cos(1.5))))-0.5)+0.5)').calc(2),
                         math.sin(math.sin(-0.2+math.sin(math.cos(0.1-math.cos(math.cos(1.5))))-0.5)+0.5))

if __name__ == '__main__':
    unittest.main()
