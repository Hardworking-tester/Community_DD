#encoding:utf-8
from appium import webdriver
from time import sleep
desired_caps={"platformName":"Android","platformVersion":"4.4.2","deviceName":"HONOR H30-L02","appPackage":"com.bd.community","appActivity":"com.bd.community.SplashActivity"}
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
sleep(5)
driver.find_element_by_id("com.bd.community:id/login_loginaccount").send_keys("wwg2")
sleep(2)
driver.find_element_by_id("com.bd.community:id/login_loginpassword").send_keys("111111")
sleep(2)
driver.find_element_by_id("com.bd.community:id/loginRememberMeCheckBox").click()
driver.find_element_by_id("com.bd.community:id/login").click()
sleep(3)
driver.find_element_by_id("com.bd.community:id/home_tab_fwsq").click()
sleep(2)
driver.find_element_by_id("com.bd.community:id/tv_wuye_fee").click()
sleep(2)
driver.find_element_by_id("com.bd.community:id/et_start_time").click()
sleep(2)
# driver.tap([(143,827)])
driver.find_element_by_xpath("//android.widget.NumberPicker[contains(@text,'2019年')]/android.widget.Button[contains(@index,'请输入邮箱或手机号码')]").click()
# element1=driver.find_element_by_xpath("//android.widget.EditText[contains(@index,'请输入邮箱或手机号码')]")#.send_keys('192519517@qq.com')
