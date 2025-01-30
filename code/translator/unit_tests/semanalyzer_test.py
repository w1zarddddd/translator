import unittest
import sys
import os

sys.path.append(os.path.join(os.getcwd(), 'code/translator'))

from semanalyzer import SemanticAnalyzer
from nodes import *
from lexer import Token

undeclared_variable_tree = StatementNode()
undeclared_variable_tree.addNode(BinOperatorNode(Token(type='ASSIGN', value='=', line=1, column=2), ValueNode(Token(type='VARIABLE', value='a', line=1, column=0)), BinOperatorNode(
    Token(type='OPERATOR', value='-', line=1, column=6), ValueNode(Token(type='VARIABLE', value='b', line=1, column=4)), ValueNode(Token(type='NUMBER', value='6', line=1, column=8)))))

unexpected_else_tree = StatementNode()
block_node1 = BlockNode(Token(type='BLOCK', value='if', line=1, column=0), ValueNode(
    Token(type='NUMBER', value='1', line=1, column=3)))
block_node2 = ElseNode(Token(type='BLOCK', value='else', line=2, column=1))
block_node2.addNode(UnarOperatorNode(Token(type='LOG', value='print', line=3,
                    column=2), ValueNode(Token(type='NUMBER', value='8', line=3, column=8))))
block_node1.addNode(block_node2)
unexpected_else_tree.addNode(block_node1)


class TestSemAnalyzer(unittest.TestCase):

    def test_undeclared_variable(self):
        with self.assertRaises(NameError):
            syntaxTree = undeclared_variable_tree
            SemanticAnalyzer().check(syntaxTree)

    def test_unexpected_else(self):
        with self.assertRaises(SyntaxError):
            syntaxTree = unexpected_else_tree
            SemanticAnalyzer().check(syntaxTree)


if __name__ == '__main__':
    unittest.main()
