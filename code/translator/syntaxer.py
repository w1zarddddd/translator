from lexer import Token
from nodes import *
from lexer import tokenize

class SyntaxAnalyzer:
    def __init__(self, tokens: list) -> None:
        self.tokens = tokens
        self.pos = 0
        self.current_token: Token = None
        self.advance()

    def advance(self) -> None:
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]
            self.pos += 1
        else:
            self.current_token = None

    def match(self, token_type: str) -> bool:
        if self.current_token and self.current_token.type == token_type:
            self.advance()
            return True
        return False

    def require(self, token_type: str) -> Token:
        if self.current_token.type == token_type:
            token = self.current_token
            self.advance()
            return token
        raise SyntaxError(f"Ожидается {token_type}, но получен {self.current_token.type}")

    def parse_program(self) -> StatementNode:
        root = StatementNode()
        self.require('PROGRAM')
        program_name = self.require('IDENTIFIER').value
        self.require('SEMICOLON')

        # Обработка секции VAR
        if self.current_token.type == 'VAR':
            var_decls = self.parse_var_declaration()
            root.addNode(VarDeclarationNode(var_decls))

        # Обработка тела программы (BEGIN...END)
        self.require('BEGIN')
        while not self.match('END'):
            stmt = self.parse_statement()
            root.addNode(stmt)
            self.require('SEMICOLON')
        self.require('DOT')
        return root

    def parse_var_declaration(self) -> list:
        self.require('VAR')
        declarations = []
        while self.current_token.type == 'IDENTIFIER':
            var_name = self.current_token.value
            self.advance()
            self.require('COLON')
            var_type = self.require('INTEGER', 'STRING_TYPE').value
            declarations.append((var_name, var_type))
            self.require('SEMICOLON')
        return declarations

    def parse_statement(self) -> ExpressionNode:
        if self.current_token.type == 'IDENTIFIER':
            # Присваивание: x := 5
            var_node = ValueNode(self.current_token)
            self.advance()
            self.require('ASSIGN')
            expr_node = self.parse_expression()
            return BinOperatorNode(Token('ASSIGN', ':=', 0, 0), var_node, expr_node)

        elif self.current_token.type == 'WRITELN':
            # Вызов writeln
            self.advance()
            self.require('LPAR')
            args = []
            while not self.match('RPAR'):
                args.append(self.parse_expression())
                if self.match('COMMA'):
                    continue
            return ProcedureCallNode('writeln', args)


        elif self.current_token.type == 'WHILE':
            self.advance()
            condition = self.parse_expression()
            self.require('DO')
            while_node = BlockNode('while', condition)
            if self.current_token.type == 'BEGIN':
                self.advance()
                while not self.match('END'):
                    while_node.addNode(self.parse_statement())
            return while_node


        elif self.current_token.type == 'IF':
            # Условный оператор IF
            self.advance()
            condition = self.parse_expression()
            self.require('THEN')
            if_node = BlockNode('if', condition)
            if self.current_token.type == 'BEGIN':
                self.advance()
                while not self.match('END'):
                    if_node.addNode(self.parse_statement())

            elif self.current_token.type == 'IF':
                self.advance()
                condition = self.parse_expression()
                self.require('THEN')
                if_node = BlockNode('if', condition)

                # Обработка блока THEN
                if self.current_token.type == 'BEGIN':
                    self.advance()
                    while not self.match('END'):
                        if_node.addNode(self.parse_statement())

                # Обработка ELSE
                if self.match('ELSE'):
                    else_node = ElseNode(Token('ELSE', 'else', 0, 0))
                    if self.current_token.type == 'BEGIN':
                        self.advance()
                        while not self.match('END'):
                            else_node.addNode(self.parse_statement())
                    if_node.body.append(else_node)

                return if_node

    def parse_term (self) -> ExpressionNode:
                if self.current_token.type == 'NUMBER':
                    node = ValueNode(self.current_token)
                    self.advance()
                    return node
                elif self.current_token.type == 'IDENTIFIER':
                    node = ValueNode(self.current_token)
                    self.advance()
                    return node
                elif self.current_token.type == 'STRING':  # Добавлено!
                    node = ValueNode(self.current_token)
                    self.advance()
                    return node
                elif self.match('LPAR'):
                    node = self.parse_expression()
                    self.require('RPAR')
                    return node
                else:
                    raise SyntaxError("Недопустимый терм")


    def parse_expression(self) -> ExpressionNode:
        node = self.parse_term()
        while self.current_token and self.current_token.type in ['OPERATOR']:
            op_token = self.current_token
            self.advance()
            node = BinOperatorNode(op_token, node, self.parse_term())
        return node

    def getTextNode(self, node: ExpressionNode, level: int = 0) -> str:
        nodeType = type(node)
        indent = '-' * level

        if nodeType == ValueNode:
            return f"{indent}ValueNode({node.value.type}: {node.value.value})\n"

        elif nodeType == BinOperatorNode:
            res = f"{indent}BinOperatorNode({node.operator.type}: {node.operator.value})\n"
            res += self.getTextNode(node.leftNode, level + 1)
            res += self.getTextNode(node.rightNode, level + 1)
            return res

        elif nodeType == BlockNode:
            res = f"{indent}BlockNode({node.operator.value})\n"
            res += f"{indent}Condition:\n"
            res += self.getTextNode(node.statement, level + 1)
            res += f"{indent}Body:\n"
            for subnode in node.body:
                res += self.getTextNode(subnode, level + 1)
            return res

        elif nodeType == VarDeclarationNode:
            res = f"{indent}VarDeclarationNode\n"
            for var_name, var_type in node.declarations:
                res += f"{indent}- {var_name}: {var_type}\n"
            return res

        elif nodeType == ProcedureCallNode:
            res = f"{indent}ProcedureCallNode({node.name})\n"
            for arg in node.args:
                res += self.getTextNode(arg, level + 1)
            return res

        else:
            return f"{indent}UnknownNode\n"

    def getTextTree(self, root: StatementNode) -> str:
        textTree = ""
        for node in root.codeStrings:
            textTree += self.getTextNode(node)
        return textTree