from core.parser import Parser

text = '''</
say something;
goto label2;
label label1;
say here is label1;
goto label3;
label label2;
say here is label2;
goto label1;
label label3;
say here is label3;
say good.
/>'''

parser = Parser()
test_script = parser.init_script(text)
print('---raw---text---')
print(test_script.script_text)
print('---label-lst----')
print(test_script.labels.to_dict())
print('---log---start---')
text = parser.next(test_script)
print('---log---stop----')
print('-------------------------------------------------------')
print(text)
