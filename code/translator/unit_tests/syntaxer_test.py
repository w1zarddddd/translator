import unittest
import sys
import os

sys.path.append(os.path.join(os.getcwd(), 'code/translator'))

from lexer import Token
from syntaxer import SyntaxAnalyzer

unexpected_token = [
    [Token(type='VARIABLE', value='a', line=1, column=0), Token(type='ASSIGN', value='=', line=1, column=2), Token(type='NUMBER', value='5', line=1, column=4), Token(type='OPERATOR',
                                                                                                                                                                      value='+', line=1, column=6), Token(type='FUNC', value='math.sin', line=1, column=8), Token(type='LPAR', value='(', line=1, column=16), Token(type='LOG', value='print', line=1, column=17), Token(type='LPAR', value='(', line=1, column=22), Token(type='NUMBER', value='5', line=1, column=23), Token(type='RPAR', value=')', line=1, column=24), Token(type='RPAR', value=')', line=1, column=25), Token(type='NEWLINE', value='\n', line=2, column=26)],
    [Token(type='FUNC', value='math.sin', line=1, column=0), Token(type='LPAR', value='(', line=1, column=8), Token(type='NUMBER', value='5', line=1, column=9), Token(type='NEWLINE',
                                                                                                                                                                       value='\n', line=2, column=10)],
    [Token(type='BLOCK', value='while', line=1, column=0), Token(type='COLON', value=':', line=1, column=5), Token(
        type='NUMBER', value='6', line=1, column=7), Token(type='NEWLINE', value='\n', line=2, column=8)],
    [Token(type='BLOCK', value='if', line=1, column=0), Token(type='NUMBER', value='5', line=1, column=3), Token(type='OPERATOR', value='>', line=1, column=5), Token(type='NUMBER', value='0', line=1, column=7), Token(type='COLON', value=':', line=1, column=8), Token(
        type='LOG', value='print', line=1, column=10), Token(type='LPAR', value='(', line=1, column=15), Token(type='NUMBER', value='6', line=1, column=16), Token(type='RPAR', value=')', line=1, column=17), Token(type='NEWLINE', value='\n', line=2, column=18)],
    [Token(type='VARIABLE', value='b', line=1, column=0), Token(type='OPERATOR', value='+', line=1, column=2), Token(type='LPAR', value='(', line=1, column=4), Token(type='VARIABLE',
                                                                                                                                                                      value='a', line=1, column=5), Token(type='OPERATOR', value='-', line=1, column=7), Token(type='LPAR', value='(', line=1, column=9), Token(type='NUMBER', value='7', line=1, column=10), Token(type='RPAR', value=')', line=1, column=11), Token(type='NEWLINE', value='\n', line=2, column=12)],
]

input_output = [
    ([Token(type='VARIABLE', value='a', line=1, column=0), Token(type='ASSIGN', value='=', line=1, column=2), Token(
        type='NUMBER', value='5', line=1, column=4), Token(type='NEWLINE', value='\n', line=2, column=5)],
        '''ASSIGN =\n-VARIABLE a\n-NUMBER 5\n'''),
    ([Token(type='BLOCK', value='while', line=1, column=0), Token(type='BOOL', value='True', line=1, column=6), Token(type='COLON', value=':', line=1, column=10), Token(type='NEWLINE', value='\n', line=2, column=11), Token(type='TAB', value='\t', line=2, column=0), Token(type='LOG', value='print', line=2, column=1), Token(type='LPAR', value='(', line=2, column=6), Token(type='NUMBER', value='1', line=2, column=7), Token(
        type='OPERATOR', value='+', line=2, column=9), Token(type='NUMBER', value='2', line=2, column=11), Token(type='OPERATOR', value='*', line=2, column=13), Token(type='NUMBER', value='7', line=2, column=15), Token(type='RPAR', value=')', line=2, column=16), Token(type='NEWLINE', value='\n', line=3, column=17)], '''BLOCK while\nSTATE\n-BOOL True\nBODY\n-LOG print\n--OPERATOR *\n---OPERATOR +\n----NUMBER 1\n----NUMBER 2\n---NUMBER 7\n'''),
    ([Token(type='VARIABLE', value='a', line=1, column=0), Token(type='ASSIGN', value='=', line=1, column=2), Token(type='FUNC', value='math.sin', line=1, column=4), Token(type='LPAR', value='(',
     line=1, column=12), Token(type='NUMBER', value='0', line=1, column=13), Token(type='RPAR', value=')', line=1, column=14), Token(type='NEWLINE', value='\n', line=2, column=15)], '''ASSIGN =\n-VARIABLE a\n-FUNC math.sin\n--NUMBER 0\n'''),
    ([Token(type='VARIABLE', value='b', line=1, column=0), Token(type='ASSIGN', value='=', line=1, column=2), Token(type='NUMBER', value='8', line=1, column=4), Token(type='NEWLINE', value='\n', line=2, column=5), Token(type='BLOCK', value='if', line=2, column=0), Token(type='VARIABLE', value='b', line=2, column=3), Token(type='OPERATOR', value='and', line=2,
                                                                                                                                                                                                                                                                                                                                    column=5), Token(type='NUMBER', value='4', line=2, column=9), Token(type='COLON', value=':', line=2, column=10), Token(type='NEWLINE', value='\n', line=3, column=11), Token(type='TAB', value='\t', line=3, column=0), Token(type='VARIABLE', value='b', line=3, column=1), Token(type='ASSIGN', value='=', line=3, column=3), Token(type='VARIABLE', value='b', line=3, column=5), Token(type='OPERATOR', value='-', line=3, column=7), Token(type='NUMBER', value='1', line=3, column=9), Token(type='NEWLINE', value='\n', line=4, column=10), Token(type='BLOCK', value='else', line=4, column=0), Token(type='COLON', value=':', line=4, column=4), Token(type='NEWLINE', value='\n', line=5, column=5), Token(type='TAB', value='\t', line=5, column=0), Token(type='VARIABLE', value='c', line=5, column=1), Token(type='ASSIGN', value='=', line=5, column=3), Token(type='VARIABLE', value='b', line=5, column=5), Token(type='OPERATOR', value='-', line=5, column=7), Token(type='NUMBER', value='2', line=5, column=9), Token(type='NEWLINE', value='\n', line=6, column=10)], '''ASSIGN =\n-VARIABLE b\n-NUMBER 8\nBLOCK if\nSTATE\n-OPERATOR and\n--VARIABLE b\n--NUMBER 4\nBODY\n-ASSIGN =\n--VARIABLE b\n--OPERATOR -\n---VARIABLE b\n---NUMBER 1\nBLOCK else\nBODY\n-ASSIGN =\n--VARIABLE c\n--OPERATOR -\n---VARIABLE b\n---NUMBER 2\n'''),
    ([Token(type='NUMBER', value='5', line=1, column=0), Token(type='OPERATOR', value='or', line=1, column=2), Token(type='NUMBER', value='7', line=1, column=5), Token(type='NEWLINE',
                                                                                                                                                                        value='\n', line=2, column=6)], '''OPERATOR or\n-NUMBER 5\n-NUMBER 7\n'''),
    ([Token(type='NUMBER', value='-5.896', line=1, column=0),
     Token(type='NEWLINE', value='\n', line=2, column=6)], '''NUMBER -5.896\n'''),
]


class TestSyntaxer(unittest.TestCase):

    def test_unexpected_token(self):
        for tokens in unexpected_token:
            with self.assertRaises(SyntaxError):
                SyntaxAnalyzer(tokens).parse()

    def test_input_output(self):
        for input, output in input_output:
            analyzer = SyntaxAnalyzer(input)
            syntaxTree = analyzer.parse()
            textTree = analyzer.getTextTree(syntaxTree)
            self.assertEqual(textTree, output)


if __name__ == '__main__':
    unittest.main()
