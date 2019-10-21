# -*-coding=utf-8-*-
import xlrd
import os

# 设定提交表格的位置和名字
# 硬编码，需要修改
path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
filename = path+os.sep+'form'+os.sep+'2019_bizsim.xls'

# 定义价格price_list
price_list = []
# 定义促销promotion_list
promotion_list = []
# 定义供货support_list
support_list = []
# 定义生产product_list
product_list = []
# 定义发展develop_list
develop_list = []
# 定义财务finance_list
finance_list = []

# 因为range函数，行列范围中的up项与实际相比加1

# 价格行列范围
price_low_row = 6
price_up_row = 11
price_low_col = 70
price_up_col = 74
# 促销行列范围
promotion_row = 10
promotion_low_col = 70
promotion_up_col = 74
# 供货行列范围
support_low_row = 13
support_up_row = 17
support_low_col = 70
support_up_col = 74
# 生产行列范围
product_low_row = 19
product_up_row = 23
product_low_col = 70
product_up_col = 75
# 发展行列范围
develop_row = 25
develop_low_col = 70
develop_up_col = 74
# 财务行列范围
finance_row = 28
finance_low_col = 70
finance_up_col = 75

# 读取模板表格对应的数据
def write_data(filename, sheet_index):
    try:
        # 打开Excel文件读取数据
        data = xlrd.open_workbook(filename)
        # 获取对应工作表
        table = data.sheet_by_index(sheet_index)

        # 价格
        for row in range(price_low_row, price_up_row):
            for col in range(price_low_col, price_up_col):
                cell_value = table.cell(row, col).value
                price_list.append(cell_value)
        # 促销
        row = promotion_row
        for col in range(promotion_low_col, promotion_up_col):
            cell_value = table.cell(row, col).value
            promotion_list.append(cell_value)

        # 供货
        for row in range(support_low_row, support_up_row):
            for col in range(support_low_col, support_up_col):
                cell_value = table.cell(row, col).value
                support_list.append(cell_value)

        # 生产
        for row in range(product_low_row, product_up_row):
            for col in range(product_low_col, product_up_col):
                cell_value = table.cell(row, col).value
                product_list.append(cell_value)

        # 发展
        row = develop_row
        for col in range(develop_low_col, develop_up_col):
            cell_value = table.cell(row, col).value
            develop_list.append(cell_value)

        # 财务
        row = finance_row
        for col in range(finance_low_col, finance_up_col):
            cell_value = table.cell(row, col).value
            finance_list.append(cell_value)

        # test
        # print(len(price_list))
        # print(len(promotion_list))
        # print(len(support_list))
        # print(len(product_list))
        # print(len(develop_list))
        # print(len(finance_list))

        # 合并返回
        result_list = price_list + support_list + promotion_list + \
            product_list + develop_list + finance_list
        return result_list

    except Exception, e:
        print str(e)


if __name__ == "__main__":
    data = write_data(filename, 5)
    # print(data)
