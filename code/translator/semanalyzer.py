from lexer import Token
from nodes import *


class SemanticAnalyzer:
    def __init__(self) -> None:
        self.variables = {}  # Словарь: имя → тип
        self.current_scope = "global"
        self.in_loop = False  # Для проверки break/continue внутри циклов

    def check_program(self, root: StatementNode):
        for node in root.codeStrings:
            self.check_node(node)

    def check_node(self, node: ExpressionNode):
        if isinstance(node, VarDeclarationNode):
            self.check_var_declaration(node)

        elif isinstance(node, BinOperatorNode):
            if node.operator.type == 'ASSIGN':
                self.check_assignment(node)
            else:
                self.check_expression(node)

        elif isinstance(node, BlockNode):
            if node.operator == 'if':
                self.check_condition(node.statement)
                for stmt in node.body:
                    self.check_node(stmt)

            elif node.operator == 'while':
                self.check_condition(node.statement)
                self.in_loop = True
                for stmt in node.body:
                    self.check_node(stmt)
                self.in_loop = False

        elif isinstance(node, ProcedureCallNode):
            if node.name == 'writeln':
                for arg in node.args:
                    self.check_expression(arg)
                    self.check_expression(arg)

        # ... другие типы узлов

    def check_expression(self, node: ExpressionNode) -> None:
        """Проверка семантики выражений."""
        if isinstance(node, BinOperatorNode):
            left_type = self.infer_type(node.leftNode)
            right_type = self.infer_type(node.rightNode)

            if node.operator.value in ['+', '-', '*', '/']:
                if left_type != 'integer' or right_type != 'integer':
                    raise TypeError(f"Арифметические операции требуют integer, получено {left_type} и {right_type}")

            elif node.operator.value in ['==', '!=', '<', '>', '<=', '>=']:
                if left_type != right_type:
                    raise TypeError(f"Сравнение {left_type} и {right_type} невозможно")

        elif isinstance(node, ValueNode):
            if node.value.type == 'IDENTIFIER' and node.value.value not in self.variables:
                raise NameError(f"Переменная {node.value.value} не объявлена")

    def infer_type(self, node: ExpressionNode) -> str:
        """Определение типа выражения."""
        if isinstance(node, ValueNode):
            if node.value.type == 'NUMBER':
                return 'integer'
            elif node.value.type == 'STRING':
                return 'string'
            elif node.value.type == 'IDENTIFIER':
                return self.variables.get(node.value.value, 'unknown')
        return 'unknown'

    def check_var_declaration(self, node: VarDeclarationNode):
        for var_name, var_type in node.declarations:
            if var_name in self.variables:
                raise NameError(f"Переменная {var_name} уже объявлена")
            self.variables[var_name] = var_type

    def check_assignment(self, node: BinOperatorNode):
        var_name = node.leftNode.value.value
        if var_name not in self.variables:
            raise NameError(f"Переменная {var_name} не объявлена")

        expr_type = self.infer_type(node.rightNode)
        expected_type = self.variables[var_name]

        if expr_type != expected_type:
            raise TypeError(f"Нельзя присвоить {expr_type} переменной типа {expected_type}")

    def check_condition(self, condition: ExpressionNode):
        cond_type = self.infer_type(condition)
        if cond_type != 'boolean':
            raise TypeError(f"Условие должно быть логическим, получено {cond_type}")

    def infer_type(self, node: ExpressionNode) -> str:
        if isinstance(node, ValueNode):
            if node.value.type == 'NUMBER':
                return 'integer'
            elif node.value.type == 'STRING':
                return 'string'
            elif node.value.type == 'IDENTIFIER':
                return self.variables.get(node.value.value, 'unknown')

        elif isinstance(node, BinOperatorNode):
            left_type = self.infer_type(node.leftNode)
            right_type = self.infer_type(node.rightNode)

            if node.operator.value in ['+', '-', '*', '/']:
                if left_type != 'integer' or right_type != 'integer':
                    raise TypeError(f"Арифметические операции требуют integer, получено {left_type} и {right_type}")
                return 'integer'

            elif node.operator.value in ['==', '!=', '<', '>']:
                if left_type != right_type:
                    raise TypeError(f"Сравнение типов {left_type} и {right_type} невозможно")
                return 'boolean'

        return 'unknown'
