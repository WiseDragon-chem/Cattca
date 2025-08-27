from ..command import Command
from .. import register_command
from typing import override

@register_command("pass")
class PassCommand(Command):
    """静默处理"""
    @override
    def execute(self):
        if self.args:
            raise AttributeError('Invalid parameters for pass.')
        return