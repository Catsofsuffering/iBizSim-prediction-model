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
    rule_url = "www.ibizsim.cn/games/rules?gameid="+game_id+"&teamid="+team_id

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
    companys = soup.find_all("tr")
    serial_number = number = 0
    for company in companys:
        number += 1
        company = unicode(str(company), encoding="utf-8")
        pat = re.compile(team_name)
        try:
            if team_name == pat.findall(company)[0]:
                serial_number=number
        except:
            pass
    data.append(serial_number-2)
    data.append(number-2)
    
    # 查找剩下的数据


if __name__ == "__main__":
    team_name=u'全国熬夜锦标赛冠军选手'
    team_id='350065'
    game_id='177395'
    get_init_data(team_name, game_id, team_id)
