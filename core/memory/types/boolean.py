from ..object import CattcaObject
from .. import TypeRegistry
from typing import override

@TypeRegistry.register("boolean")
class CattcaBoolean(CattcaObject):
    def __init__(self, value: bool):
        super().__init__("number", value)

    def __add__(self, other: CattcaObject):
        from .number import CattcaNumber
        temp_number = CattcaNumber(int(self.value))
        return temp_number + other

    def __lt__(self, other: CattcaObject):
        if not isinstance(other, CattcaObject):
            return NotImplemented
        if other.type == "number":
            return self.value < other.value