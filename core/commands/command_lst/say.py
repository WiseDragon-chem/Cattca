from ..command import Command
from .. import register_command
from typing import override

@register_command("say")
class SayCommand(Command):
    """一个简单的 'say' 命令，用于打印文本。"""
    @override
    def execute(self):
        if not self.args:
            raise ValueError('Missing parameters')
            return
        print(" ".join(self.args))