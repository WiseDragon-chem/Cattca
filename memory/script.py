class Script:
    def __init__(self, script_text: str, index: int = 0, status: str = 'AWAIT'):
        '''
        初始化脚本。
        Args:
            script_text (str): 脚本的文本
            index (int): 脚本的指针
            status (str): 表示当前状态的字符串。
                      必须是以下四种之一:
                      - "CONTINUE": 表示继续执行。
                      - "AWAIT": 表示等待外部信号。
                      - "ERROR": 表示发生错误。
                      - "EXIT": 表示终止程序。
        '''
        self.script_text = script_text
        self.index = index
        self.status = status