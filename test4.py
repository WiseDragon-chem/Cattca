from core.parser import Parser

text = '''</
log '111' +'222';
log 1+ 2;
log 3==3;
log '222'== '22' + '2';
log true + 3;
/>'''

parser = Parser()
test_script = parser.init_script(text)
parser.next(test_script)