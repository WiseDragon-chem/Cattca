# </if expression -> label/>
如果表达式expression为true，那么跳转到label所在行继续执行.

# usage
```cattca
</
let a = 3;
label loop_start;
log a;
if a>0 -> loop_start;
exit;
/>
```
```bash
3
2
1
0
```