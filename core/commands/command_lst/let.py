from ..command import Command
from .. import register_command
from typing import override
from ...utils.formula_parser import FormulaParser
from ...utils.format_checker import FormatChecker


@register_command("let")
class SayCommand(Command):
    """使用let命令声明（并赋值）一个变量"""
    @override
    def execute(self):
        if not self.args:
            raise TypeError('Missing parameters')
        arg = ''.join(self.args)
        arg = arg.split('=')
        if len(arg) != 2:
            raise TypeError('Invalid parameters')
        result = FormulaParser.evaluate_expression(arg[1], self.script.variables)
        arg[0] = arg[0].strip()
        if not FormatChecker.is_valid_variable_name(arg[0]):
            raise NameError('Invalid variable name')
        self.script.variables.declare(arg[0], result)
        
