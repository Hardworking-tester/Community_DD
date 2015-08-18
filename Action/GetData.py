# encoding:utf-8
from Data import get_number_by_data,ReadExcel
class GetData():

    def getData(self,element_key):
        zhuce_excel_path="F:\\Community_DD\\Data\zhuce.xls"
        zhuce_sheetname="zhuce_data"
        sheet=ReadExcel.ReadExcel().getTableBySheetName(zhuce_excel_path,zhuce_sheetname)
        row_col_list=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(zhuce_excel_path,zhuce_sheetname,element_key)
        data=sheet.cell_value(row_col_list[0]+1,(row_col_list[1]))
        if type(data)==float:
            return  int(data)
        else:
            return data
