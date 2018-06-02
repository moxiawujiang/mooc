__author__ = 'wujiang'
#coding:utf-8

def is_contain(str1,str2):
    """判断str1是否在str2中"""
    flag=None
    if str1 in str2:
        flag=True
    else:
        flag=False
    return flag

