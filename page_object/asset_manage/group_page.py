from page_object.login_page import login_page
from page_element_data.asset_manage.group_data import group_manage_element_data
from config.file import screenshot

class group_manage_add_page(group_manage_element_data):
    def group_add(self,group_data):
        try:
            self.login_page = login_page(group_data)
            self.driver = self.login_page.login()

            self.AST = self.login_page.login_pass()
            if self.AST == "AST":
                self.driver.implicitly_wait(10)
                self.driver.find_element_by_xpath(self.navigation).click()
                self.driver.implicitly_wait(10)
                self.driver.find_element_by_xpath(self.asset_menu).click()
                self.driver.implicitly_wait(10)
                self.driver.find_element_by_xpath(self.group_menu).click()
                self.driver.implicitly_wait(10)
                self.driver.find_element_by_xpath(self.group_button).click()
                self.driver.implicitly_wait(10)

                self.driver.find_element_by_xpath(self.server_group).send_keys(self.server_group_data)
                self.driver.find_element_by_xpath(self.describe).send_keys(self.describe_data)
                self.driver.find_element_by_xpath(self.choice_server).send_keys(self.host_name_data)
                self.driver.find_element_by_xpath(self.server_right).click()

                self.driver.find_element_by_xpath(self.submit_button).click()

            else:
                self.driver.get_screenshot_as_file(screenshot())
                print('登录有误！！！')
        except Exception as e:
            self.driver.get_screenshot_as_file(screenshot())
            print('主机添加页面有误！！！', e)

    def group_add_pass(self):
        add_pass = self.login_page.pulic_add_pass()
        return add_pass

    def group_add_error(self):
        add_error = self.login_page.pulic_add_error()
        return add_error

    def tearDown(self):
        self.login_page.tearDown()