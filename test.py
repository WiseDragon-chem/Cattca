from core.parser import Parser
from core.memory.script import Script

text = 'test111</ say I love  Rust /></ say something /> 111  123</say </ />'

test_script = Script(text, status='CONTINUE')

parser = Parser()

text = parser.next(test_script)
print(text)
