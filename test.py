from core.parser import Parser
from core.memory.script import Script

text = '''
</
let good = false;
let a = 10;
let b = 1;
let cnt = 0;
label chufa;
set a = a - b;
set cnt = cnt + 1;
if a>0 -> goto chufa;
if good -> goto chufaCompleted;
;
let l=1;
let r=100;
let target = 100;
let mid = 0;
set good = true;
label loopstart;
set a=l+r;
set b=2;
set cnt=0;
goto chufa;
label chufaCompleted;
set mid=cnt;
if mid * mid < target -> set l = mid+1;
if mid * mid > target -> set r = mid-1;
if mid * mid == target -> goto end;
goto loopstart;
label end;
log mid;
/>
'''

parser = Parser()
test_script = parser.init_script(text)
text = parser.next(test_script)
print('-------------------------------------------------------')
print(text)

