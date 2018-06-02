__author__ = 'wujiang'
#coding:utf-8
from mock import mock
def my_mock(mock_method,response_data,url,method,data):
    mock_method=mock.Mock(return_value=response_data)
    res=mock_method(url,method,data)
    return res