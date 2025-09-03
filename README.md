# Cattca

项目地址：[github](https://github.com/WiseDragon-chem/Cattca)

## 介绍

### Cattca 是什么？

Cattca 是一种编程语言，是一种文本标记语言。

### Cattca 有什么用？

您可以在展示文本的同时，在文本中嵌入代码。

Cattca 提供用户输入和条件判断的接口。

这让您可以用 Cattca 方便的制作互动小说和文本驱动的游戏。

### 为什么用 Cattca?

Cattca 的语法十分简单。一个没有编程基础的人也可以在几分钟内掌握。

Cattca 的使用非常方便。可以让简单项目的开发变得十分简单。

## 语法

Cattca 的文件由两部分组成：文本和命令。

### 文本

直接放置的文本会按顺序直接被渲染。

Cattca：

```Cattca
一段文本
第二段文本
```

输出：

```
一段文本
第二段文本
```

### 命令

Cattca 有很多命令。

要区分文本和命令，请把命令用`</`和`/>`包裹。命令之间也可以用分号分隔。

例如：

```Cattca
一段文本
</ command1 />
第二段文本
</ 
command2;
command3;
command4;
/>
```

#### `</ label />`

`label`命令与`goto`配合使用。

语法：`</ label labelname />`

`label`用来标记一个位置。使用`goto`后，代码会从 `label`命令的后面开始执行。

#### `</ goto />`

`goto`命令与`label`配合使用。

语法：`</ goto labelname />`

用`label`标记一个位置之后，使用`goto`命令，可以让代码从`labelname`对应的地方继续执行。

##### 示例一

代码：

```Cattca
一段文本。
</ goto label1 />
这段文本不会被显示。
</ label label1 />
这段文本会被显示。
```

输出：

```
一段文本。

这段文本会被显示。
```

##### 示例二

输入:

```Cattca
一段文本。
</ goto label1 />
</ label label2 />
这里是 label2。
</ goto label3 />
</ label label1 />
这里是 label1。
</ goto label2 />
</ label label3 />
结束了！
```

输出：

```
一段文本。

这里是 label1。

这里是 label2。

结束了！
```

#### `</ exit />`

`</ exit />`让你终止程序。

示例：

```Cattca
一段文本。
</ exit />
这段文本不会显示。
```

#### `</ let />`

`let`命令用于声明变量。

语法：`</ let variablename = value />`

变量可以存储数字、布尔值、字符串。

声明后可以先不赋值。此时变量会被赋值为 `null`

示例：

```Cattca
</ let a = 10 />
</ let good = false />
</ let name = "hello" />
```

#### `</ set />`

`set`命令用于修改已声明变量的值。

语法：`</ set variablename = value />`

示例：

```Cattca
</ let a = 10 />
</ set a = 20 />
</ set a = a + 5 />
```

#### `</ if />`

`if`命令用于条件判断。

语法：`</ if condition -> action />`

当条件为真时，执行指定的动作。

示例：

```Cattca
</ let a = 10 />
</ if a > 5 -> goto success />
</ exit />
</ label success />
a 大于 5！
```

支持的比较运算符：

- `>` 大于
- `<` 小于
- `==` 等于

#### `</ log />`

`log`命令用于在终端输出变量或表达式的值。

语法：`</ log variablename />`

示例：

```Cattca
</ let result = 42 />
</ log result />
</ log 'a' + 'b' />
```

输出：

```
42
ab
```

#### `</ input />`

`input`命令用于处理输入。

`input` 有多种语句。

##### `</ input text />`

`input text` 用来得到一个字符串的输入。

语法：

`</ input text variable_name />`

`variable_name` 是一个接受输入的变量名，在输入后，`variable_name` 的值会被赋值为输入的字符串。

`variable_name` 必须提前用 `let` 声明

##### `</ input case />`

`input case` 用来提供一个选项的输入。

语法：

```
<input case variable_name:
case_text_1 -> command1:
case_text_2 -> command2;
```

`variable_name`: 可选。在此处和在 `input text` 中的一样，接收所输入的字符串。

`case_text`: 一个类型为字符串的表达式。用户需要选择所有 `case_text` 其中的一个字符串进行输入。

`command`: 一条命令。如果用户的输入是对应的 `case_text`， 则对应的 `command` 会被执行。

#### `</ apply />`

`apply` 用来把一个字符串输出到文本流。

用法： `</apply text />`

`text` 是一个值的类型为字符串的表达式。

## 运算符

Cattca 支持基本的数学运算：

- `+` 加法
- `-` 减法
- `*` 乘法

示例：

```Cattca
</ let a = 10 />
</ let b = 3 />
</ set a = a + b />
</ set b = a * 2 />
```

字符串也可以使用加号，让两个字符串首尾相接。

## 完整示例

### 互动小说

```Cattca
你叫莱莉菥。
现在是早上六点，你醒了。
你躺在床上。
你要怎么做？
</let cntsleep = 0;
label 1;
input case:
'继续睡觉' -> goto 2:
'起床' -> goto 3;
/>

</label 2;
set cntsleep = cntsleep + 1;
if cntsleep > 3 ->goto 4/>
你睡不着。
</goto 1;/>

</label 3/>
结局一：起床
你成功起床了。
</exit/>

</label 4/>
结局二：睡觉
你又睡着了。
</exit/>
```

### 算法

以下是一个使用 Cattca 实现二分查找算法的完整示例：

```Cattca
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
```

这个例子展示了如何使用 Cattca 的各种功能来实现复杂的算法逻辑。

## 最佳实践

1. **合理使用标签**：为标签起有意义的名字，便于代码维护。
2. **避免无限循环**：使用 `goto` 时要确保有适当的退出条件。
3. **变量命名**：使用清晰的变量名，提高代码可读性。

## 常见问题

### Q: 如何在文本中显示 `</` 和 `/>`？

A: 目前需要避免在普通文本中使用这些字符组合。

### Q: Cattca 支持哪些数据类型？

A: Cattca 支持数字、布尔值和字符串等基本数据类型。

### Q: 可以嵌套使用命令吗？

A: 命令块内可以包含多个命令，但不支持命令的嵌套定义。

## 更多资源

- [GitHub 仓库](https://github.com/WiseDragon-chem/Cattca)
- [示例项目](https://github.com/WiseDragon-chem/Cattca/examples)
- [问题反馈](https://github.com/WiseDragon-chem/Cattca/issues)
