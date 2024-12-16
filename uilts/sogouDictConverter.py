import os

class SogouDictConverter:
    def __init__(self, txt_file):
        self.txt_file = txt_file
        self.words = []

    def load_txt(self):
        """读取TXT文件并提取每行词语"""
        if not os.path.exists(self.txt_file):
            print(f"文件 {self.txt_file} 不存在！")
            return

        with open(self.txt_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            # 清除空行并去除每行的多余空格
            self.words = [line.strip() for line in lines if line.strip()]

    def generate_sogou_dict(self, output_file):
        """将提取的词语输出为一个Sogou输入法词库"""
        if not self.words:
            print("没有词语可转换！")
            return

        with open(output_file, 'w', encoding='utf-8') as f:
            for word in self.words:
                # 默认给每个词语赋一个简单的频率值，可以根据需要修改
                f.write(f"{word} 1000\n")
        print(f"词库文件已保存为 {output_file}")

    def convert(self, output_file):
        """执行TXT转词库操作"""
        self.load_txt()
        self.generate_sogou_dict(output_file)

