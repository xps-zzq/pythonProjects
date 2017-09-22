# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from selenium import webdriver
import cookielib
import time

# 使用selenium
from selenium.webdriver.support.wait import WebDriverWait


class qq(object):
    def __init__(self, qq_code='', *args, **kwargs):
        self.qq_code = qq_code
        self.driver = webdriver.PhantomJS(executable_path="E:\\phantomjs-2.1.1-windows\\bin\phantomjs.exe")
        self.driver.maximize_window()

    # 登录QQ空间
    def get_shuoshuo(self):
        start_url = 'http://user.qzone.qq.com/{}/311'.format(self.qq_code)
        self.driver.get(start_url)
        print start_url
        time.sleep(3)
        try:
            self.driver.find_element_by_id('login_div')
            a = True
        except:
            a = False
        if a:
            self.driver.save_screenshot('1.png')
            self.driver.switch_to.frame('login_frame')
            if not self.fastLogin():
                print 'login..'
                self.driver.find_element_by_id('switcher_plogin').click()
                self.driver.find_element_by_id('u').clear()  # 选择用户名框
                self.driver.find_element_by_id('u').send_keys('49626809')
                self.driver.find_element_by_id('p').clear()
                self.driver.find_element_by_id('p').send_keys('monster2016')
                self.driver.find_element_by_id('login_button').click()
            else:
                print 'fast_login..'
            time.sleep(3)
            self.driver.implicitly_wait(5)
        wait = WebDriverWait(self.driver, 3000)
        self.driver.save_screenshot('2.png')
        try:
            print 'QM_OwnerInfo_Icon'
            self.driver.find_element_by_id('QM_OwnerInfo_Icon')
            b = True
        except:
            b = False
        print str(b)
        if b:
            print 'content...'
            self.driver.switch_to.frame('app_canvas_frame')
            content = self.driver.find_elements_by_css_selector('.content')
            stime = self.driver.find_elements_by_css_selector('.c_tx.c_tx3.goDetail')
            for con, sti in zip(content, stime):
                data = {
                    'time': sti.text,
                    'shuos': con.text
                }
                print(data)
            pages = self.driver.page_source
            soup = BeautifulSoup(pages, 'lxml')
        self.cookie()

        self.driver.close()
        self.driver.quit()

    def fastLogin(self):
        try:
            self.driver.switch_to.frame('login_frame')
            fast_btn = self.driver.find_element_by_id('img_out_496268609')
            print fast_btn
            if len(fast_btn):
                is_fast_login = True
        except:
            is_fast_login = False
        print 'is_fast_login:' + str(is_fast_login)
        return is_fast_login

    def input_code(self):
        self.driver.switch_to.frame()

    def cookie(self):
        # 设置保存cookie的文件，同级目录下的cookie.txt
        file = open('cookie.txt','wb')
        for cookie in self.driver.get_cookies():
            file.write("%s : %s" % (cookie['name'], cookie['value']))
            file.write('\n')
            print "%s : %s" % (cookie['name'], cookie['value'])


if __name__ == '__main__':
    qq = qq(qq_code='496268609')
    qq.get_shuoshuo()
