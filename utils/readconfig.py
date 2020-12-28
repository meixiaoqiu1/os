import os
import configparser
from common.getparentpath import GetParentPath

project_pathpath=GetParentPath().get_project_path()
path=os.path.join(project_pathpath,'config','config.ini')
config=configparser.ConfigParser()
cf = configparser.RawConfigParser()
cf.read(path,encoding='utf-8')

class ReadConfig():
    def get_http(self,name):
        value=cf.get('HTTP',name)
        return value

