from time import sleep

import requests
from bs4 import BeautifulSoup


def getSoup(url: str):
    sleep(1)
    html = requests.get(url, "lxml")
    html.encoding = "utf-8"
    return BeautifulSoup(html.text, features="lxml")


class Downloader:
    def __init__(self, fp):
        self.outFile = open(fp, "w", encoding="utf-8")

    def getAll(self):
        self.getCharacterName()
        self.getWeaponName()
        # self.getEnemyName() 手动添加
        self.getFoodName()
        self.getAnimalName()
        self.getItemName()
        # self.getDecorationName()
        # self.getNPCName()
        self.getToponymName()
        self.getHiddenRealmName()
        self.outFile.close()

    def getCharacterName(self):
        resList = (
            getSoup("https://wiki.biligame.com/ys/%E8%A7%92%E8%89%B2")
            .select("#CardSelectTr > div > div.L"))

        print("获取角色完毕")
        self.outFile.write("# 角色列表\n")
        for item in resList:
            self.outFile.write("{0}\n".format(item.text))

    def getWeaponName(self):
        resList = (
            getSoup("https://wiki.biligame.com/ys/%E6%AD%A6%E5%99%A8%E4%B8%80%E8%A7%88")
            .select("#frameRole > div > div > div > div:nth-child(1) > div > div > div.L"))

        print("获取武器完毕")
        self.outFile.write("# 武器列表\n")
        for item in resList:
            self.outFile.write("{0}\n".format(item.text))

    def getRelicName(self):
        resList = (
            getSoup("https://wiki.biligame.com/ys/%E5%9C%A3%E9%81%97%E7%89%A9%E4%B8%80%E8%A7%88")
            .select("#frameRole > div > div > div > div > div > div > div.L"))

        print("获取圣遗物完毕")
        self.outFile.write("# 圣遗物列表\n")
        for item in resList:
            self.outFile.write("{0}\n".format(item.text))

    def getEnemyName(self):
        resList = (
            getSoup("https://wiki.biligame.com/sr/%E6%95%8C%E4%BA%BA%E7%AD%9B%E9%80%89")
            .select("#CardSelectTr > tbody > tr > td:nth-child(2) > a"))

        print("获取敌人完毕")
        self.outFile.write("# 敌人列表\n")
        for item in resList:
            text = item.text.replace("（完整）","")
            self.outFile.write("{0}\n".format(text))

    def getFoodName(self):
        resList = (
            getSoup("https://wiki.biligame.com/ys/%E9%A3%9F%E7%89%A9%E4%B8%80%E8%A7%88")
            .select("#CardSelectTr > tbody > tr > td:nth-child(2) > a"))

        print("获取食物完毕")
        self.outFile.write("# 食物列表\n")
        for item in resList:
            self.outFile.write("{0}\n".format(item.text))

    def getAnimalName(self):
        resList = (
            getSoup("https://wiki.biligame.com/ys/%E9%87%8E%E7%94%9F%E7%94%9F%E7%89%A9%E4%B8%80%E8%A7%88")
            .select("#CardSelectTr > tbody > tr > td:nth-child(2) > a"))

        print("获取动物名称完毕")
        self.outFile.write("# 动物名称列表\n")
        for item in resList:
            self.outFile.write("{0}\n".format(item.text))

    def getItemName(self):
        resList = (
            getSoup("https://wiki.biligame.com/ys/%E9%81%93%E5%85%B7%E4%B8%80%E8%A7%88")
            .select("#CardSelectTr > tbody > tr > td:nth-child(2) > a"))

        print("获取道具完毕")
        self.outFile.write("# 道具列表\n")
        for item in resList:
            self.outFile.write("{0}\n".format(item.text))

    def getDecorationName(self):
        resList = (
            getSoup("https://wiki.biligame.com/sr/%E8%A3%85%E9%A5%B0%E4%B8%80%E8%A7%88")
            .select("#CardSelectTr > tbody > tr > td:nth-child(2) > a"))

        print("获取装饰完毕")
        self.outFile.write("# 装饰列表\n")
        for item in resList:
            self.outFile.write("{0}\n".format(item.text))

    def getNPCName(self):
        resList = (
            getSoup("https://wiki.biligame.com/sr/NPC")
            .select("#CardSelectTr > tbody > tr > td:nth-child(2) > a"))

        print("获取NPC完毕")
        self.outFile.write("# NPC列表\n")
        for item in resList:
            self.outFile.write("{0}\n".format(item.text))

    def getToponymName(self):
        list = [
            "蒙德",
            "璃月",
            "璃月",
            "须弥",
            "枫丹",
            "纳塔",
        ]

        resList = []
        resList.extend(list)

        for part in list:
            soup = getSoup("https://wiki.biligame.com/ys/%E5%9C%B0%E7%90%86%E5%BF%97{0}".format(part))
            resList.extend(soup.select("#mw-content-text > div > div > div.showOn > div"))


        print("获取地理志完毕")
        self.outFile.write("# 地理志列表\n")
        for item in resList:
            self.outFile.write("{0}\n".format(item.text))

    def getHiddenRealmName(self):
        resList = (
            getSoup("https://wiki.biligame.com/ys/%E7%A7%98%E5%A2%83")
            .select("#mw-content-text > div > table > tbody > tr > td:nth-child(1) > b > a"))

        print("获取秘境完毕")
        self.outFile.write("# 秘境列表\n")
        for item in resList:
            self.outFile.write("{0}\n".format(item.text))
