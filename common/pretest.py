from common.getparentpath import GetParentPath
from common.sendrequests import SendRequets
from utils.log import Logger
from utils.readconfig import ReadConfig
import os
import json
from utils.readexcel import ReadExcel

baseurl = ReadConfig().get_http('baseurl')
cookies = ReadConfig().get_http('cookies')
open_file = ReadExcel('os测试用例.xlsx', 'home')
headers = {'Content-Type': 'application/x-www-form-urlencoded',
           'Cookie': cookies
           }

class PreTest():


    def simplePost(self,row=1,col1=2,col2=3,col3=4):
        path = open_file.read_xls(row, col1)
        url = baseurl + path
        method = open_file.read_xls(row, col2)
        data = open_file.read_xls(row, col3)
        result = SendRequets().send_requests(method=method, url=url, data=data, headers=headers)
        return result
