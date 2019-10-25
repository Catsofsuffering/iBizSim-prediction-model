# -*- coding=utf-8 -*-
import requests
from bs4 import BeautifulSoup
import http.cookiejar as cookielib
import re

# 获取已经保存在ibizsimCookies.txt的cookie值
s = requests.session()
s.cookies = cookielib.LWPCookieJar(filename="ibizsimCookies.txt")
s.cookies.load(ignore_discard=True, ignore_expires=True)

data = []

def get_update_data(team_name, game_id, team_id, period_id, company_number):

    account_url = "http://www.ibizsim.cn/games/private_report?gameid=" + \
        game_id+"&teamid="+team_id+"&periodid="+period_id

    price_url = "http://www.ibizsim.cn/games/private_report?gameid=" + \
        game_id+"&teamid="+team_id+"&periodid="+period_id

    render = []

    public_url = "http://www.ibizsim.cn/games/public_report?gameid=" + \
        game_id+"&teamid="+team_id+"&periodid="+period_id+"render="+render

    public_url = "http://www.ibizsim.cn/games/private_report?gameid=" + \
        game_id+"&teamid="+team_id+"&periodid="+period_id+"render="+render

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
    # 查找上期发债卷数
    account_resp = s.get(account_url, headers=headers)
    soup = BeautifulSoup(account_resp.text, "lxml")
    bond = soup.find_all(name="td",class="text-right")
    b

    # 查找上期期末企业状况
    private_resp = s.get(private_url, headers=headers)
    soup = BeautifulSoup(private_resp.text, "lxml")
    conditions = soup.find_all(name="td",class="text-right")
    for n in range(company_number):
        for m in range(16):
            pat = re.compile("[\d\.\%]+")
            data.append(pat.findall(conditions[n*16+m])[0])


