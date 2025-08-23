import abc
from typing import List
from ..memory.script import Script

class Command(abc.ABC):
    """命令的抽象基类 (Abstract base class for commands)."""
    def __init__(self, args: List[str], script: Script):
        self.args = args
        self.script = script

    @abc.abstractmethod
    def execute(self):
        """执行命令的抽象方法 (Abstract method to execute the command)."""
        raise NotImplementedError