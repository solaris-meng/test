#coding=utf-8
import traceback
import random
import string
import requests
import hashlib
import xlwt
import csv

def csv_to_xls(name_csv):
    try:

        name_xls = '%s.xls' % name_csv[:-4]

        ###############################
        wb = xlwt.Workbook()
        ws = wb.add_sheet('word sheet')
        font0 = xlwt.Font()
        font0.name = 'Times New Roman'
        font0.colour_index = 0
        font0.bold = False
        font0.height = 320
  
        style0 = xlwt.XFStyle()
        style0.font = font0

        fd = csv.reader(open(name_csv, encoding='gbk'))
        #fd = csv.reader(open(name_csv))

        # open csv
        cur_row = 0
        for line in fd:
            cur_col = 0

            if not line:
                cur_row += 1
                continue

            tokens = line[0].split(',')
            for i in tokens:
                print('row-%d,col-%d, %s' % (cur_row, cur_col, i))
                ws.write(cur_row, cur_col, i,style0)
                cur_col += 1
            cur_row += 1

        wb.save(name_xls)
        return 'success'
        
    except Exception as e:
        err = traceback.print_exc()
        print(err)
        return 'failed'

name_csv = '111.csv'
csv_to_xls(name_csv)
