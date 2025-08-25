from ..command import Command
from .. import register_command
from typing import override

@register_command("label")
class LabelCommand(Command):
    """label 命令，用于标记 goto 的位置"""
    @override
    def execute(self):
        if not len(self.args) == 1:
            raise TypeError(f'get {len(self.args)} label{"s" if len(self.args) > 1 else ""}, expect 1')
            return
        self.script.labels.add_label(self.args[0], self.script.index)