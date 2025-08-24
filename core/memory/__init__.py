import pkgutil
from typing import Dict, Type
from .object import CattcaObject

class TypeRegistry:
    _types: Dict[str, Type[CattcaObject]] = {}
    
    @classmethod
    def register(cls, cattca_type: str):
        def decorator(type_class: Type[CattcaObject]):
            if not issubclass(type_class, CattcaObject):
                raise TypeError(f'Class {type_class.__name__} is not a subclass of CattcaObject')
            cls._types[cattca_type] = type_class
            return type_class
        return decorator
    
    @classmethod
    def get_type(cls, type_name: str) -> Type[CattcaObject]:
        return cls._types.get(type_name)
    
    @classmethod
    def get_all_types(cls) -> Dict[str, Type[CattcaObject]]:
        return cls._types.copy()
    
def _load_types():
    from . import types
    
    pkg_path = types.__path__
    pkg_name = types.__name__

    for _, name, _ in pkgutil.walk_packages(pkg_path, prefix=f'{pkg_name}.'):
        __import__(name, fromlist=[''])

_load_types()