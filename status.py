import xlrd 

def status():
    xl_workbook = xlrd.open_workbook('00 index.xlsx')
    
    print (xl_workbook.sheet_by_index(0).col_values(0))

    
if __name__ == '__main__':
    status()
