# -*- coding=utf-8 -*-
import requests
from bs4 import BeautifulSoup
import http.cookiejar as cookielib

# 获取已经保存在ibizsimCookies.txt的cookie值
s = requests.session()
s.cookies = cookielib.LWPCookieJar(filename="ibizsimCookies.txt")
s.cookies.load(ignore_discard=True, ignore_expires=True)

# 获取规则界面的html
def get_init_data(game_id, team_id):
    rule_url =  "www.ibizsim.cn/games/rules?gameid="+game_id"&teamid="+team_id
    
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

    rule_resp = s.get(rule_url, headers=headers)
    

