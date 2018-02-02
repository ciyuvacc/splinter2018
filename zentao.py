# -*- coding: utf-8 -*-

from splinter.browser import Browser
from time import sleep
import traceback
import time, sys

username = u"admin"
passwd = u"5d436e123#@"

	
login_url = "http://59.151.121.91:8787/zentao/user-login.html"
	
driver=Browser()	
def login():
	driver.visit(login_url)
		
	driver.fill("account",username)
		# sleep(1)
	driver.fill("password",passwd)
	driver.click_link_by_id("submit")
		
	#print u"等待验证码，自行输入..."	

def start():
	#driver=Browser(driver_name=driver_name)
	#river=Browser()
	driver.driver.set_window_size(1400, 1000)
	login()
	driver.click_link_by_href("/zentao/company/")
	# sleep(1)

		

if __name__ == '__main__':
	
	start()