from ..command import Command
from .. import register_command
from typing import override
from ...utils.formula_parser import FormulaParser

@register_command("set")
class SetCommand(Command):
    """使用let命令声明（并赋值）一个变量"""
    @override
    def execute(self):
        if not self.args:
            raise TypeError('Missing parameters')
        arg = ''.join(self.args)
        eq_index = arg.find('=')
        if eq_index == -1:
            raise TypeError('Invalid parameters')
        arg_name = arg[:eq_index].strip()
        if not self.script.variables.value_exist(arg_name):
            raise NameError(f'Name {arg_name} is not declared in this scope.')
        result = FormulaParser.evaluate_expression(arg[eq_index+1:], self.script.variables)
        self.script.variables.assign(arg_name, result)
