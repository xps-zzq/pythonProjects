# -*- coding: utf-8 -*-
import urllib

from bs4 import BeautifulSoup
from selenium import webdriver
import time
import json


class demo(object):
    def __init__(self):
        # 使用selenium
        self.driver = webdriver.PhantomJS(executable_path="E:\\phantomjs-2.1.1-windows\\bin\phantomjs.exe")
        self.driver.maximize_window()

    # 登录QQ空间
    def get_shuoshuo(self, qq):
        start_url = 'http://user.qzone.qq.com/{}/311'.format(qq)
        self.driver.get(start_url)
        print start_url
        time.sleep(5)

        try:
            self.driver.find_element_by_id('login_div')
            print'login_div'
            a = True
        except:
            a = False
        print 'isLogin:{}'.format(str(a))
        if a:
            self.driver.switch_to.frame('login_frame')
            self.driver.find_element_by_id('switcher_plogin').click()
            self.driver.find_element_by_id('u').clear()  # 选择用户名框
            self.driver.find_element_by_id('u').send_keys('496268609')
            self.driver.find_element_by_id('p').clear()
            self.driver.find_element_by_id('p').send_keys('monster2016')
            self.driver.find_element_by_id('login_button').click()
            time.sleep(3)
        self.driver.implicitly_wait(5)

        # 验证码逻辑
        try:
            self.driver.switch_to.frame('login_frame')
            is_check = True
        except:
            is_check = False
        print 'isCheck:' + str(is_check)
        if is_check:
            input_code = raw_input('请输入验证码:')
            self.driver.find_element_by_id('capAns').send_keys(input_code)
            self.driver.find_element_by_id('submit').click()
        # 正文内容
        self.driver.implicitly_wait(5)
        self.driver.save_screenshot('1.png')
        # try:
        #     print 'QM_OwnerInfo_Icon'
        #     self.driver.find_element_by_id('QM_OwnerInfo_Icon')
        #     b = True
        # except:
        #     b = False
        # print b
        # self.driver.save_screenshot('2.png')
        # print 'title' + self.driver.title
        # print 'current_url:{}'.format(self.driver.current_url)
        #
        # if b:
        # 获取说说逻辑
        print 'current_url:{}'.format(self.driver.current_url)
        self.driver.implicitly_wait(5)
        try:
            self.driver.switch_to.frame('app_canvas_frame')
            is_content = True
        except:
            is_content = False
        print 'is_content:{}'.format(str(is_content))
        if is_content:
            # content = self.driver.find_elements_by_css_selector('.content')
            # stime = self.driver.find_elements_by_css_selector('.c_tx.c_tx3.goDetail')
            # self.driver.save_screenshot('3.png')
            # for con, sti in zip(content, stime):
            #     data = {
            #         'time': sti.text,
            #         'shuos': con.text
            #     }
            #     print json.dumps(data, encoding="UTF-8", ensure_ascii=False)
            # pages = self.driver.page_source
            # soup = BeautifulSoup(pages, 'lxml')
            hp = self.driver.find_elements_by_class_name('img-attachments-inner')
            ho = ''
            for ho in hp:
                hq = ho.find_elements_by_tag_name('a')
                for tg in hq:
                    try:
                        linkF = tg.get_attribute('href')
                        print linkF
                    except:
                        print ('something was wrong!')
        cookie = self.driver.get_cookies()
        cookie_dict = []
        for c in cookie:
            ck = "{0}={1};".format(c['name'], c['value'])
            cookie_dict.append(ck)
        i = ''
        for c in cookie_dict:
            i += c
        print('Cookies:', i)
        print("==========完成================")

        self.driver.close()
        self.driver.quit()

    def code(self):
        # 切入登陆
        self.driver.switch_to.frame('login_frame')
        input_code = raw_input('请输入验证码:')
        self.driver.find_element_by_id('capAns').send_keys(input_code)
        self.driver.find_element_by_id('submit').click()

    # 将数据写入文件
    # TODO 下载图片
    def writeInFile(self):
        print ''

    def hasImg(self):
        shuoshuo_img = self.driver.find_element_by_css_selector('img-attachments-inner clearfix')


if __name__ == '__main__':
    qq = demo()
    qq.get_shuoshuo('496268609')
