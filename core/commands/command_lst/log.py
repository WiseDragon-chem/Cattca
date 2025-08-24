from ..command import Command
from .. import register_command
from typing import override
from ...utils.formula_parser import FormulaParser

@register_command("log")
class SayCommand(Command):
    """一个简单的 'log' 命令，输出变量或表达式的值。"""
    @override
    def execute(self):
        if not self.args:
            raise TypeError('Missing parameters')
            return
        print(FormulaParser.evaluate_expression(" ".join(self.args), self.script.variables))