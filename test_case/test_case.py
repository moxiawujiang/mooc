__author__ = 'wujiang'
#coding:utf-8
import sys
import os
pj_path=os.path.dirname(os.path.dirname(__file__))
sys.path.append(pj_path)
from base.get_data import GetData
from base.my_requests import MyRequests
from util.is_contain import is_contain
import xlrd
from xlutils.copy import copy
import time
from base.depend_data import DependsData

class Runtest:
    def __init__(self):
        self.data=GetData()
        self.request=MyRequests()
        self.path="C:\\Learn\\Interface_test\\mooc\\dataconfig\\"
        self.new_file="interface"+time.strftime("%y-%m-%d %H-%M-%S")+".xls"
        self.file_name="interface.xlsx"


    def run_test(self):

        read=xlrd.open_workbook(self.path+self.file_name)
        write_data=copy(read)
        write_sheet=write_data.get_sheet(0)

        rows=self.data.get_excel_lines()
        for i in  range(1,rows):
            case_id=self.data.get_test_id(i)
            print(case_id)
            url=self.data.get_url(i)
            data=self.data.get_request_data(i)
            method=self.data.get_methon(i)
            header=self.data.get_header(i)
            expect=self.data.get_expect(i)
            depends_id=self.data.get_depends_id(i)
            depends_on=self.data.get_depends_on(i)
            if self.data.get_is_run(i):
                if depends_id!="":
                    dp=DependsData(depends_id)
                    res_data=dp.get_data_for_key(i)
                    data[depends_on]=res_data
                res=self.request.run_main(url,method,data,header)
                print("实际结果为："+res)
                print("预期结果为："+expect)
                if is_contain(expect,res):
                    write_sheet.write(i,11,"pass")
                else:
                    write_sheet.write(i,11,"Fail")

        write_data.save(self.path+self.new_file)


if __name__ == '__main__':
    Runtest().run_test()