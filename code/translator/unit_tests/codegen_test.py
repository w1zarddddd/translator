import unittest
import sys
import os

sys.path.append(os.path.join(os.getcwd(), 'code/translator'))

from nodes import *
from lexer import Token
from codegen import CodeGenerator

assignment_tree = StatementNode()
assignment_tree.addNode(BinOperatorNode(Token(type='ASSIGN', value='=', line=1, column=2), ValueNode(Token(type='VARIABLE', value='a', line=1, column=0)), BinOperatorNode(
    Token(type='OPERATOR', value='+', line=1, column=6), ValueNode(Token(type='NUMBER', value='2', line=1, column=4)), ValueNode(Token(type='NUMBER', value='6', line=1, column=8)))))

assignment = (assignment_tree, '''let a;\na = 2 + 6;\n''')

while_tree = StatementNode()
block_node1 = BlockNode(Token(type='BLOCK', value='while', line=1, column=0), ValueNode(
    Token(type='BOOL', value='True', line=1, column=6)))
block_node2 = UnarOperatorNode(Token(type='LOG', value='print', line=2, column=1), ValueNode(
    Token(type='NUMBER', value='1', line=2, column=7)))
block_node1.addNode(block_node2)
while_tree.addNode(block_node1)

while_block = (while_tree, '''while (true) {\n\tconsole.log(1);\n}\n''')


class TestSemAnalyzer(unittest.TestCase):

    def test_assignment(self):
        syntaxTree, output = assignment
        self.assertEqual(CodeGenerator().genJavaScript(syntaxTree), output)

    def test_while_block(self):
        syntaxTree, output = while_block
        self.assertEqual(CodeGenerator().genJavaScript(syntaxTree), output)


if __name__ == '__main__':
    unittest.main()
