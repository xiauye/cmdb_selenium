from selenium.webdriver.support.select import Select
from page_object.login_page import login_page
from page_element_data.asset_manage.cabinet_data import cabinet_element_data
from config.file import screenshot
class cabinet_manage_add_page(cabinet_element_data):
    def cabinet_add(self,cabinet_data):
        try:
            self.login_page = login_page(cabinet_data)
            self.driver = self.login_page.login()

            self.AST = self.login_page.login_pass()
            if self.AST == "AST":
                self.driver.implicitly_wait(10)
                self.driver.find_element_by_xpath(self.navigation).click()
                self.driver.implicitly_wait(10)
                self.driver.find_element_by_xpath(self.asset_menu).click()
                self.driver.implicitly_wait(10)
                self.driver.find_element_by_xpath(self.cabinet_menu).click()
                self.driver.implicitly_wait(10)
                self.driver.find_element_by_xpath(self.cabinet_button).click()
                self.driver.implicitly_wait(10)

                Select(self.driver.find_element_by_xpath(self.computer)).select_by_visible_text(self.computer_data)
                self.driver.find_element_by_xpath(self.cabinet).send_keys(self.cabinet_data)
                self.driver.find_element_by_xpath(self.describe).send_keys(self.describe_data)
                self.driver.find_element_by_xpath(self.choice_server).send_keys(self.host_name_data)
                self.driver.find_element_by_xpath(self.server_right_button).click()

                self.driver.find_element_by_xpath(self.submit_button).click()
            else:
                self.driver.get_screenshot_as_file(screenshot())
                print('登录有误！！！')
        except Exception as e:
            self.driver.get_screenshot_as_file(screenshot())
            print('主机添加页面有误！！！', e)

    def cabinet_add_pass(self):
        add_pass = self.login_page.pulic_add_pass()
        return add_pass

    def cabinet_add_error(self):
        add_error = self.login_page.pulic_add_error()
        return add_error

    def tearDown(self):
        self.login_page.tearDown()