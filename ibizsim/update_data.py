# -*- coding=utf-8 -*-
import requests
from bs4 import BeautifulSoup
import http.cookiejar as cookielib
import re
from settings import *

# 获取已经保存在ibizsimCookies.txt的cookie值
s = requests.session()
s.cookies = cookielib.LWPCookieJar(filename="ibizsimCookies.txt")
s.cookies.load(ignore_discard=True, ignore_expires=True)

data = []
zero = 0

def get_url(game_id, team_id, period_id, number, Ispubulic):

    render = ['private_report_condition',
              'private_report_product', 'public_report_marketshare', 'public_report_primary']

    public_url = "http://www.ibizsim.cn/games/public_report?gameid=" + \
        game_id+"&teamid="+team_id+"&periodid=" + \
        period_id+"&render="+render[number]

    private_url = "http://www.ibizsim.cn/games/private_report?gameid=" + \
        game_id+"&teamid="+team_id+"&periodid=" + \
        period_id+"&render="+render[number]

    if Ispubulic == True:
        return public_url
    else:
        return private_url


def get_update_data(team_name, game_id, team_id, period_id, company_number):

    account_url = "http://www.ibizsim.cn/games/private_report?gameid=" + \
        game_id+"&teamid="+team_id+"&periodid="+period_id

    price_url = "http://www.ibizsim.cn/games/public_report?gameid=" + \
        game_id+"&teamid="+team_id+"&periodid="+period_id


    # 查找上期发债卷数
    account_resp = s.get(account_url, headers=header)
    soup = BeautifulSoup(account_resp.text, "lxml")
    bond = soup.find_all(name="td", class_="text-right")
    pat = re.compile("[\d\.\,]+")
    n_bond = pat.findall(str(bond[5]))[0]
    # print(n_bond)
    data.append(n_bond)

    # 查找上期债偿本金
    principal = pat.findall(str(bond[9]))[0]
    # print(principal)
    data.append(principal)

    # 查找上期期末企业状况
    private_url = get_url(
        game_id, team_id, period_id, 0, False)
    private_resp = s.get(private_url, headers=header)
    soup = BeautifulSoup(private_resp.text, "lxml")
    conditions = soup.find_all(name="td", class_="text-right")
    for m in range(36):
        pat = re.compile("[\d\.\%\,]+")
        n_conditions = pat.findall(str(conditions[m]))[0]
        # print(n_conditions)
        data.append(n_conditions)

    # 查找上期期末产品状况
    private_url = get_url(
        game_id, team_id, period_id, 1, False)
    private_resp = s.get(private_url, headers=header)
    soup = BeautifulSoup(private_resp.text, "lxml")
    product = soup.find_all(name="td", class_="text-right")
    for m in range(132):
        pat = re.compile("[\d\.\%\,]+")
        n_product = pat.findall(str(product[m]))[0]
        # print(n_product)
        data.append(n_product)

    # 查找上期公共报表价格
    public_resp = s.get(price_url, headers=header)
    soup = BeautifulSoup(public_resp.text, "lxml")
    price = soup.find_all(name="td", class_="text-right")
    for m in range(16*int(company_number)):
        pat = re.compile("[\d\.\%\,]+")
        n_price = pat.findall(str(price[m]))[0]
        # print(n_price)
        data.append(n_price)
    if int(company_number) < 20:
        for n in range((20-int(company_number))*16):
            data.append(zero)


    # 查找上期市场份额
    public_url = get_url(
        game_id, team_id, period_id, 2, True)
    public_resp = s.get(public_url, headers=header)
    soup = BeautifulSoup(public_resp.text, "lxml")
    market = soup.find_all(name="td", class_="text-right")
    for m in range(16*int(company_number)):
        pat = re.compile("[\d\.\%]+")
        n_market = pat.findall(str(market[m]))[2]
        # print(n_market)
        data.append(n_market)
    if int(company_number) < 20:
        for n in range((20-int(company_number))*16):
            data.append(zero)

    # 查找上期主要指标
    public_url = get_url(
        game_id, team_id, period_id, 3, True)
    public_resp = s.get(public_url, headers=header)
    soup = BeautifulSoup(public_resp.text, "lxml")
    indicators = soup.find_all(name="td", class_="text-right")
    # print(indicators)
    for m in range(8*int(company_number)):
        pat = re.compile("\-[\d\.\,]+|[\d\.\,]+")
        n_indicators = pat.findall(str(indicators[m]))[0]
        # print(n_indicators)
        data.append(n_indicators)
    if int(company_number) < 20:
        for n in range((20-int(company_number))*8):
            data.append(zero)

    for m in range(1000):
        data.append(zero)
    
    # 将结果中的空格除去
    datas = []
    for i in data:
        try:
            i = i.replace(",","")
            datas.append(i)
        except:
            datas.append(i)
    return datas
    


if __name__ == "__main__":
    team_name = u'全国熬夜锦标赛冠军选手'
    team_id = '350065'
    game_id = '177395'
    period_id = '3376324'
    company_number = '19'
    datas = get_update_data(team_name, game_id, team_id, period_id, company_number)
    print(len(datas))