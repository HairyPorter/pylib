import pdfplumber
path = "200707-1.pdf"
data=[]
datadictlist=[]
with pdfplumber.open(path) as pdf:
    for i in [1,2]:
        apage = pdf.pages[i]
        # 读出每个表格
        pagetables = apage.extract_tables()

        # print(pagetables)
        for pagetable in pagetables:
            # 读出一个表格
            print('\n')
            for tablerow in pagetable:
                # 表格中的一行
                datadict={}
                if(tablerow[0].find('Contents')>0):


                    data.append(tablerow)
                    print(tablerow)


# print("data=\n",data)






