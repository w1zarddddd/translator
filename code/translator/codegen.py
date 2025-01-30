from lexer import Token
from nodes import *

toGo = {
    'writeln': 'fmt.Println',
    'integer': 'int',
    'string': 'string',
    'and': '&&',
    'or': '||',
    ':=': '=',
}

MARGIN = '\t'


class CodeGenerator:
    def __init__(self) -> None:
        self.output = ''
        self.variables = set()
        self.needs_fmt_import = False  # Для автоматического добавления import "fmt"

    def genVarDeclaration(self, node)   -> str:
        decls = []
        for var_name, var_type in node.declarations:
            decls.append(f'var {var_name} {toGo.get(var_type, var_type)}')
        return '\n'.join(decls) + '\n'

    def genProcedureCall(self, node) -> str:
        self.needs_fmt_import = True
        args = ', '.join(self.genCode(arg) for arg in node.args)
        return f'fmt.Println({args})'

    def genBinOperator(self, node) -> str:
        if node.operator.type == 'ASSIGN':
            return f'{self.genCode(node.leftNode)} {toGo[node.operator.value]} {self.genCode(node.rightNode)}'
        return f'{self.genCode(node.leftNode)} {node.operator.value} {self.genCode(node.rightNode)}'

    def genBlock(self, node) -> str:
        code = '{\n'
        for stmt in node.body:
            code += self.genCode(stmt) + '\n'
        return code + '}'

    def genCode(self, node, level=0) -> str:
        if isinstance(node, VarDeclarationNode):
            return self.genVarDeclaration(node)

        elif isinstance(node, ProcedureCallNode):
            return MARGIN * level + self.genProcedureCall(node)

        elif isinstance(node, BinOperatorNode):
            return MARGIN * level + self.genBinOperator(node) + ';'

        elif isinstance(node, BlockNode):
            return MARGIN * level + f'if {self.genCode(node.statement)} ' + self.genBlock(node)

        elif isinstance(node, ValueNode):
            return node.value.value

        elif isinstance(node, BlockNode) and node.operator == 'while':
            condition = self.genCode(node.statement, level)
            code = MARGIN * level + f'for {condition} {{\n'
            for stmt in node.body:
                code += self.genCode(stmt, level + 1) + '\n'
            return code + MARGIN * level + '}'

        elif isinstance(node, BlockNode) and node.operator == 'if':
            condition = self.genCode(node.statement, level)
            code = MARGIN * level + f'if {condition} {{\n'
            for stmt in node.body:
                if isinstance(stmt, ElseNode):
                    continue  # Обрабатываем ELSE отдельно
                code += self.genCode(stmt, level + 1) + '\n'
            code += MARGIN * level + '}'

            # Добавляем ELSE
            for stmt in node.body:
                if isinstance(stmt, ElseNode):
                    code += ' else {\n'
                    for else_stmt in stmt.body:
                        code += self.genCode(else_stmt, level + 1) + '\n'
                    code += MARGIN * level + '}'
            return code

        elif isinstance(node, ElseNode):
            return ''  # Уже обработано в BlockNode

    def genProcedureCall(self, node) -> str:
        args = []
        for arg in node.args:
            if isinstance(arg, ValueNode) and arg.value.type == 'STRING':
                # Замена ' на " и экранирование
                arg_str = arg.value.value.replace("'", "\"")
                args.append(f'"{arg_str[1:-1]}"')
            else:
                args.append(self.genCode(arg))
        return f'fmt.Println({", ".join(args)})'

    def generate(self, root) -> str:
        # Добавляем заголовок пакета и импорты
        self.output = 'package main\n\n'
        if self.needs_fmt_import:
            self.output += 'import "fmt"\n\n'

         # Генерируем функцию main
            self.output += 'func main() {\n'
        for node in root.codeStrings:
            self.output += self.genCode(node, level=1) + '\n'
            self.output += '}'
        return self.output

        # Генерируем основной код
        for node in root.codeStrings:
            self.output += self.genCode(node) + '\n'

        return self.output
