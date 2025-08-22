# Error Types Table Program

from prettytable import PrettyTable

# Table object
table = PrettyTable()
table.field_names = ["Error Type", "Kab hota hai?", "Example"]

# Saare errors ko add karte hain
table.add_row(["ValueError", "Jab data wrong format me ho", "int('abc')"])
table.add_row(["TypeError", "Jab galat type ke values use kare", "'abc' + 5"])
table.add_row(["ZeroDivisionError", "Jab 0 se divide kare", "10/0"])
table.add_row(["NameError", "Jab variable define hi nahi", "print(x) (agar x banaya hi nahi)"])
table.add_row(["IndexError", "Jab list ke bahar index maange", "[1,2,3][5]"])
table.add_row(["KeyError", "Jab dictionary me galat key use kare", "{'a':1}['b']"])
table.add_row(["FileNotFoundError", "Jab file exist hi na kare", "open('abc.txt')"])
table.add_row(["PermissionError", "Jab file/resource access ka right na ho", "File read-only hone pe likhne ki koshish"])
table.add_row(["ImportError", "Jab module import nahi ho raha", "import kuchnahi"])
table.add_row(["ModuleNotFoundError", "Jab module hi nahi mil raha", "import abcdefg"])
table.add_row(["AttributeError", "Jab object ka method/attribute exist na kare", "'abc'.push()"])
table.add_row(["RuntimeError", "General runtime galti", "Kabhi kabhi libraries me hota hai"])
table.add_row(["MemoryError", "Jab memory khatam ho jaye", "Huge list banate waqt"])
table.add_row(["RecursionError", "Jab recursion limit cross ho jaye", "Function khud ko infinite call kare"])
table.add_row(["AssertionError", "Jab assert fail ho jaye", "assert 2+2==5"])
table.add_row(["IndentationError", "Jab indentation galat ho", "Galat spacing lagana"])
table.add_row(["SyntaxError", "Jab code grammar galat ho", "if True print('hi')"])
table.add_row(["OverflowError", "Jab number result bohot bada ho", "math.exp(1000)"])
table.add_row(["UnicodeError", "Jab encoding/decoding fail ho", "Wrong unicode conversion"])

# Table print karna
print("\n🔹 Python Common Errors Table 🔹\n")
print(table)
