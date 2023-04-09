from openpyxl import Workbook
workbook=Workbook()
sheet= workbook.active
sheet["A1"]="hello"
sheet["B1"]="world!"

workbook.save(filename="openpyxl_test\hello_world.xlsx")