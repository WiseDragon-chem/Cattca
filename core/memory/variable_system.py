from . import TypeRegistry
from .object import CattcaObject

class DynamicVariableSystem:

    @staticmethod
    def create_object(value) -> CattcaObject:
        if value is None:
            return TypeRegistry.get_type('null')()
        elif isinstance(value, bool):
            return TypeRegistry.get_type('boolean')(value)
        elif isinstance(value, int):
            return TypeRegistry.get_type('number')(value)
        elif isinstance(value, str):
            return TypeRegistry.get_type('string')(value)
        else:
            return CattcaObject('object', value=value)
    
    @staticmethod
    def is_true(obj: CattcaObject) -> bool:
        if obj.type == 'null':
            return False
        elif obj.type == 'boolean':
            return obj.value
        elif obj.type == 'number':
            return obj.value != 0
        elif obj.type == 'string':
            return obj.value != ''
        else:
            return True

class VariableTable:
    def __init__(self):
        self.scopes: dict[str, CattcaObject] = [{}] # 初始全局作用域, scopes[-1]表示当前作用域

    def enter_scope(self):
        '''进入一个作用域'''
        self.scopes.append({})

    def exit_scope(self):
        """退出当前作用域"""
        if len(self.scopes) > 1:
            self.scopes.pop()     # 移除最后一个作用域
        else:
            raise Exception("Cannot exit global scope")
    
    def get_current_scope(self) -> dict[str, CattcaObject]:
        return self.scopes[-1]
    
    def get_scopes_depth(self) -> int:
        return len(self.scopes)
    
    def declare(self, name: str, value: CattcaObject):
        '''声明并赋值一个变量'''
        if name in self.scopes[-1]:
            raise Exception(f'variable {name} already exists!')
        self.scopes[-1][name] = value
    
    def assign(self, name: str, value: CattcaObject):
        '''赋值一个变量'''
        for scope in reversed(self.scopes):
            if name in scope:
                scope[name].value = value
                return
                
        raise Exception(f"variable {name} hasn't declared!")

    def get_value(self, name: str) -> CattcaObject:
        '''获取一个变量的值'''
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name].value
        
        raise Exception(f"variable {name} hasn't declared!")
    
    def value_exist(self, name: str) -> bool:
        '''判断一个变量是否存在'''
        for scope in reversed(self.scopes):
            if name in scope:
                return True
        return False


