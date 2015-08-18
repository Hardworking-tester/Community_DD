# encoding:utf-8
from Data import get_number_by_data,ReadExcel
zhuce_excelpath="F:\\Community_DD\\Data\zhuce.xls"
zhuce_sheet_name="zhuce_data"

table=ReadExcel.ReadExcel().getTableBySheetName(zhuce_excelpath,zhuce_sheet_name)
countrows=table.nrows

print int(table.cell_value(1,2))
