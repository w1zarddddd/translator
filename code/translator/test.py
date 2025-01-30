import lexer
import syntaxer
import semanalyzer
import codegen

code = '''while True:\n\tprint(1)'''


tokens = lexer.tokenize(code)
print('\n'.join(map(str, tokens)))

analyzer = syntaxer.SyntaxAnalyzer(tokens)
syntaxTree = analyzer.parse()
textTree = analyzer.getTextTree(syntaxTree)
print(textTree)

semanalyzer.SemanticAnalyzer().check(syntaxTree)

output = codegen.CodeGenerator().genJavaScript(syntaxTree)
print(output)
