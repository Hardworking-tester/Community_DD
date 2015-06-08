#encoding:utf-8
from pyadb import ADB
from appium import webdriver
import os
from time import sleep
pp=os.popen("adb shell ps")
print pp.read()
