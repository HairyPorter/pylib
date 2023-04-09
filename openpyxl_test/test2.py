import openpyxl as xl

def print_rows(sheet):
    for row in sheet.iter_rows(values_only=True):
        print(row)

filename="sample.xlsx"
workbook = xl.load_workbook(filename=filename)
sheet=workbook['amazon_reviews_us_Watches_v1_00']
print(sheet.dimensions)



workbook.save(filename=filename)
# print_rows(sheet)
