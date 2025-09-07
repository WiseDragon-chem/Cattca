from .memory.script import Script
from .commands.parser import execute_line, parse_line
from .exceptions import *

class Parser:

    def __init__(self, text: str):
        self.script = self.init_script(text)

    @staticmethod
    def init_script(text: str) -> Script:
        try:
            script = Script(text)
            script.turn_all_semicolon_into_wrapper()
            def init_labels(script: Script):
                script.index = 0
                while(script.index < script.len_text):
                    if script.check_is_left_wrapper():
                        command = script.get_command()
                        command_name, args = parse_line(command)
                        if command_name == 'label':
                            execute_line(command, script)
                    else:
                        script.index+=1
                script.index = 0
            init_labels(script)
        except CattcaSyntaxError as e:
            print(f'In index {script.index}:')
            print(e)
        return script

    def parse(self):
        while True:
            command = ''
            try:
                output = ''
                while self.script.status == 'CONTINUE':
                    output += Parser._get_text_til_command(self.script)
                    if self.script.index == self.script.len_text:
                        self.script.status = 'EXIT'
                        break
                    command = self.script.get_command()
                    #print(command)
                    temp_output = execute_line(command, self.script)
                    if temp_output != None:
                        output += temp_output
                if self.script.status == 'EXIT':
                    yield output
                    break
                elif self.script.status == 'AWAIT':
                    inp = yield output
                    self.script.clear_input()
                    self.script.set_input(inp)
                    self.script.status = 'CONTINUE'
                else:
                    yield output
            except CattcaAwaitException:
                pass
            except CattcaExitException:
                pass
            except CattcaException as e:
                print(f'In index {self.script.index}:')
                print(f'   {command}')
                print('   ' + '^'*len(command))
                print(e)
                break

    @staticmethod
    def _get_text_til_command(script: Script) -> str:
        '''
        往下移动指针，直到遇到 '</'，停留在 '<'
        '''
        output=''
        while(script.index < script.len_text and not script.check_is_left_wrapper()):
            output += script.get_char()
            script.index += 1
        return output