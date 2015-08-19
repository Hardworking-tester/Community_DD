# encoding:utf-8
from appium import webdriver
from time import sleep
from Data import get_number_by_data,ReadExcel


desired_caps={'platformName':'Android','platformVersion':'4.4','deviceName':'SM-G3608','appPackage':'com.dinghe.dingding.community','appActivity':'.SplashActivity'}
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
sleep(10)
driver.find_element_by_id("com.dinghe.dingding.community:id/tv_fangkeshouquan").click()
sleep(2)
driver.find_element_by_id("com.dinghe.dingding.community:id/shouquan").click()
sleep(2)
driver.find_element_by_id("com.dinghe.dingding.community:id/et_visitor_name").send_keys('wwg')
sleep(2)
driver.find_element_by_id("com.dinghe.dingding.community:id/et_start_time").click()
sleep(2)
driver.find_element_by_id("android:id/button1").click()
driver.find_element_by_id("com.dinghe.dingding.community:id/et_end_time").click()
driver.find_element_by_id("android:id/button1").click()
driver.find_element_by_id("com.dinghe.dingding.community:id/et_carnum").send_keys('heool')
driver.find_element_by_id("com.dinghe.dingding.community:id/et_beizhu").send_keys('wwggh')
driver.find_element_by_id("com.dinghe.dingding.community:id/btn_commit").click()
sleep(2)
element=[]
element.__len__()