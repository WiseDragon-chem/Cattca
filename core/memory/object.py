class CattcaObject:
    def __init__(self, type_name, value=None):
        self.type = type_name
        self.value = value
        self.attributes = {}
        self.methods = {}
    
    def __eq__(self, value):
        from . import TypeRegistry
        return TypeRegistry.get_type('boolean')(self.value == value.value)
    
    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f'<{self.type} Object: {self.value}>'
    
    def get_type(self):
        return self.type

    def get_value(self):
        return self.value
    
    def set_value(self, value):
        self.value = value

    def set_attribute(self, name, value):
        self.attributes[name] = value

    def get_attribute(self, name):
        if not name in self.attributes:
            raise AttributeError(f'{self.type}.{name} not exist')
        return self.attributes[name]
    
    def has_attribute(self, name):
        return name in self.attributes
    
    def set_method(self, name, method):
        self.methods[name] = method

    def get_method(self, name, method):
        if not name in self.methods:
            raise AttributeError(f'{self.type}.{name} not exist')
        return self.methods[name]
    
    @property
    def is_true(self) -> bool:
        if self.type == 'null':
            return False
        elif self.type == 'boolean':
            return self.value
        elif self.type == 'number':
            return self.value != 0
        elif self.type == 'string':
            return self.value != ''
        else:
            return True