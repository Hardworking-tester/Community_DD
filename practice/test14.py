# encoding:utf-8
from appium import webdriver
from time import sleep
from Data import get_number_by_data,ReadExcel
zhuce_excelpath="F:\\Community_DD\\Data\zhuce.xls"
zhuce_sheet_name="zhuce_data"

table=ReadExcel.ReadExcel().getTableBySheetName(zhuce_excelpath,zhuce_sheet_name)

data_list=[table.cell_value(0,2),table.cell_value(0,3),table.cell_value(0,4),table.cell_value(0,5)]
desired_caps={'platformName':'Android','platformVersion':'4.4','deviceName':'SM-G3608','appPackage':'com.dinghe.dingding.community','appActivity':'.SplashActivity'}
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
sleep(5)
driver.find_element_by_id("com.dinghe.dingding.community:id/login_register").click()
sleep(2)
driver.find_element_by_id("com.dinghe.dingding.community:id/zcone_re2").click()
sleep(2)
driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'五行嘉园')]").click()
sleep(2)
driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'666')]").click()
sleep(2)
driver.find_element_by_id("com.dinghe.dingding.community:id/zhuce_next1").click()
sleep(2)
driver.find_element_by_id("com.dinghe.dingding.community:id/zcone_sfqr_Et1").send_keys(int(data_list[0]))
driver.find_element_by_id("com.dinghe.dingding.community:id/zcone_sfqr_Et2").send_keys(int(data_list[1]))
driver.find_element_by_id("com.dinghe.dingding.community:id/zcone_sfqr_Et3").send_keys(int(data_list[2]))
driver.find_element_by_id("com.dinghe.dingding.community:id/zcone_sfqr_Et4").send_keys(int(data_list[3]))
driver.find_element_by_id("com.dinghe.dingding.community:id/zhuce_two_next").click()
sleep(2)
driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'获取验证码')]").click()
sleep(1)
driver.find_element_by_id("com.dinghe.dingding.community:id/edi_yanzhengma").send_keys("1234")
driver.find_element_by_id("com.dinghe.dingding.community:id/edittext").send_keys("w11111111")
driver.hide_keyboard()
driver.find_element_by_id("com.dinghe.dingding.community:id/zcone_three_final").click()