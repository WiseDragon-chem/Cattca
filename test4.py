from core.parser import Parser
import sys

text = ''

def get_text():
    if len(sys.argv) != 2:
        print("使用方法: python test4.py <Cattca 文件路径>")
        sys.exit(1)
    
    try:
        with open(sys.argv[1], 'r', encoding='utf-8') as file:
            text = file.read()
            return text
    except Exception as e:
        print(f"错误: {e}")

if __name__ == "__main__":
    text = get_text()
    parser = Parser(text)
    parser_parse = parser.parse()
    print(next(parser_parse))
    while(parser.script.status != 'EXIT'):
        parser_parse.send(input(parser.script.input_request_message))