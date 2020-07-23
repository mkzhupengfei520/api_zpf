#coding:utf-8
import sys
#sys.setdefaultencoding('utf8')
import xlrd

import traceback

def Api_Data_read(path,sheetname):
    try:
        workbook = xlrd.open_workbook(path)
    except:
        print( traceback.format_exc())
        print ('can not find Api data file...')
        return False
    try:
        sheet_name = workbook.sheet_by_name(sheetname)
    except:
        print ('can not find datasheet...')
        return False
    title = []
    redata = []
    rows =sheet_name.nrows  #行
    clng = sheet_name.ncols  #列
    for i in range(clng-1):
        title.append(str(sheet_name.cell_value(0,i)))
    for index in range(rows):
        if index == 0:
            continue
        all_data = []
        json = {}
        for indexy in range(clng-1):
            json[title[indexy]] = str(sheet_name.cell_value(index, indexy))
            #json[title[indexy]]=str(int(sheet_name.cell_value(index,indexy)))
        code = (str(sheet_name.cell_value(index, indexy + 1)))
        #code = (str(int(sheet_name.cell_value(index, indexy+1))))
        json['case_name'] = sheetname
        all_data.append(json)
        all_data.append(code)
        redata.append(all_data)
    return redata
def Api_Data_write():
    pass

if __name__ == '__main__':
    a = Api_Data_read(r'C:\Users\EDZ\Desktop\ziyuanbao\untitled2\api_test\case\case1\Api_data2.xlsx', 'Api_data')
    print(a)



