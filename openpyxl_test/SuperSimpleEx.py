from openpyxl import Workbook
# from write_row import *
workbook=Workbook()
sheet= workbook.active
sheet["a"+"1"]="hello"
sheet["B1"]="world!"
sheet.cell(row=4,column=6)

sheet.append(["abc","def"])

workbook.save(filename="openpyxl_test\hello_world.xlsx")