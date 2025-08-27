from core.parser import Parser

text = '''</
let a;
set a=7;
log a+3;
/>'''

parser = Parser()
test_script = parser.init_script(text)
# print('---raw---text---')
# print(test_script.script_text)
# print('---label-lst----')
# print(test_script.labels.to_dict())
# print('---log---start---')
# text = parser.next(test_script)
# print('---log---stop----')
# print('-------------------------------------------------------')
# print(text)
print(parser.next(test_script))