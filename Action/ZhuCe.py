# encoding:utf-8
from appium import webdriver
from Base.APPBasePage import APPBasePage
import GetElement
import GetData
class ZhuCe(APPBasePage):

    def getoperateElementMethodAndData1(self):
        how_what_list=GetElement.GetElement().getElementList()
        print how_what_list
        for method_data_list in how_what_list:
            app_object=method_data_list[0]
            how=method_data_list[1]
            what=method_data_list[2]
            operate_method=method_data_list[3]
            self.locateElement(app_object,how,what,operate_method)
    def locateElement(self,app_object,how,what,operate_method):
        located_element=self.find_element(how,what)
        print located_element
        print operate_method
        if operate_method=='click':
            self.extend_click_element(located_element)
        elif operate_method=='sendkey':
            send_data=GetData.GetData().getData(app_object)
            self.extend_send_data(located_element,send_data)


    def extend_click_element(self,located_element):
        self.click_element(located_element)

    def extend_send_data(self,located_element,send_data):
        self.send_data(located_element,send_data)