from ..command import Command
from .. import register_command
from typing import override
from ...utils.formula_parser import FormulaParser
from ...utils.format_checker import FormatChecker
from ...memory import TypeRegistry


@register_command("let")
class LetCommand(Command):
    """使用let命令声明一个变量"""
    @override
    def execute(self):
        if not self.args:
            raise TypeError('Missing parameters')
        arg = ''.join(self.args)
        eq_index = arg.find('=')
        if eq_index == -1:
            arg_name = arg
        else:
            arg_name = arg[:eq_index].strip()
        if not FormatChecker.is_valid_variable_name(arg_name):
            raise NameError('Invalid variable name')
        if eq_index == -1:
            self.script.variables.declare(arg_name, TypeRegistry.get_type("null"))
            return
        result = FormulaParser.evaluate_expression(arg[eq_index+1:], self.script.variables)
        self.script.variables.declare(arg_name, result)
        
