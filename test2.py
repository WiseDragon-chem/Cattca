from core.parser import Parser

text = '''
</
let a = 8;
log a+8*7;
let cc = 876789;
input text a;
log a;
/>'''

parser = Parser(text)
parser = parser.parse()
print(next(parser))
print(parser.send(12))
