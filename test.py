from core.parser import Parser
from core.memory.script import Script

text = '''
---render---
render start
</say -----log-----/>
---
</goto label2/>
</label label1/>this wont be rendered</say i love rust/>
</label label2/>this will be rendered
---
</goto label3/>
text
</label label3;say something;goto label4/>
</label label4/>
---
render end
</say ----endlog---/>
----exit----
</ exit />
some other text'''

parser = Parser()
test_script = parser.init_script(text)
text = parser.next(test_script)
print('-------------------------------------------------------')
print(text)
