#! /usr/bin/env python
# coding: utf-8


import xlwt
import codecs


def text_to_excel(inputfile, sheetname, start_row, start_col, outputfile):
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet(sheetName)
    f = codecs.open(inputfile, 'r')
    row_excel = start_row
    try:
        for line in f:
            row_excel += 1
            line = line.strip()
            line = line.split(' ')
            len_line = len(line)
            col_excel = start_col
            for j in range(len_line):
                ws.write(row_excel, col_excel, line[j])
                col_excel += 1
                wb.save(outputfile)
    except:
        print ('')


if __name__ == "__main__":
    sheetName = 'Sheet2'#需要写入excel中的Sheet2中，可以自己设定
    start_row = 7 #从第7行开始写
    start_col = 3 #从第3列开始写
    inputfile = 'text.txt' #输入文件
    outputfile = 'excel_result.xls' #输出excel文件
    text_to_excel(inputfile,sheetName,start_row,start_col,outputfile)