# encoding:utf-8
from Data import ReadExcel,get_number_by_data
from  appium.webdriver.common.mobileby import By
class GetElement():

    def getElementList(self):
        zhuce_excelpath="F:\\Community_DD\\Data\\zhuce.xls"
        zhuce_sheet_name="objname_locatemethod_locatedata"
        zhuce_element_list=[]
        zhuce_how_what_method_list=[]
        table=ReadExcel.ReadExcel().getTableBySheetName(zhuce_excelpath,zhuce_sheet_name)
        countrows=table.nrows
        for i in range(countrows):
            zhuce_element_list.append(table.cell_value(i,0))
        zhuce_element_list.pop(0)
        print zhuce_element_list
        for element in zhuce_element_list:
            zhuce_how_what_method_list.append(self.getLocatDataAndMethod(element,zhuce_element_list))
        print zhuce_how_what_method_list
        return zhuce_how_what_method_list

    def getLocatDataAndMethod(self,element,zhuce_element_list):
        zhuce_data_excelpath="F:\\Community_DD\\Data\zhuce.xls"
        zhuce_data_sheet_name="objname_locatemethod_locatedata"
        sheeet=ReadExcel.ReadExcel().getTableBySheetName(zhuce_data_excelpath,zhuce_data_sheet_name)
        row_col_index=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(zhuce_data_excelpath,zhuce_data_sheet_name,element)
        old_how=sheeet.cell_value(row_col_index[0],(row_col_index[1]+1))
        what=sheeet.cell_value(row_col_index[0],(row_col_index[1]+2))
        #在这里增加一个字典是因为如果直接把By.ID写在excel里的话，取出来不能用
        locate_method_dict={'id':By.ID,'css':By.CSS_SELECTOR,'xpath':By.XPATH,'linktext':By.LINK_TEXT}
        new_how=locate_method_dict[old_how]
        how_what=[]
        how_what.append(element)
        how_what.append(new_how)
        how_what.append(what)
        how_what.append(self.getOperateMethod(element))
        return how_what

    def getOperateMethod(self,element):

        zhuce_operate_data_excelpath="F:\\Community_DD\\Data\zhuce.xls"
        zhuce_operate_data_sheet_name="operate_method"
        sheet=ReadExcel.ReadExcel().getTableBySheetName(zhuce_operate_data_excelpath,zhuce_operate_data_sheet_name)
        row_col_list=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(zhuce_operate_data_excelpath,zhuce_operate_data_sheet_name,element)
        operate_method_data=sheet.cell_value(row_col_list[0],(row_col_list[1]+1))
        return operate_method_data


