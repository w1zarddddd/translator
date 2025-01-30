import unittest
import sys
import os

sys.path.append(os.path.join(os.getcwd(), 'code/translator'))

from lexer import tokenize, Token

unsupported_token = '$[]{^}\|&?;%@!`~'

reserved_name = [
    '''a = true''',
    '''a = false''',
    '''Math.sin(6)''',
    '''console = 9''',
    '''let = console''',
]

input_output = [
    ('''a = 5''', [Token(type='VARIABLE', value='a', line=1, column=0), Token(type='ASSIGN', value='=', line=1, column=2), Token(
        type='NUMBER', value='5', line=1, column=4), Token(type='NEWLINE', value='\n', line=2, column=5)]),
    ('''while True:\n\tprint(1 + 2 * 7)''', [Token(type='BLOCK', value='while', line=1, column=0), Token(type='BOOL', value='True', line=1, column=6), Token(type='COLON', value=':', line=1, column=10), Token(type='NEWLINE', value='\n', line=2, column=11), Token(type='TAB', value='\t', line=2, column=0), Token(type='LOG', value='print', line=2, column=1), Token(type='LPAR', value='(',
     line=2, column=6), Token(type='NUMBER', value='1', line=2, column=7), Token(type='OPERATOR', value='+', line=2, column=9), Token(type='NUMBER', value='2', line=2, column=11), Token(type='OPERATOR', value='*', line=2, column=13), Token(type='NUMBER', value='7', line=2, column=15), Token(type='RPAR', value=')', line=2, column=16), Token(type='NEWLINE', value='\n', line=3, column=17)]),
    ('''a = math.sin(0)''', [Token(type='VARIABLE', value='a', line=1, column=0), Token(type='ASSIGN', value='=', line=1, column=2), Token(type='FUNC', value='math.sin', line=1, column=4), Token(
        type='LPAR', value='(', line=1, column=12), Token(type='NUMBER', value='0', line=1, column=13), Token(type='RPAR', value=')', line=1, column=14), Token(type='NEWLINE', value='\n', line=2, column=15)]),
    ('''b = 8\nif b and 4:\n\tb = b - 1\nelse:\n\tc = b - 2''', [Token(type='VARIABLE', value='b', line=1, column=0), Token(type='ASSIGN', value='=', line=1, column=2), Token(type='NUMBER', value='8', line=1, column=4), Token(type='NEWLINE', value='\n', line=2, column=5), Token(type='BLOCK', value='if', line=2, column=0), Token(type='VARIABLE', value='b', line=2, column=3), Token(type='OPERATOR', value='and', line=2,
                                                                                                                                                                                                                                                                                                                                                                                               column=5), Token(type='NUMBER', value='4', line=2, column=9), Token(type='COLON', value=':', line=2, column=10), Token(type='NEWLINE', value='\n', line=3, column=11), Token(type='TAB', value='\t', line=3, column=0), Token(type='VARIABLE', value='b', line=3, column=1), Token(type='ASSIGN', value='=', line=3, column=3), Token(type='VARIABLE', value='b', line=3, column=5), Token(type='OPERATOR', value='-', line=3, column=7), Token(type='NUMBER', value='1', line=3, column=9), Token(type='NEWLINE', value='\n', line=4, column=10), Token(type='BLOCK', value='else', line=4, column=0), Token(type='COLON', value=':', line=4, column=4), Token(type='NEWLINE', value='\n', line=5, column=5), Token(type='TAB', value='\t', line=5, column=0), Token(type='VARIABLE', value='c', line=5, column=1), Token(type='ASSIGN', value='=', line=5, column=3), Token(type='VARIABLE', value='b', line=5, column=5), Token(type='OPERATOR', value='-', line=5, column=7), Token(type='NUMBER', value='2', line=5, column=9), Token(type='NEWLINE', value='\n', line=6, column=10)]),
    ('''5 or 7''', [Token(type='NUMBER', value='5', line=1, column=0), Token(type='OPERATOR', value='or', line=1, column=2), Token(type='NUMBER', value='7', line=1, column=5), Token(type='NEWLINE',
                                                                                                                                                                                      value='\n', line=2, column=6)]),
    ('''-5.896''', [Token(type='NUMBER', value='-5.896', line=1,
     column=0), Token(type='NEWLINE', value='\n', line=2, column=6)]),
]


class TestLexer(unittest.TestCase):

    def test_unsupported_token(self):
        for token in list(unsupported_token):
            with self.assertRaises(SyntaxError):
                tokenize(token)

    def test_reserved_name(self):
        for code in reserved_name:
            with self.assertRaises(NameError):
                tokenize(code)

    def test_input_output(self):
        for input, output in input_output:
            self.assertEqual(tokenize(input), output)


if __name__ == '__main__':
    unittest.main()
