# encoding:utf-8
from Action import ZhuCe_yezhu
import unittest
from appium import webdriver
from time import sleep
#业主家属注册
class ZhuCeyezhujiashu(unittest.TestCase):


    def setUp(self):
        desired_caps={'platformName':'Android','platformVersion':'4.4','deviceName':'SM-G3608','appPackage':'com.dinghe.dingding.community','appActivity':'.SplashActivity','resetKeyboard':True}
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.s=ZhuCe_yezhu.ZhuCe(self.driver)

        sleep(5)

    def testZhuce(self):
        pp=self.s
        driver=pp.getoperateElementMethodAndData1()
        self.assert_Success(driver)

    def assert_Success(self,driver):
        driver.find_element_by_id("com.dinghe.dingding.community:id/tab_mine").click()
        sleep(2)
        jifen= driver.find_element_by_id("com.dinghe.dingding.community:id/my_account").text
        print jifen
        self.assertEqual(jifen,'1500','failed to register')
    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main()