from .label import label_lst
from .variable_system import VariableTable

class Script:
    def __init__(self, script_text: str, index: int = 0, status: str = 'CONTINUE', wrapper: tuple[str, str] = ('</', '/>')):
        '''
        初始化脚本。
        Args:
            script_text (str): 脚本的文本
            index (int): 脚本的指针
            status (str): 表示当前状态的字符串。
                      必须是以下四种之一:
                      - "CONTINUE": 表示继续执行。
                      - "AWAIT": 表示等待外部信号。
                      - "EXIT": 表示终止程序。
            wrapper (tuple[str, str]): “命令”所在括号的样式
        '''
        self.script_text = script_text
        self.index = index
        self.status = status
        self.len_text = len(script_text)
        self.wrapper = wrapper
        self.labels = label_lst()
        self.variables = VariableTable()

        self.output_area = ''
        self.input_area = ''
        self.input_request_message = []
    
    def get_char(self):
        return self.script_text[self.index]
    
    def push_forward(self):
        self.index += 1
    
    def check_is_left_wrapper(self):
        len_left = len(self.wrapper[0])
        if self.index + len_left > self.len_text:
            return False
        if self.script_text[self.index:self.index+len_left] == self.wrapper[0]:
            return True
    
    def check_is_right_wrapper(self):
        len_right = len(self.wrapper[1])
        if self.index + len_right > self.len_text:
            return False
        if self.script_text[self.index:self.index+len_right] == self.wrapper[1]:
            return True

    def get_command(self):
        '''
        从当前指针位置解析一个命令。
        如果当前位置不是一个命令的开始，则返回 None。
        如果命令没有正确闭合，则引发 SyntaxError。
        成功解析后，返回命令的字符串内容，并更新指针到命令之后。
        '''
        if not self.check_is_left_wrapper():
            return None
        
        len_left = len(self.wrapper[0])
        len_right = len(self.wrapper[1])
        command_start_index = self.index + len_left
        command_end_index = self.script_text.find(self.wrapper[1], command_start_index)

        if command_end_index == -1:
            raise SyntaxError(f"Unclosed command starting at index {self.index}. Expected '{self.wrapper[1]}'.")

        command_text = self.script_text[command_start_index:command_end_index].strip()

        self.index = command_end_index + len_right
        return command_text
        
    def to_dict(self):
        return {'script_text': self.script_text, 'index': self.index, 'status': self.status, 'len_text': self.len_text, 'wrapper': self.wrapper, 'labels': self.labels}
    
    def turn_all_semicolon_into_wrapper(self): 
        """把所有的 '</''/>'内的 ';' 变成 '/></'"""
        self.index = 0
        tmp_str_lst = ['']
        while self.index < self.len_text:
            if self.check_is_left_wrapper():
                while self.index<self.len_text and not self.check_is_right_wrapper():
                    if self.script_text[self.index] == ';':
                        tmp_str_lst.append(self.wrapper[1] + self.wrapper[0])
                    else:
                        tmp_str_lst.append(self.script_text[self.index])
                    self.index += 1
            else:
                tmp_str_lst[len(tmp_str_lst) -1] += self.script_text[self.index]
                self.index += 1
        self.index = 0
        self.script_text = ''.join(tmp_str_lst)
        self.len_text = len(self.script_text)
        return self.script_text
    
    def append_output(self, text: str):
        """将输出追加至输出区"""
        self.output_area = self.output_area + text

    def set_input(self, text: str):
        if self.input_area != '':
            raise RuntimeError('Input area has not been cleared. Clean it in advance.')
        self.input_area = text

    def clear_input(self):
        self.input_area = ''

    def get_input(self) -> str:
        return self.input_area
    