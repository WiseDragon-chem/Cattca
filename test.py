from core.parser import Parser
from core.memory.script import Script

text = '''
</
let a = 1;
let b = a + 1 == 2;
log a;
log b;

/>
'''

parser = Parser()
test_script = parser.init_script(text)
text = parser.next(test_script)
print('-------------------------------------------------------')
print(text)
