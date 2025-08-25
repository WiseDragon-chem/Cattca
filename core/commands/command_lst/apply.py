from ..command import Command
from .. import register_command
from typing import override
from ...utils.formula_parser import FormulaParser

@register_command("apply")
class ApplyCommand(Command):
    """将字符串添加到output中"""
    @override
    def execute(self):
        if not self.args:
            raise TypeError('Missing parameters')
            return
        return FormulaParser.evaluate_expression(" ".join(self.args), self.script.variables)