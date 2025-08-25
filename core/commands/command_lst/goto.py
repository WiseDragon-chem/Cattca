from ..command import Command
from .. import register_command
from typing import override

@register_command("goto")
class GotoCommand(Command):
    """goto 命令，跳转到对应的label"""
    @override
    def execute(self):
        if not len(self.args) == 1:
            raise TypeError(f'get {len(self.args)} label{"s" if len(self.args) > 1 else ""}, expect 1')
            return
        index = self.script.labels.get_index(self.args[0])
        self.script.index = index