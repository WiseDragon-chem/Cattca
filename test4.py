from core.parser import Parser

text = '''</
let a = 1;
log a;
let b = 2;
log a+b;
log a + b == 2;
log a + b == 3;
let c = true;
log a + c;
log c;
/>'''

parser = Parser()
test_script = parser.init_script(text)
parser.next(test_script)