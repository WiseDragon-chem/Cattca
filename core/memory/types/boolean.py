from ..object import CattcaObject
from .. import TypeRegistry
from typing import override

@TypeRegistry.register("boolean")
class CattcaBoolean(CattcaObject):
    def __init__(self, value: bool):
        super().__init__("boolean", value)

    def to_number(self):
        from .number import CattcaNumber
        temp_number = CattcaNumber(int(self.value))
        return temp_number
    
    @override
    def __str__(self):
        return 'true' if self.value else 'false'
    
    def __add__(self, other: CattcaObject):
        return self.to_number() + other

    def __lt__(self, other: CattcaObject):
        return self.to_number() < other