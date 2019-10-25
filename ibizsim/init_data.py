# -*- coding=utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup
import http.cookiejar as cookielib

# 获取已经保存在ibizsimCookies.txt的cookie值
s = requests.session()
s.cookies = cookielib.LWPCookieJar(filename="ibizsimCookies.txt")
s.cookies.load(ignore_discard=True, ignore_expires=True)

# 获取规则界面的html
data = []

def get_init_data(team_name, game_id, team_id):
    rule_url = "http://www.ibizsim.cn/games/rules?gameid="+game_id+"&teamid="+team_id

    report_url = "http://www.ibizsim.cn/games/public_report?gameid=" + \
        game_id+"&teamid="+team_id

    headers = {
        'Host': 'www.ibizsim.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'close',
        'Upgrade-Insecure-Requests': '1',
        'If-None-Match': '"9674b5cba51bec402d5be893520406b9"',
        'Cache-Control': 'max-age=0'
    }

    # 查找公司序号和公司数
    report_resp = s.get(report_url, headers=headers)
    soup = BeautifulSoup(report_resp.text, "lxml")
    total_company = soup.find_all("tr")
    company_number = number = 0
    for company in total_company:
        number += 1
        company = unicode(str(company), encoding="utf-8")
        pat = re.compile(team_name)
        try:
            if team_name == pat.findall(company)[0]:
                company_number = number
        except:
            pass
    data.append(company_number-2)
    data.append(number-2)

    # 查找剩下的数据
    rule_resp = s.get(rule_url, headers=headers)
    rule_resp.encoding = rule_resp.apparent_encoding
    # print(rule_resp.text)
    soup = BeautifulSoup(rule_resp.text, "lxml")

    # 查找产品运出率
    pat = re.compile(u"本期产品的 (.*?)%")
    product_delivery_rate = pat.findall(rule_resp.text)[0]+"%"
    # print(unicode(str(product_delivery_rate), encoding="utf-8"))
    data.append(product_delivery_rate)

    # 查找运费
    freight = soup.find_all("td", string=team_name)
    for m in range(4):
        n_freight = freight[m].find_all_next("td", align="right")
        for n in range(8):
            pat = re.compile(u"[\d\,]+")
            data.append(pat.findall(str(n_freight[n]))[0])

    # 查找单位原材料库存费
    pat = re.compile(u"每元原材料每期(.*?)元")
    per_material_inventory = pat.findall(rule_resp.text)[0]
    # print(unicode(str(per_material_inventory), encoding="utf-8"))
    data.append(per_material_inventory)

    # 查找库存
    inventory = soup.find_all("h2")[0]
    n_inventory = inventory.find_all_next("td", align="right")
    for n in range(4):
        pat = re.compile("[1-9]\d*\.\d*|0\.\d*[1-9]\d*")
        inventory_cost = pat.findall(str(n_inventory))[n]
        # print(unicode(str(inventory_cost), encoding="utf-8"))
        data.append(inventory_cost)

    # 查找单位生产资源
    resources = soup.find_all("h2")[2]
    n_resources = resources.find_all_next("td", align="right")
    for n in range(12):
        pat = re.compile("[1-9]\d*\.\d*|0\.\d*[1-9]\d*")
        resources_cost = pat.findall(str(n_resources))[n]
        # print(unicode(str(resources_cost), encoding="utf-8"))
        data.append(resources_cost)

    # 查找机器价格
    pat = re.compile(u"机器价格为(.*?)元")
    machine_price = pat.findall(rule_resp.text)[0]
    # print(unicode(str(machine_price), encoding="utf-8"))
    data.append(machine_price)

    # 查找折旧率
    pat = re.compile(u"折旧为(.*?)%")
    depreciation_rate = pat.findall(rule_resp.text)[0]+"%"
    # print(unicode(str(depreciation_rate), encoding="utf-8"))
    data.append(depreciation_rate)

    # 查找原材料价格
    material_price = soup.find_all("h2")[5]
    n_material_price = material_price.find_all_next("td", align="right")
    for n in range(8):
        pat = re.compile("[0-9\.]+")
        material_price_cost = pat.findall(str(n_material_price))[n+8]
        # print(unicode(str(material_price_cost), encoding="utf-8"))
        data.append(material_price_cost)

    # 查找原材料运费(固定)
    pat = re.compile(u"固定费用为 (.*?)元")
    fixd_material_freight = pat.findall(rule_resp.text)[0]
    # print(unicode(str(fixd_material_freight), encoding="utf-8"))
    data.append(fixd_material_freight)

    # 查找原材料运费(变动)
    pat = re.compile(u"变动费用为 (.*?)元")
    var_material_freight = pat.findall(rule_resp.text)[0]
    # print(unicode(str(var_material_freight), encoding="utf-8"))
    data.append(var_material_freight)

    # 查找原材料使用率
    pat = re.compile(u"原材料至多有 (.*?)%")
    material_usage = pat.findall(rule_resp.text)[0]+"%"
    # print(unicode(str(material_usage), encoding="utf-8"))
    data.append(material_usage)

    # 查找管理费
    management_fee = soup.find_all(string=re.compile(u"公司每期的固定费用与生产的产品和班次有关。"))
    pat = re.compile(u"[^u4e00-u9fa5][\d]+")
    n_management_fee = pat.findall(str(management_fee))
    # print(unicode(str(n_management_fee), encoding="utf-8"))
    for n in range(12):
        if n % 3 != 0:
            data.append(n_management_fee[n])

    # 查找机器维修费99
    pat = re.compile(u"维修费为 (.*?)元")
    maintenance = pat.findall(rule_resp.text)[0]
    # print(unicode(str(maintenance), encoding="utf-8"))
    data.append(maintenance)

    # 查找研发费用
    development_fee = soup.find_all("h2")[8]
    n_development_fee = development_fee.find_all_next("td", align="right")
    for n in range(6, 29):
        pat = re.compile("[\d\.\,]+")
        f_development_fee = pat.findall(str(n_development_fee[n]))
        # print(unicode(str(f_development_fee), encoding="utf-8"))
        if n % 6 != 5:
            data.append(f_development_fee[0])

    # 查找工人数据
    workers_data = soup.find(string=re.compile(u"企业可以在每期期初招聘工人"))
    pat = re.compile("[\d\.\%]+")
    n_workers_data = pat.findall(workers_data)
    # print(n_workers_data)
    for n in range(3):
        data.append(n_workers_data[n])

    workers_data2 = soup.find(string=re.compile(u"企业决策时，可以根据情况解聘工人"))
    pat = re.compile("[\d\.\%]+")
    n_workers_data2 = pat.findall(workers_data2)
    # print(n_workers_data2)
    for n in range(3):
        data.append(n_workers_data2[n])

    # 查找工人工资
    pat = re.compile(u"第一班正班: (.*?)元")
    wage1 = pat.findall(rule_resp.text)[0]
    data.append(wage1)

    pat = re.compile(u"第一班加班: (.*?)元")
    wage2 = pat.findall(rule_resp.text)[0]
    data.append(wage2)

    pat = re.compile(u"第二班正班: (.*?)元")
    wage3 = pat.findall(rule_resp.text)[0]
    data.append(wage3)

    pat = re.compile(u"第二班加班: (.*?)元")
    wage4 = pat.findall(rule_resp.text)[0]
    data.append(wage4)

    # 查找银行相关数据
    bank_data = soup.find(string=re.compile(u"模拟开始时各公司有现金"))
    pat = re.compile("[\d\.\,]+")
    n_bank_data = pat.findall(bank_data)
    # print(n_bank_data)
    for n in range(1, 3):
        data.append(n_bank_data[n])

    pat = re.compile(u"银行贷款的本利在本期末偿还，年利率为(.*?)%")
    bank_data2 = pat.findall(rule_resp.text)[0]+"%"
    # print(unicode(str(bank_data2), encoding="utf-8"))
    data.append(bank_data2)

    pat = re.compile(u"公司每期都可以买国债，年利率为(.*?)%")
    bank_data3 = pat.findall(rule_resp.text)[0]+"%"
    # print(unicode(str(bank_data3), encoding="utf-8"))
    data.append(bank_data3)

    pat = re.compile(u"债券的年利率为(.*?)%")
    bank_data4 = pat.findall(rule_resp.text)[0]+"%"
    # print(unicode(str(bank_data4), encoding="utf-8"))
    data.append(bank_data4)

    pat = re.compile(u"税金为本期净收益的 (.*?)%")
    bank_data5 = pat.findall(rule_resp.text)[0]+"%"
    # print(unicode(str(bank_data5), encoding="utf-8"))
    data.append(bank_data5)

    # 查找偿债券率
    pat = re.compile(u"各期要按(.*?)%的比例偿还债券的本金")
    bond_rate = pat.findall(rule_resp.text)[0]+"%"
    # print(unicode(str(bond_rate), encoding="utf-8"))
    data.append(bond_rate)

    # 查找评判标准
    pat = re.compile(u"各项指标的权重分别为: (.*?), 其中")
    criteria = pat.findall(rule_resp.text)[0]
    pat = re.compile(u'[\d\.]+')
    for n in range(7):
        data.append(pat.findall(str(criteria))[n])


    # 将结果中的空格除去
    datas = []
    for i in data:
        try:
            i = i.replace(" ", "")
            i = i.replace(",","")
            datas.append(i)
        except:
            datas.append(i)
    return datas


if __name__ == "__main__":

    team_name = u'全国熬夜锦标赛冠军选手'
    team_id = '350065'
    game_id = '177395'
    datas = get_init_data(team_name, game_id, team_id)
    print(datas)
'''
    import form_init
    import os
    path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    filename = path+os.sep+'form'+os.sep+'2019_bizsim.xls'
    form_init.write_data(filename, datas)
'''

