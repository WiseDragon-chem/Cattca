from core.parser import Parser
from core.memory.script import Script

text = '''test111</ say I love  Rust /></say    something/> 111  123</say </ />
---
</goto label2/>
</label label1/>this will not render
</label label2/>but this will
---
some text</ exit />
some other text'''

parser = Parser()
test_script = parser.init_script(text)
print(test_script.to_dict())
text = parser.next(test_script)
print(text)
