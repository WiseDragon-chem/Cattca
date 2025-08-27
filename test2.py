from core.parser import Parser

text = '''
</
let a = 1;
let b;
if a == 1 ->input text a;
log a;
input text b;
log a;
/>'''

parser = Parser(text)
parser = parser.parse()
print('next1', next(parser))
print(parser.send(100))
# print('next2', next(parser))