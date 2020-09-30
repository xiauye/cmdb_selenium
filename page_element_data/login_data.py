from config.file import element_yaml

from config.file import xlrd_file
class login_element_data():
    def __init__(self,login_data):
        # 元素
        self.login_element = element_yaml(yaml_path="/data/element_data/login.yaml")
        self.AdminSet = self.login_element['login'].get('AdminSet')
        self.username = self.login_element['login'].get('username')
        self.password = self.login_element['login'].get('password')
        self.denglu = self.login_element['login'].get('denglu')
        self.error = self.login_element['login'].get('error')
        self.AST = self.login_element['login'].get('AST')

        # 测试数据
        # login_data1 = xlrd_file(sheet_name="login", xlsx_path="/data/data_source/asset_manager_data.xlsx")
        # self.login_data = login_data1[login_data]
        self.username_data = login_data["username"]
        self.password_data = login_data['password']


        # public
        self.add_pass = self.login_element['login'].get('add_pass')
        self.add_fail = self.login_element['login'].get('add_fail')


