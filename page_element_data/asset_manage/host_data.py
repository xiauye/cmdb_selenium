from config.file import element_yaml,xlrd_file


class host_manage_element_data():  # 主机管理_添加_元素定位_测试数据
    def __init__(self, host_data):
        self.element = element_yaml(yaml_path="/data/element_data/asset_manager.yaml")

        # 主机管理_元素定位
        self.navigation = self.element['host_manage_add'].get('navigation')

        self.asset_menu = self.element['host_manage_add'].get('asset_menu')
        self.host_menu = self.element['host_manage_add'].get('host_menu')
        self.add_button = self.element['host_manage_add'].get('add_button')

        self.add_host_content = self.element['host_manage_add'].get('add_host_content')
        self.host_name = self.element['host_manage_add'].get('host_name')
        self.ip = self.element['host_manage_add'].get('ip')

        # self.number = self.element['host_manage_add'].get('number')
        self.computer = self.element['host_manage_add'].get('computer')

        self.other_ip = self.element['host_manage_add'].get('other_ip')
        self.asset_number = self.element['host_manage_add'].get('asset_number')

        self.device_type = self.element['host_manage_add'].get('device_type')
        self.device = self.element['host_manage_add'].get('device')

        self.system = self.element['host_manage_add'].get('system')
        self.equipment = self.element['host_manage_add'].get('equipment')
        self.upper_time = self.element['host_manage_add'].get('upper_time')
        self.cpu_type = self.element['host_manage_add'].get('cpu_type')
        self.cpu_number = self.element['host_manage_add'].get('cpu_number')
        self.memory = self.element['host_manage_add'].get('memory')
        self.disk = self.element['host_manage_add'].get('disk')
        self.sn_number = self.element['host_manage_add'].get('sn_number')
        self.position = self.element['host_manage_add'].get('position')
        self.remarks = self.element['host_manage_add'].get('remarks')

        self.submit_button = self.element['host_manage_add'].get('submit_button')

        self.return_button = self.element['host_manage_add'].get('return_button')

        # 编辑
        self.update_button = self.element['host_manage_add'].get('update_button')
        self.host_update_news = self.element['host_manage_add'].get('host_update')
        self.iframe = self.element['host_manage_add'].get('iframe')
        self.preservation_button = self.element['host_manage_add'].get('preservation_button')
        self.host_name_update = self.element['host_manage_add'].get('host_name_update')





        # 删除
        self.checkall_button = self.element['host_delete'].get('checkall_button')
        self.delete_button = self.element['host_delete'].get('delete_button')

        self.id_check = self.element['host_manage_add'].get('id_check')

        # 提示信息
        self.fail = self.element["checkpoint"].get("fail")
        self.success = self.element["checkpoint"].get("success")

        # 主机管理_测试数据
        computer_data = xlrd_file(sheet_name="asset_manage_data", xlsx_path="/data/data_write/cmdb_write_data.xlsx")
        self.computer_data = computer_data[0]

        self.host_name_data = host_data['host_name']
        self.ip_data = host_data['ip']

        # self.number_data = host_data['number']

        self.computer_data = self.computer_data['computer_name']  # 得到机房管理名称
        # print('self.computer_data',self.computer_data)

        self.other_ip_data = host_data['other_ip']
        self.asset_number_data = host_data['asset_number']

        self.device_type_data = host_data['device_type']
        self.device_data = host_data['device']

        self.system_data = host_data['system']
        self.equipment_data = host_data['equipment']
        self.upper_time_data = host_data['upper_time']
        self.cpu_type_data = host_data['cpu_type']
        self.cpu_number_data = host_data['cpu_number']
        self.memory_data = host_data['memory']
        self.disk_data = host_data['disk']
        self.sn_number_data = host_data['sn_number']
        self.position_data = host_data['position']
        self.remarks_data = host_data['remarks']
