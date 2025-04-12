from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

from SimpleLexer import SimpleLexer
from SimpleParser import SimpleParser

class VerboseErrorListener(ErrorListener):
    def __init__(self):
        super(VerboseErrorListener, self).__init__()
        self.hubo_error = False

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.hubo_error = True
        print(f"❌ Error de sintaxis en línea {line}, columna {column}: {msg}")

def parse_input(input_text):
    input_stream = InputStream(input_text)
    lexer = SimpleLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = SimpleParser(tokens)

    error_listener = VerboseErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    try:
        tree = parser.prog()
        if error_listener.hubo_error:
            print("❌ Entrada no válida por errores de sintaxis.")
        else:
            print("✅ Entrada válida.")
    except Exception as e:
        print("❌ Excepción atrapada:", str(e))

if __name__ == "__main__":
    print("=== Entrada válida ===")
    parse_input("class A { int x; }")

    print("\n=== Entrada con error 1 ===")
    parse_input("class B { int f(x) { a = 3 4 5; } }")

    print("\n=== Entrada con error 2 ===")
    parse_input("class C { int f(x) { a = 3 + ; } }")
