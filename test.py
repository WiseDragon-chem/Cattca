from core.parser import Parser
from core.memory.script import Script

text = '''
</
let a = 1;
log a;
let c='1';
log c;
/>
'''

parser = Parser()
test_script = parser.init_script(text)
text = parser.next(test_script)
print('-------------------------------------------------------')
print(text)

