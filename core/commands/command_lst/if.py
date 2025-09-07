from ..command import Command
from .. import register_command
from typing import override
from ...utils.formula_parser import FormulaParser
from ..parser import execute_line
from ...exceptions import *

@register_command("if")
class IfCommand(Command):
    """if 命令，如果条件为真，执行对应的代码"""
    @override
    def execute(self):
        if not self.args:
            raise CattcaTypeError('Missing parameters')
        arg = ' '.join(self.args)
        jump_index = arg.find('->')
        if jump_index == -1:
            raise CattcaSyntaxError('Missing jump charactor "->".')
        expression = arg[:jump_index]
        target_command  = arg[jump_index+2:]
        if len(expression) == 0:
            raise CattcaSyntaxError('Missing jump condition.')
        if FormulaParser.evaluate_expression(expression, self.script.variables).is_true:
            execute_line(target_command, self.script)
