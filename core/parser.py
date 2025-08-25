from .memory.script import Script
from .commands.parser import execute_line, parse_line
class Parser:

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
        except SyntaxError as e:
            print(f'SyntaxError: {e}')
        return script

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
                temp_output = execute_line(command, script)
                if temp_output != None:
                    output += temp_output
            return output
        except SyntaxError as e:
            print(f'SyntaxError: {e}')
        except ValueError as e:
            print(f'ValueError: {e}')
        except IndexError as e:
            print(f'IndexError: {e}')
        except KeyError as e:
            print(f'KeyError: {e}')
        except TypeError as e:
            print(f'TypeError: {e}')
        except NameError as e:
            print(f'NameError: {e}')
        except AttributeError as e:
            print(f'AttributeError: {e}')
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