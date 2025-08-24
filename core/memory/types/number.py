from ..object import CattcaObject
from .. import TypeRegistry
from typing import override

@TypeRegistry.register("number")
class CattcaNumber(CattcaObject):
    def __init__(self, value: int):
        if not isinstance(value, int):
            raise ValueError(f'value {value} is not an number')
        super().__init__("number", value)

    def __add__(self, other: CattcaObject):
        from .boolean import CattcaBoolean
        if not isinstance(other, CattcaObject):
            return NotImplemented
        if other.type == "number" or other.type == "boolean":
            return CattcaNumber(self.value + other.value)
        else:
            raise TypeError(f'{other.type} can not be added with a number')

    def __lt__(self, other: CattcaObject):
        from .boolean import CattcaBoolean
        if not isinstance(other, CattcaObject):
            return NotImplemented
        if other.type == "number" or other.type == "boolean":
            return CattcaBoolean(self.value < other.value)
        else:
            raise TypeError(f'{other.type} can not compare with {self.type}')
