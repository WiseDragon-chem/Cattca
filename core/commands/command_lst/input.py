from ..command import Command
from .. import register_command
from typing import override
from ...utils.formula_parser import FormulaParser
from ...memory import TypeRegistry
from ..parser import execute_line

@register_command("input")
class InputCommand(Command):
    """获取输入"""
    input_method = ['text', 'case', 'case:']

    @override
    def execute(self):
        if not self.args:
            raise TypeError('Missing parameters')
        if self.args[0] not in self.input_method:
            raise AttributeError(f'{' '.join(self.args)} is not a option for input, use "text" or "case".')
        if self.args[0] == 'text':
            if self.script.input_area == '':
                self._exec_text()
            else:
                self._call_back_text()
        elif self.args[0] == 'case' or 'case:':
            if self.script.input_area == '':
                self._exec_case()
            else:
                self._call_back_case()
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

    def _exec_case(self):
        self.script.status = 'AWAIT'
        case_detail, var_name = self._parse_case()
        self.script.input_request_message = case_detail.keys()
        # print(case_detail, _var_name)
        self._moveback_index_til_command()

    def _call_back_case(self):
        value = str(self.script.get_input())
        case_detail, var_name = self._parse_case()
        if value not in case_detail.keys():
            raise ValueError(f'"{value}" is not a option for this input case. Input {' or '.join(case_detail.keys())} instead.')
        self.script.variables.assign(var_name, TypeRegistry.get_type('string')(value))
        execute_line(case_detail[value], self.script)


    def _moveback_index_til_command(self):
        self.script.index -= 1  #必须先左移一位，不然会认为命令结尾的/>已经是指令开头了
        while(self.script.index >= 0 and not self.script.check_is_left_wrapper()):
            self.script.index -= 1
    
    def _parse_case(self) -> tuple[dict, str]:
        """解析input case，返回一个保存case内容的字典和需要储存值储存的变量名.
        字典的键：选项名称；字典的值：对应的指令；
        """
        ret = dict()
        #预处理阶段
        if ':' in self.args[0]:  
            self.args[1] = ':' + self.args[1]
        if len(self.args) < 2:
            raise AttributeError(f'Missing parameters for input case.')
        varible_name = ''
        if not ':' in self.args[1]:
            varible_name = self.args[1]
            if not self.script.variables.value_exist(varible_name):
                raise NameError(f'Name {varible_name} is not declared in this scope.')
        arg = ' '.join(self.args[1:])
        args = arg.split(':')
        if args[0].strip() != varible_name:
            #对于所有合法的输入，变量名都会被且分到args[0]
            #特别的，当不提供变量名时，其为空，与varible_name的初始值恰好相同。
            raise SyntaxError('Missing ":" in input case command.')
        args = args[1:] #args总是长度大于等于1.
        for case_str in args:
            if not '->' in case_str:
                raise SyntaxError(f'Missing "->" in input case "{case_str}"')
            case_list = case_str.split('->')
            if len(case_list) != 2:
                raise AttributeError('Too much "->" for input case command.')
            description_str, command_str = case_list
            description = str(FormulaParser.evaluate_expression(description_str, self.script.variables))
            if description in ret.keys():
                raise AttributeError(f'Two same case string in one input command: {description_str}.')
            ret[description] = command_str

        return (ret, varible_name)