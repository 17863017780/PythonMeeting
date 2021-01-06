import time
from selenium.webdriver import firefox
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import config

firefox_options = Options()
firefox_options.add_argument('--no-sandbox')
firefox_options.add_argument('--disable-dev-shm-usage')
#禁用图片
# firefox_options.add_argument('blink-settings=imagesEnabled=false')
firefox_options.add_argument('--disable-gpu')
#无头浏览
# firefox_options.add_argument('--headless')
firefox = webdriver.Firefox(firefox_options=firefox_options)

# chrome_options = webdriver.ChromeOptions()
# #驱动路径 谷歌的驱动存放路径
# path = r'D:\SoftWare\ChromeDriver\chromedriver.exe'
# prefs = {
#     'profile.default_content_setting_values': {
#         'images': 2,  # 禁用图片的加载
#         'css': 2,  # 禁用图片的加载
#         'javascript': 2  # 禁用js，可能会导致通过js加载的互动数抓取失效
#     }
# }
# chrome_options.add_experimental_option("prefs", prefs)
# chrome_options.add_argument('blink-settings=imagesEnabled=false')
# firefox= webdriver.Chrome(
#     executable_path=path, chrome_options=chrome_options
# )


#这个是显示的
# firefox = webdriver.Firefox()
# firefox.maximize_window()
login_url = 'http://ssa.jd.com/sso/login?ReturnUrl=http%3A%2F%2Fjmrs.jd.com%2Fsaas%2Fsso#/'

# 保存文件的方法
def save_content(param, content):
    file = open(param, 'w')
    file.write(content)
    return True


def login():
    firefox.get(login_url)
    # print("this is running")
    firefox.find_element_by_id('username').send_keys(config.ACCOUNT[0]['username'])
    print(config.ACCOUNT[0]['username']+'1324'+config.ACCOUNT[0]['pwd'])
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

# if __name__ == '__main__':
#     login()

