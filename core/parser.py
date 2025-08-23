from .memory.script import Script
from .commands.parser import execute_line
class Parser:
    @staticmethod
    def next(script: Script):
        try:
            output = ''
            while(script.status == 'CONTINUE'):
                output += Parser._get_text_til_command(script)
                if script.index == script.len_text:
                    script.status = 'EXIT'
                    break
                command = script.get_command()
                execute_line(command, script)
            return output
        except SyntaxError as e:
            print(f'SyntaxError: {e}')
        except ValueError as e:
            print(f'ValueError: {e}')
        except Exception as e:
            print(f'Exception: {e}')


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