__author__ = 'wujiang'
#coding:utf-8
import requests
import json

class MyRequests:

    def send_post(self,url,data,header=None):

        if header!=None:
            res=requests.post(url=url,data=data,headers=header)
        else:
            res=requests.post(url=url,data=data)
        return res.json()

    def send_get(self,url,data=None,header=None):
        if None != header:
            res=requests.get(url,data,headers=header)
        else:
            res=requests.get(url,data)
        return res.json()


    def run_main(self,url,method,data=None,header=None):
        if method=="get":
            res=self.send_get(url,data,header)
        else:
            res=self.send_post(url,data,header)
        return json.dumps(res,ensure_ascii=False,sort_keys=True)


if __name__ == '__main__':
    url="http://localhost:8000/home/"
    data={"school":"562","name":"lili","card_id":"654321"}
    res=requests.get(url,data).json()
    header=None
    print(res)
    res=MyRequests().run_main(url=url,method="get",data=data,header=header)
    print(res)