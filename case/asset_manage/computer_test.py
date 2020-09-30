import unittest
from page_object.asset_manage.computer_page import computer_manage_add_page,computer_manage_update_page
from config.file import xlrd_file,write_excel

class computer_manage_add(unittest.TestCase):
    def computer_add_data(self):
        computer_data = xlrd_file(sheet_name="computer_manage_add",xlsx_path="/data/data_source/asset_manager_data.xlsx")
        return computer_data

    def test_computer_add_pass(self):
        u"""机房管理add:增加成功"""
        try:
            self.computer_data = computer_manage_add().computer_add_data()[0]
            self.computer_page = computer_manage_add_page(self.computer_data)
            computer_add = self.computer_page.computer_add(self.computer_data)
            computer_add_pass = self.computer_page.computer_add_pass()
            self.assertEqual('增加成功！', computer_add_pass, msg='增加成功')
            print('computer_add',computer_add)
            # 保存机房名称
            target_list = [('机房名称', 'computer_name', computer_add)]
            write_excel(target_list)
            self.computer_page.tearDown()
        except Exception as e:
            self.computer_page.tearDown()
            print(e)

    def test_computer_add_error_1(self):
        u"""机房管理add:移动电话位特殊字符，添加失败"""
        try:
            self.computer_data = computer_manage_add().computer_add_data()[1]
            self.computer_page = computer_manage_add_page(self.computer_data)
            self.computer_page.computer_add(self.computer_data)
            computer_add_error = self.computer_page.computer_add_error()
            self.assertEqual('增加失败！', computer_add_error, msg='增加失败')
            self.computer_page.tearDown()
        except Exception as e:
            self.computer_page.tearDown()
            print(e)

    def test_computer_add_error_2(self):
        u"""机房管理add:IP格式不正确，增加失败"""
        try:
            self.computer_data = computer_manage_add().computer_add_data()[2]
            self.computer_page = computer_manage_add_page(self.computer_data)
            self.computer_page.computer_add(self.computer_data)
            computer_add_error = self.computer_page.computer_add_error()
            self.assertEqual('增加失败！', computer_add_error, msg='增加失败')
            self.computer_page.tearDown()
        except Exception as e:
            self.computer_page.tearDown()
            print(e)

    def test_computer_add_error_3(self):
        u"""机房管理add:机房标识位空，增加失败"""
        try:
            self.computer_data = computer_manage_add().computer_add_data()[3]
            self.computer_page = computer_manage_add_page(self.computer_data)
            self.computer_page.computer_add(self.computer_data)

            computer_add_error = self.computer_page.computer_add_error()
            self.assertEqual('增加失败！', computer_add_error, msg='增加失败')
            self.computer_page.tearDown()
        except Exception as e:
            self.computer_page.tearDown()
            print(e)


'''
    def test_computer_add_pass(self):
        u"""机房管理add:增加成功"""
        try:
            self.computer_page = computer_manage_add_page(0)
            self.computer_page.computer_add()
            computer_add_pass = self.computer_page.computer_add_pass()
            self.assertEqual('增加成功！',computer_add_pass,msg='增加成功')
            print('11111')
            self.computer_page.tearDown()
        except Exception as e:
            self.computer_page.tearDown()
            print(e)

    def test_computer_add_error_1(self):
        u"""机房管理add:移动电话位特殊字符，添加失败"""
        try:
            self.computer_page = computer_manage_add_page(1)
            self.computer_page.computer_add()
            computer_add_error = self.computer_page.computer_add_error()
            self.assertEqual('增加失败！',computer_add_error,msg='增加失败')
            self.computer_page.tearDown()
        except Exception as e:
            self.computer_page.tearDown()
            print(e)

    def test_computer_add_error_2(self):
        u"""机房管理add:IP格式不正确，增加失败"""
        try:
            self.computer_page = computer_manage_add_page(2)
            self.computer_page.computer_add()
            computer_add_error = self.computer_page.computer_add_error()
            self.assertEqual('增加失败！', computer_add_error, msg='增加失败')
            print('3333')
            self.computer_page.tearDown()
        except Exception as e:
            self.computer_page.tearDown()
            print(e)

    def test_computer_add_error_3(self):
        u"""机房管理add:机房标识位空，增加失败"""
        try:
            self.computer_page = computer_manage_add_page(3)
            self.computer_page.computer_add()
            computer_add_error = self.computer_page.computer_add_error()
            self.assertEqual('增加失败！', computer_add_error, msg='增加失败')
            print('44444')
            self.computer_page.tearDown()
        except Exception as e:
            self.computer_page.tearDown()
            print(e)
'''

class computer_manage_update(unittest.TestCase):
    def computer_update_data(self):
        computer_data = xlrd_file(sheet_name="computer_manage_update",xlsx_path="/data/data_source/asset_manager_data.xlsx")
        return computer_data

    def test_computer_update_pass(self):
        u"""机房管理update:修改成功"""
        try:
            self.computer_data = computer_manage_update().computer_update_data()[0]
            self.computer_page = computer_manage_update_page(self.computer_data)
            self.computer_page.computer_update(self.computer_data)
            computer_pass = self.computer_page.computer_update_pass()
            self.assertIn('运维机房', computer_pass, msg='修改成功')
            self.computer_page.tearDown()
        except Exception as e:
            self.computer_page.tearDown()
            print(e)

    def test_computer_update_error_1(self):
        u"""机房管理update:移动电话位特殊字符，修改失败"""
        try:
            self.computer_data = computer_manage_update().computer_update_data()[1]
            self.computer_page = computer_manage_update_page(self.computer_data)
            computer_update_error = self.computer_page.computer_update_error()
            self.assertEqual('编辑失败！', computer_update_error, msg='增加失败')
            self.computer_page.tearDown()
        except Exception as e:
            self.computer_page.tearDown()
            print(e)

if __name__ == '__main__':
    computer_manage_add()
    # computer_manage_update()

