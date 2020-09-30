import unittest
from config.file import xlrd_file,write_excel
from page_object.asset_manage.host_page import host_manage_add_page,host_manage_update_page


class host_manege_add(unittest.TestCase):
    def host_data(self):
        host_data = xlrd_file(sheet_name="host_manage_add", xlsx_path="/data/data_source/asset_manager_data.xlsx")
        return host_data

    def test_host_manege_add_pass(self):
        u"""主机管理add：增加成功"""
        try:
            self.host_data = host_manege_add().host_data()[0]
            host_page = host_manage_add_page(self.host_data)
            host_add = host_page.host_add(self.host_data)
            self.host_add_pass = host_page.host_add_pass()
            self.assertEqual('增加成功！',self.host_add_pass,msg='主机增加成功')
            host_page.tearDown()

            target_list = [('机房名称', 'host_name', host_add)]
            write_excel(target_list)
        except Exception as e:
            print(e)

    def test_host_manege_add_error_1(self):
        u"""主机管理add：增加失败"""
        try:
            self.host_data = host_manege_add().host_data()[1]
            print('self.host_data',self.host_data)
            host_page = host_manage_add_page(self.host_data)
            host_page.host_add(self.host_data)
            self.host_add_error = host_page.host_add_error()
            print('self.host_add_pass',self.host_add_error)
            self.assertEqual('增加失败！',self.host_add_error,msg='主机增加失败！')
            host_page.tearDown()
        except Exception as e:
            print(e)

    def test_host_manege_add_error_2(self):
        u"""主机管理add：ip格式错误，增加失败"""
        try:
            self.host_data = host_manege_add().host_data()[2]
            print('self.host_data',self.host_data)
            host_page = host_manage_add_page(self.host_data)
            host_page.host_add(self.host_data)
            self.host_add_error = host_page.host_add_error()
            self.assertEqual('增加失败！',self.host_add_error,msg='主机增加失败！')
            host_page.tearDown()
        except Exception as e:
            print(e)

    def test_host_manege_add_error_3(self):
        u"""主机管理add：上架时间格式有误，增加失败"""
        try:
            self.host_data = host_manege_add().host_data()[3]
            print('self.host_data', self.host_data)
            host_page = host_manage_add_page(self.host_data)
            host_page.host_add(self.host_data)
            self.host_add_error = host_page.host_add_error()
            self.assertEqual('增加失败！', self.host_add_error, msg='主机增加失败！')
            host_page.tearDown()
        except Exception as e:
            print(e)

    def test_host_manege_add_error_4(self):
        u"""主机管理add：主机名为空，增加失败"""
        try:
            self.host_data = host_manege_add().host_data()[4]
            print('self.host_data', self.host_data)
            host_page = host_manage_add_page(self.host_data)
            host_page.host_add(self.host_data)
            self.host_add_error = host_page.host_add_error()
            self.assertEqual('增加失败！', self.host_add_error, msg='主机增加失败！')
            host_page.tearDown()
        except Exception as e:
            print(e)

class host_manege_update(unittest.TestCase):
    def host_data(self):
        host_data = xlrd_file(sheet_name="host_manage_update", xlsx_path="/data/data_source/asset_manager_data.xlsx")
        return host_data

    def test_host_manege_update_pass(self):
        u"""主机管理update：修改成功"""
        try:
            self.host_data = host_manege_update().host_data()[0]
            host_page = host_manage_update_page(self.host_data)
            host_page.host_update(self.host_data)
            self.host_update_pass = host_page.host_update_pass()
            self.assertIn('资产管理系统',self.host_update_pass,msg='主机修改成功')
            host_page.tearDown()
        except Exception as e:
            print(e)

    def test_host_manege_update_error_1(self):
        u"""主机管理update：ip格式错误，修改失败"""
        try:
            self.host_data = host_manege_update().host_data()[1]
            host_page = host_manage_update_page(self.host_data)
            host_page.host_update(self.host_data)
            self.host_update_error = host_page.host_update_error()
            self.assertEqual('增加失败！',self.host_update_error,msg='主机修改失败！')
            host_page.tearDown()
        except Exception as e:
            print(e)

if __name__ == '__main__':
    # host_manege_add()
    host_manege_update()