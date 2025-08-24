from core.memory import TypeRegistry

Num = TypeRegistry.get_type("number")
Bool = TypeRegistry.get_type("boolean")

a = Num(5)
b = Bool(True)

print((b+a).value)