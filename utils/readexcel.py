import os
import xlrd
import xlwt
from common.getparentpath import GetParentPath


path=GetParentPath().get_project_path()
class ReadExcel():
    def __init__(self,xls_name,sheet_name):
        self.xls_name=xls_name
        self.sheet_name=sheet_name
        xlsPath=os.path.join(path,'testdata',self.xls_name)
        self.f=xlrd.open_workbook(xlsPath)
        self.sheet = self.f.sheet_by_name(self.sheet_name)



    def read_xls(self,row,col):
        self.row = row
        self.col = col
        cell_value=self.sheet.cell(self.row, self.col).value
        return cell_value


    def write_xls(self,value):
        self.sheet.write(self.row, self.col, label=value)
        self.f.save()

    def f_close(self):
        self.f_close()

