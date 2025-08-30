from core.parser import Parser

text = '''
</
let a;
input case a
 :"111" -> goto aaa
 :"11111" -> goto bbb;
 label aaa;
 log 114;
 exit;
 label bbb;
 log 1919;
 input text a;
 log a;
/>'''

parser = Parser(text)
parser = parser.parse()
print('next1', next(parser))
print(parser.send(11111))
print(parser.send(345))
# print('next2', next(parser))