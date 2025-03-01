# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 16:08:41 2023

@author: KIIT
"""

import xlrd
loc=('Demo_Excel.xls')

wb=xlrd.open_workbook(loc)


sheet=wb.sheet_by_index(0)

for row_index in range(sheet.nrows):
    row_data = []
    for col_index in range(sheet.ncols):
        cell_value = sheet.cell_value(row_index, col_index)
        row_data.append(cell_value)
    print(row_data)



print(sheet.ncols)
print(sheet.nrows)

print(sheet.col_values(2))
print(sheet.row_values(1))