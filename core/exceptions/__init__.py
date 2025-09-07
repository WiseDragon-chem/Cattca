class CattcaException(Exception):

    def __init__(self, message: str):
        self.message = message
        self.error_name = self.__class__.__name__[6:]

    def __str__(self):
        return f'{self.error_name}: {self.message}'

class CattcaValueError(CattcaException):
    pass

class CattcaSyntaxError(CattcaException):
    pass

class CattcaTypeError(CattcaException):
    pass

class CattcaNameError(CattcaException):
    pass

class CattcaAttributeError(CattcaException):
    pass

class CattcaRuntimeError(CattcaException):
    pass

class CattcaExitException(CattcaException):
    """当程序执行完成时，触发该异常"""
    pass

class CattcaAwaitException(CattcaException):
    """当程序进入等待状态时(例如等待输入输出)，触发该异常"""
    pass
