__author__ = 'wujiang'
#coding:utf-8

import json

class OperaJson:
    def __init__(self):
        self.data=self.read_data()
    #读取json文件
    def read_data(self):
        with open("C:\\Learn\\Interface_test\\mooc\\dataconfig\\data.json") as fp:
            data=json.load(fp)
        return data
    #根据关键字获取数据
    def get_data(self,id):
        return self.data[id]

if __name__ == '__main__':
    data=OperaJson()
    print(data.get_data("login"))






