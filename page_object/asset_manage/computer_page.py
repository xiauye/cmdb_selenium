from page_element_data.asset_manage.computer_data import computer_manage_element_data
from config.file import screenshot
from page_object.login_page import login_page
import time

class computer_manage_add_page(computer_manage_element_data):
    def computer_add(self,computer_data):
        try:
            self.login_page = login_page(computer_data)
            self.driver = self.login_page.login()

            self.AST = self.login_page.login_pass()
            if self.AST == 'AST':
                self.driver.implicitly_wait(10)
                self.driver.find_element_by_xpath(self.navigation).click()
                self.driver.implicitly_wait(10)
                self.driver.find_element_by_xpath(self.asset_menu).click()
                self.driver.implicitly_wait(10)
                self.driver.find_element_by_xpath(self.computer_menu).click()
                self.driver.implicitly_wait(10)
                self.driver.find_element_by_xpath(self.add_button).click()
                self.driver.implicitly_wait(10)
                self.driver.find_element_by_xpath(self.sign).send_keys(self.sign_data)
                self.driver.implicitly_wait(10)
                self.driver.find_element_by_xpath(self.computer_name).send_keys(self.computer_name_data)
                self.driver.find_element_by_xpath(self.address).send_keys(self.address_data)
                self.driver.find_element_by_xpath(self.computer_phone).send_keys(self.computer_phone_data)
                self.driver.find_element_by_xpath(self.manager).send_keys(self.manager_data)
                self.driver.find_element_by_xpath(self.phone).send_keys(self.phone_data)
                self.driver.find_element_by_xpath(self.cabinet).send_keys(self.cabinet_data)
                self.driver.find_element_by_xpath(self.ip).send_keys(self.ip_data)
                self.driver.find_element_by_xpath(self.bandwidth).send_keys(self.bandwidth_data)
                self.driver.find_element_by_xpath(self.remarks).send_keys(self.remarks_data)
                self.driver.implicitly_wait(10)
                self.driver.find_element_by_xpath(self.submit_button).click()

                return self.computer_name_data
            else:
                self.driver.get_screenshot_as_file(screenshot())
        except Exception as e:
            self.driver.get_screenshot_as_file(screenshot())
            self.tearDown()
            print(e)

    def computer_add_pass(self):
        try:
            self.driver.implicitly_wait(10)
            add_pass = self.driver.find_element_by_xpath(self.add_pass).text
            return add_pass
        except Exception as e:
            self.driver.get_screenshot_as_file(screenshot())
            self.tearDown()
            print(e)

    def computer_add_error(self):
        try:
            self.driver.implicitly_wait(10)
            add_fail = self.driver.find_element_by_xpath(self.add_fail).text
            return add_fail
        except Exception as e:
            self.driver.get_screenshot_as_file(screenshot())
            self.tearDown()
            print(e)

    def tearDown(self):
        self.driver.quit()

class computer_manage_update_page(computer_manage_element_data):
    def computer_update(self,computer_data):
        try:
            self.login_page = login_page(computer_data)
            self.driver = self.login_page.login()

            self.AST = self.login_page.login_pass()
            if self.AST == 'AST':
                self.driver.implicitly_wait(10)
                self.driver.find_element_by_xpath(self.navigation).click()
                self.driver.implicitly_wait(10)
                self.driver.find_element_by_xpath(self.asset_menu).click()
                self.driver.implicitly_wait(10)
                self.driver.find_element_by_xpath(self.computer_menu).click()
                self.driver.implicitly_wait(10)
                self.driver.find_element_by_xpath(self.update_button).click()
                self.driver.implicitly_wait(10)
                self.driver.find_element_by_xpath(self.sign).clear()
                self.driver.find_element_by_xpath(self.sign).send_keys(self.sign_data)
                self.driver.find_element_by_xpath(self.computer_name).clear()
                self.driver.find_element_by_xpath(self.computer_name).send_keys(self.computer_name_data)
                self.driver.find_element_by_xpath(self.address).clear()
                self.driver.find_element_by_xpath(self.address).send_keys(self.address_data)
                self.driver.find_element_by_xpath(self.computer_phone).clear()
                self.driver.find_element_by_xpath(self.computer_phone).send_keys(self.computer_phone_data)
                self.driver.find_element_by_xpath(self.manager).clear()
                self.driver.find_element_by_xpath(self.manager).send_keys(self.manager_data)
                self.driver.find_element_by_xpath(self.phone).clear()
                self.driver.find_element_by_xpath(self.phone).send_keys(self.phone_data)
                self.driver.find_element_by_xpath(self.cabinet).clear()
                self.driver.find_element_by_xpath(self.cabinet).send_keys(self.cabinet_data)
                self.driver.find_element_by_xpath(self.ip).clear()
                self.driver.find_element_by_xpath(self.ip).send_keys(self.ip_data)
                self.driver.find_element_by_xpath(self.bandwidth).clear()
                self.driver.find_element_by_xpath(self.bandwidth).send_keys(self.bandwidth_data)
                self.driver.find_element_by_xpath(self.remarks).clear()
                self.driver.find_element_by_xpath(self.remarks).send_keys(self.remarks_data)
                self.driver.implicitly_wait(10)
                self.driver.find_element_by_xpath(self.submit_button).click()
            else:
                self.driver.get_screenshot_as_file(screenshot())
        except Exception as e:
            self.driver.get_screenshot_as_file(screenshot())
            self.tearDown()
            print(e)

    def computer_update_pass(self):
        try:
            self.driver.implicitly_wait(10)
            get_remarks = self.driver.find_element_by_xpath(self.get_remarks).text
            print('get_remarks',get_remarks)
            return get_remarks
        except Exception as e:
            self.driver.get_screenshot_as_file(screenshot())
            self.tearDown()
            print(e)

    def computer_update_error(self):
        try:
            self.driver.implicitly_wait(10)
            add_fail = self.driver.find_element_by_xpath(self.add_fail).text
            return add_fail
        except Exception as e:
            self.driver.get_screenshot_as_file(screenshot())
            self.tearDown()
            print(e)

    def tearDown(self):
        self.driver.quit()

