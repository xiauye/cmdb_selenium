import unittest
from config.file import xlrd_file
from page_object.asset_manage.cabinet_page import cabinet_manage_add_page

class cabinet_manage_add(unittest.TestCase):
    def cabinet_add_data(self):
        cabinet_data = xlrd_file(sheet_name="cabinet_manage_add", xlsx_path="/data/data_source/asset_manager_data.xlsx")
        return cabinet_data

    def test_cabinet_add_pass(self):
        u"""机柜管理add：增加成功"""
        try:
            self.cabinet_data = cabinet_manage_add().cabinet_add_data()[0]
            self.cabinet_add_page = cabinet_manage_add_page(self.cabinet_data)
            self.cabinet_add_page.cabinet_add(self.cabinet_data)

            cabinet_add_pass = self.cabinet_add_page.cabinet_add_pass()
            self.assertEqual('增加成功！',cabinet_add_pass,msg='增加成功')
            self.cabinet_add_page.tearDown()
        except Exception as e:
            print(e)

    def test_cabinet_add_error_2(self):
        u"""机柜管理add：机柜为空，增加失败"""
        try:
            self.cabinet_data = cabinet_manage_add().cabinet_add_data()[1]
            self.cabinet_add_page = cabinet_manage_add_page(self.cabinet_data)
            self.cabinet_add_page.cabinet_add(self.cabinet_data)

            cabinet_add_pass = self.cabinet_add_page.cabinet_add_error()
            self.assertEqual('增加失败！', cabinet_add_pass, msg='增加失败')
            self.cabinet_add_page.tearDown()
        except Exception as e:
            print(e)

if __name__ == '__main__':
    cabinet_manage_add()