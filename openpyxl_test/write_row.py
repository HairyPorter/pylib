import openpyxl as xl
from openpyxl import Workbook

def num2litter(num):
    # 0~25转换到AB...Z
    if(num<0 or num>25):
        return 0
    else:
        return chr(ord("A")+num)
    
def n2xlrow(num):
    # 转换为excel列标（从1开始）
    count=26
    output=""
    if(num<=0):
        return 0
    elif(num>=1 and num<=count):
        output+=num2litter(num-1)
    else: 
        output+=n2xlrow((num-1)//count)
        output+=num2litter((num-1)%26)
    return output

def xlrc_split(site):
    # 把输入excel坐标分解成(列,行)
    i=0
    for c in site:
        if(ord(c)>=ord('0') and ord(c)<=ord('9')):
            break
        else:
            i+=1

    return (site[:i],site[i:])

def xlrow2n(row):
    # 把列标转换为数字
    row=row.lower()
    output=0
    e=len(row)-1
    for c in row:

        if(ord(c)<ord('a') and ord(c)>ord('z')):
            return 0
        else:
            output+=(ord(c)-ord('a')+1)*(26**e)
        e-=1
    return output

def write_rows(sheet, wlist, site):
    # sheet工作表；list写入表格；site写入位置
    r,c = xlrc_split(site)
    nsite=''
    for cell_val in wlist:
        nsite=r+c
        sheet[str(nsite)]=cell_val
        r=n2xlrow(xlrow2n(r)+1)
        # print(r,cell_val)
write_rows("sheet",["abc","def","ghi","B2"],"c2")





