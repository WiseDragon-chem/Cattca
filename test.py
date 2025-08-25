from core.parser import Parser
from core.memory.script import Script

text = '''
</
let let = true;
let a = 1;
goto let;
label let;
log 123;
label let;


'''

parser = Parser()
test_script = parser.init_script(text)
text = parser.next(test_script)
print('-------------------------------------------------------')
print(text)
