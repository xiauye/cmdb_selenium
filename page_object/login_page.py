from page_element_data.login_data import login_element_data
from config.driver_base import driver
from config.file import screenshot

class login_page(login_element_data):
    def login(self):
        try:
            self.driver = driver(browser='Chrome')
            adminset = self.driver.find_element_by_xpath(self.AdminSet).text
            if adminset == 'AdminSet':
                self.driver.find_element_by_name(self.username).send_keys(self.username_data)
                self.driver.find_element_by_name(self.password).send_keys(self.password_data)
                self.driver.find_element_by_xpath(self.denglu).click()
                return self.driver
            else:
                current_url = self.driver.current_url
                print('地址可能有误！！！',adminset,self.AdminSet,current_url)
                self.driver.get_screenshot_as_file(screenshot())
                self.driver.quit()
        except Exception as e:
            self.driver.get_screenshot_as_file(screenshot())

    def login_pass(self):
        try:
            AST = self.driver.find_element_by_xpath(self.AST).text
            return AST
        except Exception as e:
            self.driver.get_screenshot_as_file(screenshot())

    def login_user_ps_error(self):
        try:
            user_ps_error  = self.driver.find_element_by_xpath(self.error).text
            return user_ps_error
        except Exception as e:
            self.driver.get_screenshot_as_file(screenshot())

    def login_user_ps_null_error(self):
        try:
            user_ps_null_error = self.driver.find_element_by_xpath(self.AdminSet).text
            return user_ps_null_error
        except Exception as e:
            self.driver.get_screenshot_as_file(screenshot())

    def tearDown(self):
        self.driver.quit()


    # public
    def pulic_add_pass(self):  # 增加成功！
        try:
            self.driver.implicitly_wait(10)
            add_pass = self.driver.find_element_by_xpath(self.add_pass).text
            return add_pass
        except Exception as e:
            self.driver.get_screenshot_as_file(screenshot())
            self.tearDown()
            print(e)


    def pulic_add_error(self): # 增加失败！
        try:
            self.driver.implicitly_wait(10)
            add_pass = self.driver.find_element_by_xpath(self.add_fail).text
            return add_pass
        except Exception as e:
            self.driver.get_screenshot_as_file(screenshot())
            self.tearDown()
            print(e)