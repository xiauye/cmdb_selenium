import unittest
from page_object.login_page import login_page
from config.file import xlrd_file

class login(unittest.TestCase):
    def login_test_data(self):
        login_data = xlrd_file(sheet_name="login",xlsx_path="/data/data_source/asset_manager_data.xlsx")
        return login_data

    def test_login_pass_1(self):
        u'''用户名正确、密码正确，登录成功'''
        self.login_data = login().login_test_data()[0]
        self.login_page = login_page(self.login_data)
        self.login_page.login()
        login_pass = self.login_page.login_pass()
        self.assertEqual('AST',login_pass,'登录成功')
        print('11111')
        self.login_page.tearDown()

    def test_login_error_2(self):
        u'''用户名错误、密码正确，登录失败'''
        self.login_data = login().login_test_data()[1]
        self.login_page = login_page(self.login_data)
        self.login_page.login()
        user_ps_error = self.login_page.login_user_ps_error()
        self.assertEqual('账号密码不匹配', user_ps_error, '登录失败')
        print('22222')
        self.login_page.tearDown()

    def test_login_error_3(self):
        u'''用户名正确、密码错误，登录失败'''
        self.login_data = login().login_test_data()[2]
        self.login_page = login_page(self.login_data)
        self.login_page.login()
        user_ps_error = self.login_page.login_user_ps_error()
        self.assertEqual('账号密码不匹配', user_ps_error, '登录失败')
        print('333333')
        self.login_page.tearDown()

    def test_login_error_4(self):
        u'''用户名正确、密码错误，登录失败'''
        self.login_data = login().login_test_data()[3]
        self.login_page = login_page(self.login_data)
        self.login_page.login()
        user_ps_null_error = self.login_page.login_user_ps_null_error()
        self.assertEqual('AdminSet',user_ps_null_error,'登录失败')
        print('44444')
        self.login_page.tearDown()

    def test_login_error_5(self):
        u'''用户名正确、密码错误，登录失败'''
        self.login_data = login().login_test_data()[4]
        self.login_page = login_page(self.login_data)
        self.login_page.login()
        user_ps_null_error = self.login_page.login_user_ps_null_error()
        self.assertEqual('AdminSet', user_ps_null_error,'登录失败')
        print('55555')
        self.login_page.tearDown()


'''
    def test_login(self):
        self.login_data = login().test_data()
        for data in self.login_data:
            username = data['username']
            password = data['password']
            if username =='admin' and password=='admin123':
                self.login_page = login_page(self.login_data)
                self.login_page.login()
                login_pass = self.login_page.login_pass()
                self.assertEqual('AST',login_pass,'登录成功')
                self.login_page.tearDown()
            elif username =='admin1' and password=='admin123':
                self.login_page = login_page(self.login_data)
                self.login_page.login()
                user_ps_error = self.login_page.login_user_ps_error()
                self.assertEqual('账号密码不匹配', user_ps_error, '登录失败')
                print('22222')
                self.login_page.tearDown()
            else:
                print('没有你要的数据')
'''

if __name__ == '__main__':
    login()

