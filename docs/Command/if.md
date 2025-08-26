# </if expression -> command />
如果表达式expression为true，那么执行command指令.

# usage
```cattca
</
let a = 3;
label loop_start;
log a;
set a = a-1;
if a>0 -> goto loop_start;
exit;
/>
```
```bash
3
2
1
0
```