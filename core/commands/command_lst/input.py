from ..command import Command
from .. import register_command
from typing import override
from ...utils.formula_parser import FormulaParser
from ...memory import TypeRegistry

@register_command("input")
class InputCommand(Command):
    """获取输入"""
    input_method = ['text', 'case']

    @override
    def execute(self):
        if not self.args:
            raise TypeError('Missing parameters')
        if self.args[0] not in self.input_method:
            raise AttributeError(f'{self.args} is not a option for input, use "text" or "case".')
        if self.args[0] == 'text':
            if self.script.input_area == '':
                self._exec_text()
            else:
                self._call_back_text()
        elif self.args[0] == 'case':
            raise NotImplementedError
        self.script.clear_input()
    def _exec_text(self):
        self.script.status = 'AWAIT'
#        print('in exec', self.script.index)
        if len(self.args) == 3:
            self.script.input_request_message = FormulaParser.parse_value(self.args[2])
        if len(self.args) <= 1 or len(self.args) >= 4:
            raise AttributeError(f'get {len(self.args)} parameters for input, expect 1 or 2')
        varible_name = self.args[1]
        if not self.script.variables.value_exist(varible_name):
            raise NameError(f'Name {varible_name} is not declared in this scope.')
        self._moveback_index_til_command()
#        print(self.script.index, 'after')

    def _call_back_text(self):
        value = self.script.get_input()
        self.script.variables.assign(self.args[1], TypeRegistry.get_type('string')(value))

    def _moveback_index_til_command(self):
        self.script.index -= 1
        while(self.script.index >= 0 and not self.script.check_is_left_wrapper()):
            self.script.index -= 1
        # self.script.index -= 1