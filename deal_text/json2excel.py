#! /usr/bin/env python
# coding: utf-8


import xlwt
import json
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')
import io



def city_info(jsonfile):
    with io.open(jsonfile, encoding='utf-8') as f:
        content = json.load(f)
    wb = xlwt.Workbook()
    sheet = wb.add_sheet('sheet1', cell_overwrite_ok=True)
    titles = ['id', '城市']
    for col in range(len(titles)):
        sheet.write(0, col, titles[col])
    for line in content:
        sheet.write(int(line), 0, line)
        for col in range(len(content[line])):
            sheet.write(int(line),col+1, content[line][col] )
    wb.save(jsonfile)
jsonfile = 'city.txt'
city_info(jsonfile)