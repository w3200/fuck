# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
# 引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains


class Zhuce(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.vip.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_zhuce(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_link_text(u"注册").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=nXnONeF2x7MyHv5XnM9lR12UDkzuWwCeiIsnGR0E9R0PhyjGu0usTsvJlgkH/TXjmvAaRdfZLMfLzw2jPVAKf3l16sn8EarBwwtlrbdIkrM= | ]]
        driver.find_element_by_id("J_mobile_name").clear()
        driver.find_element_by_id("J_mobile_name").send_keys("15652653590")
        time.sleep(3)
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=nXnONeF2x7MyHv5XnM9lR12UDkzuWwCeiIsnGR0E9R0PhyjGu0usTsvJlgkH/TXjmvAaRdfZLMfLzw2jPVAKf3l16sn8EarBwwtlrbdIkrM= | ]]
        driver.find_element_by_id("J_mobile_pwd").clear()
        driver.find_element_by_id("J_mobile_pwd").send_keys("wangpeng0000")
        time.sleep(3)
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=nXnONeF2x7MyHv5XnM9lR12UDkzuWwCeiIsnGR0E9R0PhyjGu0usTsvJlgkH/TXjmvAaRdfZLMfLzw2jPVAKf3l16sn8EarBwwtlrbdIkrM= | ]]
        driver.find_element_by_id("J_mobile_confirm_pwd").clear()
        driver.find_element_by_id("J_mobile_confirm_pwd").send_keys("wangpeng0000")
        time.sleep(3)
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=nXnONeF2x7MyHv5XnM9lR12UDkzuWwCeiIsnGR0E9R0PhyjGu0usTsvJlgkH/TXjmvAaRdfZLMfLzw2jPVAKf3l16sn8EarBwwtlrbdIkrM= | ]]
        driver.find_element_by_id("J_mobile_reg_button").click()

    #登录
    def test_denglu(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=nXnONeF2x7MyHv5XnM9lR12UDkzuWwCeiIsnGR0E9R0PhyjGu0usTsvJlgkH/TXjmvAaRdfZLMfLzw2jPVAKf3l16sn8EarBwwtlrbdIkrM= | ]]
        driver.find_element_by_css_selector("span.order-in > a").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=nXnONeF2x7MyHv5XnM9lR12UDkzuWwCeiIsnGR0E9R0PhyjGu0usTsvJlgkH/TXjmvAaRdfZLMfLzw2jPVAKf0rjfHsXB6tGwcayo/qtQOM= | ]]
        # 此处应该有一个窗口切换
        all_handles = driver.window_handles
        # 切换到第二个窗口
        driver.switch_to.window(all_handles[1])
        time.sleep(3)
        driver.find_element_by_id("J_login_name").clear()
        driver.find_element_by_id("J_login_name").send_keys("15652653590")
        time.sleep(3)
        driver.find_element_by_id("J_login_pwd").clear()
        driver.find_element_by_id("J_login_pwd").send_keys("wangpeng0000")
        time.sleep(3)
        driver.find_element_by_id("J_login_submit").click()

    #男装
    def test_nanzhuang(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()
        driver.find_element_by_link_text(u"男装").click()
        time.sleep(3)
        # 点击完页面往上滚一些
        js = "window.scrollTo(0,600);"
        driver.execute_script(js)
        time.sleep(2)







    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
