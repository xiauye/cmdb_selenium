import yaml, xlrd, openpyxl
import os, time

path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# random_now = time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time()))


"""截图"""
def screenshot():
    now = time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time()))
    report_path = (path + '/report/screenshot/%s.png' % now)
    print("%s：截图成功！！！" % report_path)
    return report_path

"""文件保存为html"""
def report_html():
    now = time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time()))
    report_dir = (path + '/report/report/%s.html' % now)
    # print("测试报告文件生成成功！！！：" , report_dir)
    re_open = open(report_dir, 'wb')
    return re_open

"""文件保存为logs"""
def report_log():
    now = time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time()))
    report_dir = (path + '/report/logs/%s.log' % now)
    # print("测试日志文件生成成功！！！：" , report_dir)
    # re_open = open(report_dir, 'wb')
    return report_dir

"""获取yaml中的值"""
def element_yaml(yaml_path):
    # file=open(path+"\\data\\page_data.yaml", "r",encoding= "utf-8")
    file = open(path + yaml_path, "r", encoding="utf-8")
    element_path = yaml.safe_load(file)
    file.close()
    return element_path


"""获取Excel中的值"""
def xlrd_file(sheet_name, xlsx_path):
    case_path = path + xlsx_path
    file = xlrd.open_workbook(case_path)
    sheet = file.sheet_by_name(sheet_name)

    ncols = sheet.ncols-2 #总例数
    listdata = []
    for n in range(ncols):
        if ncols >= n:
            dictdata = {}
            col_values = sheet.col_values(1)  # 例
            col_values2 = sheet.col_values(n+2)
            if len(col_values) == len(col_values2):
                for i in range(len(col_values2)):
                    dictdata[str(col_values[i])] = col_values2[i]
                listdata.append(dictdata)
            else:
                print('合并列表长度不一样')
                raise EOFError
        else:
            print('列表长度有误')
            raise EOFError
    return listdata


"""excel文件写入"""
def write_excel(target_list):
    filename = (path + "/data/data_write/cmdb_write_data.xlsx")
    sheet_name = "asset_manage_data"
    if not filename.endswith('.xlsx'):
        filename += '.xlsx'
    # 读取xlrd
    file = xlrd.open_workbook(filename)
    sheet_xlrd = file.sheet_by_name(sheet_name)
    data = sheet_xlrd.col_values(1)

    # openpyxl
    ws = openpyxl.load_workbook(filename)
    sheet = ws.get_sheet_by_name(sheet_name)

    # columns = sheet.max_column #获取总行数
    target_list1 = target_list[0][1]
    target_list2 = target_list1.split()

    ret = []
    for s in data:
        if s in target_list2:
            ret.append(s)

    # title_data = ('数据字段名', '字段名', '数据值1')
    if ret == target_list2:
        # 获取值的位置
        seat_row = data.index(target_list1)
        rows = len(target_list)
        lines = len(target_list[0])
        for i in range(rows):
            for j in range(lines):
                sheet.cell(row=i+seat_row+1,column=j+1).value = target_list[i][j]
                ws.save(filename)
                ws.close()
    elif ret != target_list2:
        rows1 = len(target_list)
        lines = len(target_list[0])
        rows = sheet.max_row  # 获取总列数
        for i in range(rows1):
            for j in range(lines):
                sheet.cell(row=i + rows + 1, column=j + 1).value = target_list[i][j]
                ws.save(filename)
                ws.close()
    else:
        print('写入格式有误')
        raise EOFError
    # target_list = [('用户名2', 'username', 'admin2')]

# 数据字段名	字段名	数据值1
# 用户名1	username2	admin
if __name__ == '__main__':
    computer_data=xlrd_file(sheet_name="host_manager_add", xlsx_path="/data/data_source/asset_manager_data.xlsx")
    print('computer_data',computer_data)

