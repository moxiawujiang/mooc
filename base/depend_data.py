__author__ = 'wujiang'
import os
import sys
pj_path=os.path.dirname(os.path.dirname(__file__))
sys.path.append(pj_path)
from base.get_data import GetData
from util.operation_excel import OperationExcel
from  base.my_requests import MyRequests
from jsonpath_rw import parse
import json

class DependsData:
    def __init__(self,caseid):
        self.data=GetData()
        self.excel=OperationExcel()
        self.caseid=caseid

    def run_depend_case(self):
        resquet=MyRequests()
        i=self.excel.get_row_num(self.caseid)
        url=self.data.get_url(i)
        data=self.data.get_request_data(i)
        method=self.data.get_methon(i)
        header=self.data.get_header(i)
        res=resquet.run_main(url,method,data,header)
        return json.loads(res)
    #获取返回值
    def get_data_for_key(self,row):
        depend_data=self.data.get_depends_key(row)
        response_data=self.run_depend_case()
        json_exe=parse(depend_data)
        madle=json_exe.find(response_data)
        return [math.value for math in madle][0]






