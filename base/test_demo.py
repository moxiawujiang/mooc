__author__ = 'wujiang'

#coding:utf-8

import unittest
import json
from my_requests import MyRequests
from my_mock import my_mock
import  requests


class TestMthod(unittest.TestCase):

    def setUp(self):
        self.run=MyRequests()


    @unittest.skip("test_01")
    def test_01(self):
        url="http://localhost:8000/login/"
        data={"username":"zhangxiaoxue",
              "password":"123456"
              }
        #res=my_mock(self.run.run_main,data,url,"POST",data)
        header=''
        res=self.run.run_main(url,"POST",data,header)


    def test_02(self):
        count=0
        for i in range(1,1002):
            if i%2==0 or i%3==0 or i%5==0:
                count=count+1

        print(count)


if __name__ == '__main__':
    unittest.main()