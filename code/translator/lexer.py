from typing import NamedTuple
import re

class Token(NamedTuple):
    type: str
    value: str
    line: int
    column: int

TOKEN_SPECIFICATION = [
    ('PROGRAM',      r'program\b'),
    ('VAR',          r'var\b'),
    ('INTEGER',      r'integer\b'),
    ('STRING_TYPE',  r'string\b'),
    ('BEGIN',        r'begin\b'),
    ('END',          r'end\b'),
    ('IF',           r'if\b'),
    ('THEN',         r'then\b'),
    ('ELSE',         r'else\b'),
    ('WHILE',        r'while\b'),
    ('DO',           r'do\b'),
    ('WRITELN',      r'writeln\b'),
    ('ASSIGN',       r':='),
    ('COLON',        r':'),
    ('SEMICOLON',    r';'),
    ('COMMA',        r','),
    ('LPAR',         r'\('),
    ('RPAR',         r'\)'),
    ('OPERATOR',     r'[+\-*/]|==|!=|<=|>=|<|>|and|or'),
    ('NUMBER',       r'-?\d+'),
    ('STRING',       r"'.*?'"),
    ('IDENTIFIER',   r'[a-zA-Z_][a-zA-Z0-9_]*'),  # Идентификаторы Pascal
    ('SKIP',         r'[\s\t\n\r]+'),
    ('DOT', r'\.'),
    ('MISMATCH',     r'.'),
]

def tokenize(code: str) -> list[Token]:
    tokens = []
    tok_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in TOKEN_SPECIFICATION)
    line_num = 1
    line_start = 0

    for mo in re.finditer(tok_regex, code, re.IGNORECASE):
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start

        if kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise SyntaxError(f"Недопустимый символ '{value}' на строке {line_num}")
        elif kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
        else:
            # Проверка на зарезервированные слова Go (например, 'package', 'import')
            if kind == 'IDENTIFIER' and value.lower() in {'package', 'import', 'func'}:
                raise NameError(f"Использование зарезервированного слова Go: '{value}'")
            tokens.append(Token(kind, value, line_num, column))

    return tokens