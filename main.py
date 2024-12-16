from time import sleep

from uilts.converter import Converter
from uilts.downloader import Downloader
from uilts.sogouDictConverter import SogouDictConverter

downloadFile = "files/download.txt"
outputFile = "files/genshin.dict.yaml"

print("开始获取信息")
# downloader = Downloader(downloadFile)
# downloader.getAll()
info = {
    "name": "genshin",
    "version": "2024-12-16",
    "sort": "by_weight"
}
print(info)
print("开始转换")
converter = Converter(downloadFile, outputFile, info)
converter.generate()

converter = SogouDictConverter(downloadFile)  # 'input.txt' 为输入的TXT文件路径
converter.convert('files/sogou_dict.txt')  # 生成的词库文件路径
