from selenium import webdriver
import random,string



def driver(browser):
    try:
        path = "http://127.0.0.1:8000/"
        if browser == 'Chrome' or browser == 'chrome':
            driver = webdriver.Chrome()
            driver.get(path)
            driver.maximize_window()
            return driver
        elif browser == 'Firefox' or browser == 'firefox':
            driver = webdriver.Firefox()
            driver.get(path)
            driver.maximize_window()
            return driver
        elif browser == 'Opera' or browser == 'opera':
            driver = webdriver.Opera()
            driver.get(path)
            driver.maximize_window()
            return driver
        elif browser == 'Ie' or browser == 'ie':
            driver = webdriver.Ie()
            driver.get(path)
            driver.maximize_window()
            return driver
        elif browser == 'PhantomJS' or browser == 'phantomjs':
            driver = webdriver.PhantomJS()
            driver.get(path)
            driver.maximize_window()
            return driver
        else:
            print('未找到此浏览器，您可以使用“firefox”、“chrome”、“ie”或“phantomjs”')
            raise EOFError
    except Exception as e:
        print("启动浏览器出现异常：%s" % str(e))
        raise EOFError


#生成随机数四位
def generate_random():
    s = ""
    for i in range(0, 4):
        if random.randint(0, 1) == 0:
            # 生成字母
            s = s + chr(random.randint(65, 90))
        else:
            # 生成数字
            s = s + str(random.randint(0, 9))
    print("随机数:",s)
    return s

