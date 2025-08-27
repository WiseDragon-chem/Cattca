from core.parser import Parser

text = '''
</
let a;
let b;
input text a;
log 1;
input text b;
log b;
/>'''

parser = Parser(text)
parser = parser.parse()
print('next1', next(parser))
print('------------------')
print(parser.send(100))
#print(parser.send(120))
# print('next2', next(parser))