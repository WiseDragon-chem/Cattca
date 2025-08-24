from ..object import CattcaObject
from .. import TypeRegistry
from typing import override

@TypeRegistry.register("number")
class CattcaNumber(CattcaObject):
    def __init__(self, value: int):
        if not value.is_integer:
            raise ValueError(f'value {value} is not an number')
        super().__init__("number", value)

    def __add__(self, other: CattcaObject):
        if not isinstance(other, CattcaObject):
            return NotImplemented
        if other.type == "number":
            return CattcaNumber(self.value + other.value)
        else:
            raise TypeError(f'{other.type} can not be added with a number')

    def __lt__(self, other: CattcaObject):
        if not isinstance(other, CattcaObject):
            return NotImplemented
        if other.type == "number":
            return self.value < other.value
