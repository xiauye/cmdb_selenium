from config.file import xlrd_file,element_yaml

class group_manage_element_data():
    def __init__(self,group_data):
        # 元素定位
        self.element = element_yaml(yaml_path="/data/element_data/asset_manager.yaml")
        self.navigation = self.element["group_manage"].get("navigation")
        self.asset_menu = self.element["group_manage"].get("asset_menu")
        self.group_menu = self.element["group_manage"].get("group_menu")
        self.group_button = self.element["group_manage"].get("group_button")

        self.server_group = self.element["group_manage"].get("server_group")
        self.describe = self.element["group_manage"].get("describe")
        self.choice_server = self.element["group_manage"].get("choice_server")
        self.server_right = self.element["group_manage"].get("server_right")

        self.submit_button = self.element["group_manage"].get("submit_button")
        self.return_button = self.element["group_manage"].get("return_button")

        # 删除
        # self.checkall = self.element["computer_delete"].get('checkall_button')
        # self.delete_button = self.element["computer_delete"].get('delete_button')
        #
        # self.id_check = self.element["group_menu"].get("id_check")


        # 测试数据
        group_add = xlrd_file(sheet_name="asset_manage_data", xlsx_path="/data/data_write/cmdb_write_data.xlsx")
        group_host_data = group_add[0]

        self.server_group_data = group_data["server_group"]
        self.describe_data = group_data["describe"]

        self.host_name_data = group_host_data["host_name"]

