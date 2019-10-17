# -*-coding=utf-8-*-
import login_requ.py

authenticity_token = get_token()
cookies = login(authenticity_token, username, password)

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'
    'Accept-Encoding': 'gzip, deflate'
    'Accept-Language': 'zh-CN,zh;q=0.9'
    'Cache-Control': 'max-age=0'
    'Connection': 'keep-alive'
    'Content-Length': '2063'
    'Content-Type': 'application/x-www-form-urlencoded'
    'Cookie': 'cookies'
    'Host': 'www.ibizsim.cn'
    'Origin': 'http://www.ibizsim.cn'
    'Referer': 'http://www.ibizsim.cn/games/decision?gameid=177430&type=raw&teamid=351328&mode=old'
    'Upgrade-Insecure-Requests': '1'
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

def formput():
    

