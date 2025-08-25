from ..command import Command
from .. import register_command
from typing import override

@register_command("exit")
class ExitCommand(Command):
    """exit命令，结束当前进程"""
    @override
    def execute(self):
        if self.args:
            raise TypeError(f'get {len(self.args)} arg{"s" if len(self.args) > 1 else ""}, expect 0')
            return
        self.script.status = 'EXIT'