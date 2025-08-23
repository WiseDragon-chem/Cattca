from core.parser import Parser
from core.memory.script import Script

text = 'test111</ say I_love_Rust />'

test_script = Script(text, status='CONTINUE')

parser = Parser()

print(parser.next(test_script))