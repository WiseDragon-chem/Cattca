from ..object import CattcaObject
from .. import TypeRegistry
from typing import override
from ...exceptions import *

@TypeRegistry.register("string")
class CattcaString(CattcaObject):
    def __init__(self, value: str):
        super().__init__("string", value)

    def __add__(self, other: CattcaObject):
        if not isinstance(other, CattcaObject):
            return NotImplemented
        if other.type == 'string':
            return CattcaString(self.value + other.value)
        else:
            raise CattcaTypeError(f"{other.type} can not be added with a string")
    