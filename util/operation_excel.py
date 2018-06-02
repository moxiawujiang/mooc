__author__ = 'wujiang'
#coding:utf-8
import xlrd
from xlutils.copy import copy
import time

class OperationExcel:
    def __init__(self,path=None):
        if None == path:
            self.path="C:\\Learn\\Interface_test\\mooc\\dataconfig\\"
            self.filename='interface.xlsx'
        self.excel=xlrd.open_workbook(self.path+self.filename)

    def get_sheet(self,i=None):
        if i==None:
            i=0
        return self.excel.sheets()[i]

    def get_lines(self):
        return  self.get_sheet().nrows

    def get_cell(self,row,col):
        return self.get_sheet().cell_value(row,col)

    #写入数据到excel
    def write_value(self,row,value):
        file_name="interface"+time.strftime("%y-%m-%d %H-%M-%S")+".xls"
        read=xlrd.open_workbook(self.path+self.filename)
        write_data=copy(read)
        write_sheet=write_data.get_sheet(0)
        write_sheet.write(row,11,value)
        write_data.save(self.path+file_name)

    #根据caseid找到行号
    def get_row_num(self,caseid):
        rows=self.get_lines()
        for i in range(1,rows):
            if self.get_cell(i,0)==caseid:
                return i

    #根据行号找到对应行的内容
    def get_row_data(self,row):
        row_data=self.excel.row_values(row)
        return row_data
    #根据caseid，找到对应行的内容
    def get_rows_data(self,caseid):
        row=self.get_row_num(caseid)
        rows=self.get_row_data(row)
        return rows




if __name__ == '__main__':
    book=OperationExcel()
    print(book.get_lines())
    print(book.get_cell(0,0))