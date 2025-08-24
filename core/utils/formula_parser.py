import re
from typing import List, Union
from ..memory.variable_system import VariableTable, DynamicVariableSystem
from ..memory.object import CattcaObject
from ..memory import TypeRegistry

class FormulaParser:
    # 定义运算符优先级（数值越大优先级越高）
    OPERATOR_PRECEDENCE = {
        '==': 1, '!=': 1,  # 比较运算符
        '<': 2, '>': 2, '<=': 2, '>=': 2,
        '+': 3, '-': 3,    # 加减法
        '*': 4, '/': 4,    # 乘除法
        '**': 5,           # 指数
    }
    
    # 按长度排序的运算符列表（长的优先匹配）
    OPERATORS = sorted(OPERATOR_PRECEDENCE.keys(), key=len, reverse=True)
    
    @staticmethod
    def tokenize(expression: str) -> List[str]:
        """
        将表达式分词
        
        Example:
            input: 'a + b * (c + 1)'
            output: ['a', '+', 'b', '*', '(', 'c', '+', '1', ')']
        """
        tokens = []
        i = 0
        n = len(expression)
        
        while i < n:
            char = expression[i]
            
            # 跳过空格
            if char.isspace():
                i += 1
                continue
                
            # 处理字符串字面量
            if char in ('"', "'"):
                end_quote = expression.find(char, i + 1)
                if end_quote == -1:
                    raise SyntaxError("Unclosed string literal")
                tokens.append(expression[i:end_quote + 1])
                i = end_quote + 1
                continue
                
            # 处理运算符
            operator_found = False
            for op in FormulaParser.OPERATORS:
                if expression.startswith(op, i):
                    tokens.append(op)
                    i += len(op)
                    operator_found = True
                    break
                    
            if operator_found:
                continue
                
            # 处理括号
            if char in '()':
                tokens.append(char)
                i += 1
                continue
                
            # 处理标识符和数字
            if char.isalpha() or char == '_':  # 标识符
                j = i
                while j < n and (expression[j].isalnum() or expression[j] == '_'):
                    j += 1
                tokens.append(expression[i:j])
                i = j
            elif char.isdigit() or (char == '.' and i + 1 < n and expression[i + 1].isdigit()):  # 数字
                j = i
                # 处理整数和小数
                while j < n and (expression[j].isdigit() or expression[j] == '.'):
                    j += 1
                # 处理科学计数法
                if j < n and expression[j].lower() == 'e':
                    j += 1
                    if j < n and expression[j] in '+-':
                        j += 1
                    while j < n and expression[j].isdigit():
                        j += 1
                tokens.append(expression[i:j])
                i = j
            else:
                raise SyntaxError(f"Unexpected character: {char}")
                
        return tokens

    @staticmethod
    def infix_to_postfix(tokens: List[str]) -> List[str]:
        """将中缀表达式转换为后缀表达式（逆波兰表示法）"""
        output = []
        stack = []
        
        for token in tokens:
            if token in FormulaParser.OPERATOR_PRECEDENCE:
                # 处理运算符
                while (stack and stack[-1] != '(' and 
                       FormulaParser.OPERATOR_PRECEDENCE.get(stack[-1], 0) >= 
                       FormulaParser.OPERATOR_PRECEDENCE[token]):
                    output.append(stack.pop())
                stack.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                # 弹出直到左括号
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                if not stack or stack[-1] != '(':
                    raise SyntaxError("Mismatched parentheses")
                stack.pop()  # 弹出左括号
            else:
                # 操作数直接输出
                output.append(token)
                
        # 弹出剩余运算符
        while stack:
            if stack[-1] == '(':
                raise SyntaxError("Mismatched parentheses")
            output.append(stack.pop())
            
        return output

    @staticmethod
    def parse_value(token: str, table: VariableTable) -> CattcaObject:
        """将token转换为CattcaObject"""
        if not token:
            return TypeRegistry.get_type('null')()
            
        # 字符串字面量
        if (token.startswith('"') and token.endswith('"')) or \
           (token.startswith("'") and token.endswith("'")):
            content = token[1:-1]
            return TypeRegistry.get_type('string')(content)
            
        # 布尔值
        if token.lower() in ('true', 'false'):
            return TypeRegistry.get_type('boolean')(token.lower() == 'true')
            
        # 数字
        if token.replace('.', '', 1).replace('e', '', 1).replace('E', '', 1).replace('+', '', 1).replace('-', '', 1).isdigit():
            try:
                if '.' in token or 'e' in token.lower():
                    value = float(token)
                else:
                    value = int(token)
                return TypeRegistry.get_type('number')(value)
            except ValueError:
                pass
                
        # 变量
        if table.value_exist(token):
            return table.get_value(token)
            
        # 空值
        if token.lower() == 'null':
            return TypeRegistry.get_type('null')()
            
        raise NameError(f"Undefined variable or invalid literal: {token}")

    @staticmethod
    def evaluate_expression(expression: str, table: VariableTable) -> CattcaObject:
        """计算表达式值"""
        # 分词
        tokens = FormulaParser.tokenize(expression)
        if not tokens:
            return TypeRegistry.get_type('null')()
            
        # 转换为后缀表达式
        postfix = FormulaParser.infix_to_postfix(tokens)
        
        # 计算后缀表达式
        stack = []
        for token in postfix:
            if token in FormulaParser.OPERATOR_PRECEDENCE:
                # 处理运算符
                if len(stack) < 2:
                    raise SyntaxError("Insufficient operands")
                right = stack.pop()
                left = stack.pop()
                result = FormulaParser.apply_operator(token, left, right)
                stack.append(result)
            else:
                # 处理操作数
                value = FormulaParser.parse_value(token, table)
                stack.append(value)
                
        if len(stack) != 1:
            raise SyntaxError("Invalid expression")
            
        return DynamicVariableSystem.create_object(stack[0])

    @staticmethod
    def apply_operator(operator: str, left: CattcaObject, right: CattcaObject) -> CattcaObject:
        """应用运算符"""
        try:
            if operator == '+':
                return left + right
            elif operator == '-':
                return left - right
            elif operator == '*':
                return left * right
            elif operator == '/':
                return left / right
            elif operator == '==':
                return left == right
            elif operator == '!=':
                return left != right
            elif operator == '<':
                return left < right
            elif operator == '>':
                return left > right
            elif operator == '<=':
                return left <= right
            elif operator == '>=':
                return left >= right
            else:
                raise ValueError(f"Unsupported operator: {operator}")
        except Exception as e:
            raise TypeError(f"Operation {operator} not supported between {type(left).__name__} and {type(right).__name__}")
