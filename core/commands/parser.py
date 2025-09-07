from typing import List, Tuple, Optional
from ..memory.object import CattcaObject
from ..memory.script import Script
from ..exceptions import *
from . import COMMANDS

def parse_line(line: str) -> Tuple[str, Optional[List[str]]]:
    '''
    解析一行代码。
    返回命令名和参数列表。
    '''
    parts = line.strip().split()
    if not parts:
        return '',None
    command_name = parts[0]
    args = parts[1:] if len(parts) > 1 else None
    return command_name, args

def execute_line(line: str, script: Script) -> None:
    '''
    执行一行代码。
    '''
    command_name, args = parse_line(line)
    if command_name == '':
        return
    if command_name in COMMANDS:
        command_instance = COMMANDS[command_name](args, script)
        output = command_instance.execute()
        if not isinstance(output, CattcaObject):
            return
        output = str(output)
        return output
    else:
        raise CattcaSyntaxError(f"Unknown command: {command_name}")