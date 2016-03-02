'''
Run from command line
python gen_report.py > output.csv
'''

import xlrd
import glob

#constants
sheet_name = "Sheet1"
start_row  = 5
start_col  = 0

def get_excel_data(name):

    xls1  = xlrd.open_workbook(name)

    dataList = []

    for sheet in xls1.sheet_names(): #iterate through sheets of workbook
        if sheet == sheet_name:
            sheet1 = xls1.sheet_by_name(sheet)

            MaxRows = sheet1.nrows

            MaxColumns = sheet1.ncols

            for rownum in range(start_row,MaxRows):
                rowList = []
                for colnum in range(start_col,MaxColumns):
                    cellval1 = sheet1.cell_value(rownum, colnum)
                    try:
                        if type(cellval1) is not float:
                            cellval1 = str(callval1).strip()
                            cellval1 = re.sub('[''!(,\':=.\r\n)%]','_',cellval1.strip())
                    except:
                        if type(cellval1) is float:
                            pass
                        else:
                            cellval1 = cellval1.encode('ascii', 'ignore')
                    rowList.append(cellval1)
                rowList.append(name[:-5])
                dataList.append(rowList)
        return dataList
                    
if __name__=='__main__':

    #get file list to feed into function, runs in current directory as is
    file_list = sorted(glob.glob('*.xlsx'))

    data = []

    for f in file_list:
        data += get_excel_data(f)

    for i in data:
        for j in i:
            print j,",",
        print
