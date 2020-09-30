from selenium.webdriver.support.select import Select

from page_element_data.asset_manage.host_data import host_manage_element_data
from page_object.login_page import login_page
from config.file import screenshot
import time

class host_manage_add_page(host_manage_element_data):
    def host_add(self,host_data):
        try:
            self.login_page = login_page(host_data)
            self.driver = self.login_page.login()

            self.AST = self.login_page.login_pass()
            if self.AST == 'AST':
                self.driver.implicitly_wait(10)
                self.driver.find_element_by_xpath(self.navigation).click()
                self.driver.find_element_by_xpath(self.asset_menu).click()
                self.driver.find_element_by_xpath(self.host_menu).click()
                self.driver.implicitly_wait(10)
                self.driver.find_element_by_xpath(self.add_button).click()
                self.driver.implicitly_wait(10)
                add_host_content = self.driver.find_element_by_xpath(self.add_host_content).text
                assert '添加主机条目' == add_host_content

                self.driver.find_element_by_xpath(self.host_name).send_keys(self.host_name_data)
                self.driver.find_element_by_xpath(self.ip).send_keys(self.ip_data)

                # Select(self.driver.find_element_by_xpath(self.number).send_keys(self.number_data))
                Select(self.driver.find_element_by_xpath(self.computer)).select_by_visible_text(self.computer_data)
                self.driver.implicitly_wait(10)

                self.driver.find_element_by_xpath(self.other_ip).send_keys(self.other_ip_data)
                self.driver.find_element_by_xpath(self.asset_number).send_keys(self.asset_number_data)

                Select(self.driver.find_element_by_xpath(self.device_type)).select_by_visible_text(self.device_type_data)
                Select(self.driver.find_element_by_xpath(self.device)).select_by_visible_text(self.device_data)

                self.driver.find_element_by_xpath(self.system).send_keys(self.system_data)
                self.driver.find_element_by_xpath(self.equipment).send_keys(self.equipment_data)
                self.driver.find_element_by_xpath(self.upper_time).send_keys(self.upper_time_data)
                self.driver.find_element_by_xpath(self.cpu_type).send_keys(self.cpu_type_data)
                self.driver.find_element_by_xpath(self.cpu_number).send_keys(self.cpu_number_data)
                self.driver.find_element_by_xpath(self.memory).send_keys(self.memory_data)
                self.driver.find_element_by_xpath(self.disk).send_keys(self.disk_data)
                self.driver.find_element_by_xpath(self.sn_number).send_keys(self.sn_number_data)
                self.driver.find_element_by_xpath(self.position).send_keys(self.position_data)
                self.driver.find_element_by_xpath(self.remarks).send_keys(self.remarks_data)

                self.driver.find_element_by_xpath(self.submit_button).click()

                return self.host_name_data
            else:
                self.driver.get_screenshot_as_file(screenshot())
                print('登录有误！！！')
        except Exception as e:
            self.driver.get_screenshot_as_file(screenshot())
            print('主机添加页面有误！！！',e)

    def host_add_pass(self):
        add_pass = self.login_page.pulic_add_pass()
        return add_pass

    def host_add_error(self):
        add_error = self.login_page.pulic_add_error()
        return add_error

    def tearDown(self):
        self.login_page.tearDown()


class host_manage_update_page(host_manage_element_data):
    def host_update(self,host_data):
        try:
            self.login_page = login_page(host_data)
            self.driver = self.login_page.login()

            self.AST = self.login_page.login_pass()
            if self.AST == 'AST':
                self.driver.implicitly_wait(10)
                self.driver.find_element_by_xpath(self.navigation).click()
                self.driver.find_element_by_xpath(self.asset_menu).click()
                self.driver.find_element_by_xpath(self.host_menu).click()
                self.driver.implicitly_wait(10)
                self.driver.find_element_by_xpath(self.update_button).click()
                self.driver.implicitly_wait(10)
                host_update = self.driver.find_element_by_xpath(self.host_update_news).text
                assert '修改主机信息' == host_update
                # self.driver.switch_to.default_content()
                iframe = self.driver.find_element_by_xpath(self.iframe)
                self.driver.switch_to.frame(iframe)
                self.driver.implicitly_wait(10)
                self.driver.find_element_by_xpath(self.host_name).clear()
                self.driver.find_element_by_xpath(self.host_name).send_keys(self.host_name_data)
                self.driver.find_element_by_xpath(self.ip).clear()
                self.driver.find_element_by_xpath(self.ip).send_keys(self.ip_data)

                # Select(self.driver.find_element_by_xpath(self.number).send_keys(self.number_data))
                Select(self.driver.find_element_by_xpath(self.computer)).select_by_visible_text(self.computer_data)

                self.driver.find_element_by_xpath(self.other_ip).clear()
                self.driver.find_element_by_xpath(self.other_ip).send_keys(self.other_ip_data)
                self.driver.find_element_by_xpath(self.asset_number).clear()
                self.driver.find_element_by_xpath(self.asset_number).send_keys(self.asset_number_data)

                Select(self.driver.find_element_by_xpath(self.device_type)).select_by_visible_text(self.device_type_data)
                Select(self.driver.find_element_by_xpath(self.device)).select_by_visible_text(self.device_data)

                self.driver.find_element_by_xpath(self.system).clear()
                self.driver.find_element_by_xpath(self.system).send_keys(self.system_data)
                self.driver.find_element_by_xpath(self.equipment).clear()
                self.driver.find_element_by_xpath(self.equipment).send_keys(self.equipment_data)
                self.driver.find_element_by_xpath(self.upper_time).clear()
                self.driver.find_element_by_xpath(self.upper_time).send_keys(self.upper_time_data)
                self.driver.find_element_by_xpath(self.cpu_type).clear()
                self.driver.find_element_by_xpath(self.cpu_type).send_keys(self.cpu_type_data)
                self.driver.find_element_by_xpath(self.cpu_number).clear()
                self.driver.find_element_by_xpath(self.cpu_number).send_keys(self.cpu_number_data)
                self.driver.find_element_by_xpath(self.memory).clear()
                self.driver.find_element_by_xpath(self.memory).send_keys(self.memory_data)
                self.driver.find_element_by_xpath(self.disk).clear()
                self.driver.find_element_by_xpath(self.disk).send_keys(self.disk_data)
                self.driver.find_element_by_xpath(self.sn_number).clear()
                self.driver.find_element_by_xpath(self.sn_number).send_keys(self.sn_number_data)
                self.driver.find_element_by_xpath(self.position).clear()
                self.driver.find_element_by_xpath(self.position).send_keys(self.position_data)
                self.driver.find_element_by_xpath(self.remarks).clear()
                self.driver.find_element_by_xpath(self.remarks).send_keys(self.remarks_data)
                self.driver.implicitly_wait(10)
                self.driver.find_element_by_xpath(self.preservation_button).click()
            else:
                self.driver.get_screenshot_as_file(screenshot())
                print('登录有误！！！')
        except Exception as e:
            self.driver.get_screenshot_as_file(screenshot())
            print('页面元素定位或者测试数据有误！！！',e)

    def host_update_pass(self):
        host_name_update = self.driver.find_element_by_xpath(self.host_name_update)
        return host_name_update

    def host_update_error(self):
        add_error = self.login_page.pulic_add_error()
        return add_error

    def tearDown(self):
        self.login_page.tearDown()