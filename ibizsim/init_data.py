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
    #print(rule_resp.text)
    soup = BeautifulSoup(rule_resp.text, "lxml")

    # 查找产品运出率
    pat = re.compile(r"([0-9.]+)[ ]*%")
    product_delivery_rate = pat.findall(rule_resp.text)[0]+"%"
    data.append(product_delivery_rate)

    # 查找运费
    freight = soup.find_all("td", string=team_name)
    for m in range(4):
        n_freight = freight[m].find_all_next("td", align="right")
        for n in range(8):
            pat = re.compile(r"\d+\,?\d*")
            data.append(pat.findall(str(n_freight[n]))[0])

    # 查找单位原材料库存费
    pat = re.compile(u"每元原材料每期\d+\.?\d*元")
    pre_per_material_inventory = pat.findall(rule_resp.text)[0]
    per_material_inventory = re.findall(re.compile("\d+\.?\d*"),pre_per_material_inventory)[0]
    data.append(per_material_inventory)
    
    # 查找库存(仍需修改)
    inventory = soup.find("h2")
    print(unicode(str(inventory), encoding="utf-8"))
    n_inventory = inventory.find_all_next("td", align="right")
    print(unicode(str(n_inventory), encoding="utf-8"))
    for n in range(4):
        #inventory_cost = inventory.find_all_next(re.compile("\d+\.?\d*"))[n]
        # data.append(pat.findall(str(n_inventory))[n])
        #data.append(inventory_cost)

    print(data)


if __name__ == "__main__":
    team_name = u'全国熬夜锦标赛冠军选手'
    team_id = '350065'
    game_id = '177395'
    get_init_data(team_name, game_id, team_id)
