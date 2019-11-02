# -*-coding=utf-8-*-
import requests
import re
from bs4 import BeautifulSoup
import http.cookiejar as cookielib
from settings import *

# 获取已经保存在ibizsimCookies.txt的cookie值
s = requests.session()
s.cookies = cookielib.LWPCookieJar(filename="ibizsimCookies.txt")
s.cookies.load(ignore_discard=True, ignore_expires=True)


def get_id(game_name):
    
    gu_resp = s.get(gu_url, headers=header)
    # gu_resp.encoding = gu_resp.apparent_encoding
    soup = BeautifulSoup(gu_resp.text, "lxml")
    game = soup.find(name="td", string=game_name)
    game_link = game.parent.find('a')
    pat = re.compile(r'\d+')
    result = pat.findall(game_link["href"])

    p_url = "http://www.ibizsim.cn/games/decision?gameid=" + \
        result[0]+"&type=raw&teamid="+result[1] + "&mode=old"

    p_resp = s.get(p_url, headers=header)
    soup = BeautifulSoup(p_resp.text, "lxml")
    period = soup.find_all("li", class_="active")
    pat = re.compile(r'\d+')
    result = pat.findall(str(period))

    tn_resp = s.get(tn_url, headers=header)
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