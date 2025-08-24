from core.memory import TypeRegistry

Num = TypeRegistry.get_type("number")
Bool = TypeRegistry.get_type("boolean")
String = TypeRegistry.get_type("string")

a = Num(5)
b = Bool(True)
c = String('114')
d = String('224')

print((b+a).value)
print((a+b).value)
print((b<a).value)
print((c+d).value)

from core.utils.formula_parser import FormulaParser
from core.memory.variable_system import VariableTable
table = VariableTable()

table.declare('c', c)
table.declare('d', d)

print(FormulaParser.evaluate_expression('c + d', table).value)