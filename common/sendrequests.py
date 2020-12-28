import requests
import json

class SendRequets():
    def send_post(self,url,data,headers):
        result1=requests.post(url=url,data=data,headers=headers)
        res1 = json.dumps(result1.text, ensure_ascii=False)
        return res1
    def send_get(self,url,data,headers):
        result2=requests.get(url=url,data=data,headers=headers)
        res2=json.dumps(result2.text,ensure_ascii=False)
        return res2
    def send_requests(self,method,url,data,headers):
        if method=='post':
            return self.send_post(url,data,headers)
        elif method=='get':
            return self.send_get(url,data,headers)
        else:
            print('请求方法错误')
