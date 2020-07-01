import time
from selenium.webdriver import firefox
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import config

firefox_options = Options()
firefox_options.add_argument('--no-sandbox')
firefox_options.add_argument('--disable-dev-shm-usage')
firefox_options.add_argument('blink-settings=imagesEnabled=false')
firefox_options.add_argument('--disable-gpu')
firefox_options.add_argument('--headless')
# 这个就是让浏览器不显示在gpu上
firefox = webdriver.Firefox(firefox_options=firefox_options)

#这个是显示的
# firefox = webdriver.Firefox()
# firefox.maximize_window()
login_url = 'https://jmrs.jd.com/saas/sso#/'

# 保存文件的方法
def save_content(param, content):
    file = open(param, 'w')
    file.write(content)
    return True


def login():
    firefox.get(login_url)
    # print("this is running")
    firefox.find_element_by_id('username').send_keys(config.ACCOUNT[0]['username'])
    firefox.find_element_by_id('password').send_keys(config.ACCOUNT[0]['pwd'])
    firefox.find_element_by_class_name('formsubmit_btn').click()
    time.sleep(1)
    # current_url = firefox.current_url
    # print("the url is :" + current_url )
    cookie = [item["name"] + "=" + item["value"] for item in firefox.get_cookies()]
    cookie_string = ';'.join(item for item in cookie)
    print(" the cookie is :" +cookie_string)
    if( cookie_string.__len__() != 0):
        config.COOKIE =str(cookie_string)
    firefox.close()
