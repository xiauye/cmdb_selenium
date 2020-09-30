from config.file import element_yaml
# from page_object.login_page import login_page
# from config.file import xlrd_file

class computer_manage_element_data(): #机房管理——添加——元素定位——测试数据
    def __init__(self,computer_data):
        # 元素定位
        self.element = element_yaml(yaml_path = "/data/element_data/asset_manager.yaml")
        self.navigation = self.element["computer_manage_add"].get("navigation")
        self.asset_menu = self.element["computer_manage_add"].get("asset_menu")
        self.computer_menu = self.element["computer_manage_add"].get("computer_menu")

        self.add_button = self.element["computer_manage_add"].get("add_button")

        self.sign = self.element["computer_manage_add"].get("sign")
        self.computer_name = self.element["computer_manage_add"].get("computer_name")
        self.address = self.element["computer_manage_add"].get("address")
        self.computer_phone = self.element["computer_manage_add"].get("computer_phone")
        self.manager = self.element["computer_manage_add"].get("manager")
        self.phone = self.element["computer_manage_add"].get("phone")
        self.cabinet = self.element["computer_manage_add"].get("cabinet")
        self.ip = self.element["computer_manage_add"].get("ip")
        self.bandwidth = self.element["computer_manage_add"].get("bandwidth")
        self.remarks = self.element["computer_manage_add"].get("remarks")

        self.submit_button = self.element["computer_manage_add"].get("submit_button")
        self.return_button = self.element["computer_manage_add"].get("return_button")

        self.add_pass = self.element["computer_manage_add"].get("add_pass")
        self.add_fail = self.element["computer_manage_add"].get("add_fail")

        # 编辑
        self.update_button = self.element["computer_manage_add"].get("update_button")
        # self.get_computer_name = self.element["computer_manage_add"].get("get_computer_name")
        self.get_remarks = self.element["computer_manage_add"].get("get_remarks")

        # 删除
        # self.checkall = self.element["computer_delete"].get('checkall_button')
        # self.delete_button = self.element["computer_delete"].get('delete_button')
        #
        # self.fail = self.element["checkpoint"].get('fail')
        # self.success = self.element["checkpoint"].get('success')
        # self.id_check = self.element["checkpoint"].get('id_check')


        # 测试数据
        # computer_add = xlrd_file(sheet_name="computer_manage_add",xlsx_path="/data/data_source/asset_manager_data.xlsx")
        # computer_data = computer_add[computer_add_data]

        self.sign_data = computer_data['sign']
        self.computer_name_data = computer_data['computer_name']
        self.address_data = computer_data['address']
        self.computer_phone_data = computer_data['computer_phone']
        self.manager_data = computer_data['manager']
        self.phone_data = computer_data['phone']
        self.cabinet_data = computer_data['cabinet']
        self.ip_data = computer_data['ip']
        self.bandwidth_data = computer_data['bandwidth']
        self.remarks_data = computer_data['remarks']

        # self.login_page = login_page(computer_data)

        # element = (//li[text()=self.computer_name_data]/../../../td[8]/a[text()='编辑'])

    def computer_name_return(self):
        computer_name_data = self.computer_name_data
        return computer_name_data