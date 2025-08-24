from ..object import CattcaObject
from .. import TypeRegistry
from typing import override

@TypeRegistry.register("null")
class CattcaNull(CattcaObject):
    def __init__(self):
        super().__init__("null", None)