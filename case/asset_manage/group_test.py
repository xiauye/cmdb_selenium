import unittest
from config.file import xlrd_file,write_excel
from page_object.asset_manage.group_page import group_manage_add_page


class group_manage_add(unittest.TestCase):
    def group_data(self):
        group_data = xlrd_file(sheet_name="group_manage_add", xlsx_path="/data/data_source/asset_manager_data.xlsx")
        return group_data

    def test_group_manege_add_pass(self):
        u"""属组管理add：增加成功"""
        try:
            self.data = group_manage_add().group_data()[0]
            self.cabinet_add_page = group_manage_add_page(self.data)
            self.cabinet_add_page.group_add(self.data)

            group_add_pass = self.cabinet_add_page.group_add_pass()
            self.assertEqual('增加成功！',group_add_pass,msg='增加成功')
            self.cabinet_add_page.tearDown()
        except Exception as e:
            print(e)

    def test_group_manege_add_error_1(self):
        u"""属组管理add：增加成功"""
        try:
            self.data = group_manage_add().group_data()[1]
            self.cabinet_add_page = group_manage_add_page(self.data)
            self.cabinet_add_page.group_add(self.data)

            group_add_error = self.cabinet_add_page.group_add_error()
            self.assertEqual('增加失败！',group_add_error,msg='增加失败')
            self.cabinet_add_page.tearDown()
        except Exception as e:
            print(e)