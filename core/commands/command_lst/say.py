from ..command import Command
from .. import register_command
from typing import override
from ...exceptions import *

@register_command("say")
class SayCommand(Command):
    """一个简单的 'say' 命令，用于打印文本。"""
    @override
    def execute(self):
        if not self.args:
            raise CattcaTypeError('Missing parameters')
        print(" ".join(self.args))