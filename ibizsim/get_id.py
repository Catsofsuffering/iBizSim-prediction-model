# -*-coding=utf-8-*-
import requests
import re
from bs4 import BeautifulSoup
import http.cookiejar as cookielib

# 获取已经保存在ibizsimCookies.txt的cookie值
s = requests.session()
s.cookies = cookielib.LWPCookieJar(filename="ibizsimCookies.txt")
s.cookies.load(ignore_discard=True, ignore_expires=True)


def get_id(game_name):

    gu_url = "http://www.ibizsim.cn/games/mygames"

    tn_url = "http://www.ibizsim.cn/main/myteam"

    headers = {
        'Host': 'www.ibizsim.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'close',
        'Upgrade-Insecure-Requests': '1',
        'If-None-Match': '"1276c30637724dc281faae64786f2d08"',
        'Cache-Control': 'max-age=0'
    }

    gu_resp = s.get(gu_url, headers=headers)
    # gu_resp.encoding = gu_resp.apparent_encoding
    soup = BeautifulSoup(gu_resp.text, "lxml")
    game = soup.find(name="td", string=game_name)
    game_link = game.parent.find('a')
    pat = re.compile(r'\d+')
    result = pat.findall(game_link["href"])

    p_url = "http://www.ibizsim.cn/games/decision?gameid=" + \
        result[0]+"&type=raw&teamid="+result[1] + "&mode=old"

    p_resp = s.get(p_url, headers=headers)
    soup = BeautifulSoup(p_resp.text, "lxml")
    period = soup.find_all("li", class_="active")
    pat = re.compile(r'\d+')
    result = pat.findall(str(period))

    tn_resp = s.get(tn_url, headers=headers)
    soup = BeautifulSoup(p_resp.text, "lxml")
    team = soup.find('font')
    pat = re.compile(r'\：(.*?)比赛')
    result.append(pat.findall(str(team))[0])
    return result[0], result[1], result[2], result[3], result[4]


if __name__ == "__main__":
    game_name = u"初赛5赛区"
    get_id(game_name)
    game_id, period_id, team_id, current_period, team_name = get_id(game_name)
    print("game_id={0},\nperiod_id={1},\nteam_id={2},\ncurrent_period={3}".format(
        game_id, period_id, team_id, current_period))
    print(unicode(team_name, encoding="utf-8"))