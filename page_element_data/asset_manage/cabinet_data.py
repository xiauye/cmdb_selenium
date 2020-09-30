from config.file import element_yaml,xlrd_file

class cabinet_element_data:
    def __init__(self,cabinet_data):
        # 元素定位
        self.element = element_yaml(yaml_path="/data/element_data/asset_manager.yaml")
        self.navigation = self.element["cabinet_add"].get("navigation")

        self.asset_menu = self.element["cabinet_add"].get("asset_menu")
        self.cabinet_menu = self.element["cabinet_add"].get("cabinet_menu")
        self.cabinet_button = self.element["cabinet_add"].get("cabinet_button")

        self.computer = self.element["cabinet_add"].get("computer")
        self.cabinet = self.element["cabinet_add"].get("cabinet")
        self.describe = self.element["cabinet_add"].get("describe")
        self.choice_server = self.element["cabinet_add"].get("choice_server")
        self.server_right_button = self.element["cabinet_add"].get("server_right_button")

        self.submit_button = self.element["cabinet_add"].get("submit_button")

        self.return_button = self.element["cabinet_add"].get("return_button")
        # 删除
        self.checkall = self.element["computer_delete"].get('checkall_button')
        self.delete_button = self.element["computer_delete"].get('delete_button')

        self.id_check = self.element["cabinet_add"].get('id_check')


        # 测试数据
        cabinet_add = xlrd_file(sheet_name="asset_manage_data", xlsx_path="/data/data_write/cmdb_write_data.xlsx")
        cabinet_host_data = cabinet_add[0]
        print('cabinet_add',cabinet_add)

        self.computer_data = cabinet_host_data["computer_name"]
        self.host_name_data = cabinet_host_data["host_name"]

        self.cabinet_data = cabinet_data["cabinet"]
        self.describe_data = cabinet_data["describe"]



