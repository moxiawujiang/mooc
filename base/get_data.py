__author__ = 'wujiang'
#coding:utf-8

import os
import sys
# project_path=os.path.dirname(os.path.dirname(__file__))
# sys.path.append(project_path)
sys.path.append("..\\util")
from util.operation_excel  import OperationExcel
from util.opera_json import OperaJson

class GetData:
    def __init__(self):
        self.data=OperationExcel()

    #获取行数
    def get_excel_lines(self):
        return  self.data.get_lines()

    #获取id
    def get_test_id(self,row):
        return self.data.get_cell(row,0)
    #获取用例名称
    def get_test_name(self,row):
        return self.data.get_cell(row,1)
    #获取url
    def get_url(self,row):
        return self.data.get_cell(row,2)
    #获取是否执行
    def get_is_run(self,row):
        res=self.data.get_cell(row,3)
        if res=="yes":
            return True
        else:
            return False
    #获取请求方式
    def get_methon(self,row):
        return self.data.get_cell(row,4)

    #获取头部信息
    def get_header(self,row):
        res=self.data.get_cell(row,5)
        if res!="":
            return res
        else:
            return None

    #获取请求数据
    def get_request_data(self,row):
        res=self.data.get_cell(row,9)
        if  res=="":
            return None
        else:
            res=OperaJson().get_data(res)
            return res
    #获取预期结果
    def get_expect(self,row):
        res=self.data.get_cell(row,10)
        return res
    #获取依赖id
    def get_depends_id(self,row):
        res=self.data.get_cell(row,6)
        return res
    #获取依赖数据
    def get_depends_key(self,row):
        res=self.data.get_cell(row,7)
        return res
    #获取依赖字段
    def get_depends_on(self,row):
        res=self.data.get_cell(row,8)
        return res




