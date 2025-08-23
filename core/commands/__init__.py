import pkgutil
from typing import Dict, Type
from .command import Command

# 命令注册表 (Command Registry)
# 键是命令名 (str)，值是命令类 (Command Class)
COMMANDS: Dict[str, Type[Command]] = {}

def register_command(name: str):
    """一个用于注册命令类的装饰器 (A decorator to register command classes)."""
    def decorator(cls: Type[Command]):
        if not issubclass(cls, Command):
            raise TypeError(f"Class {cls.__name__} is not a subclass of Command")
        COMMANDS[name] = cls
        return cls
    return decorator

def _load_commands():
    """
    动态加载所有命令模块以触发注册
    (Dynamically load all command modules to trigger registration).
    """
    # 导入目标子包，并专门从该子包加载命令
    from . import command_lst

    pkg_path = command_lst.__path__
    pkg_name = command_lst.__name__
    
    for _, name, _ in pkgutil.walk_packages(pkg_path, prefix=f"{pkg_name}."):
        __import__(name, fromlist=[""])

# 在包被导入时自动加载所有命令
_load_commands()