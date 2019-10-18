# coding=utf-8
import requests
import re
import http.cookiejar as cookielib

s = requests.session()
s.cookies = cookielib.LWPCookieJar(filename="ibizsimCookies.txt")

header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'www.ibizsim.cn',
    'If-None-Match': '"8678321f2ab73884db2bd1f70c4e29c8"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
}


def get_token():
    get_url = 'http://www.ibizsim.cn/main/login'
    response = s.get(get_url)
    pat = 'name=\"authenticity_token\" type=\"hidden\" value=\"(.*?)\"'
    authenticity_token = re.findall(pat, response.text)[0]
    return authenticity_token


def login(authenticity_token, username, password):
    login_url = "http://www.ibizsim.cn//center/trylogin"
    param = {
        'utf8': '✓',
        'authenticity_token': authenticity_token,
        'name': username,
        'password': password,
        'commit': '登录'
    }
    response = s.post(login_url, data=param, headers=header)
    # response.encoding = response.apparent_encoding
    # print(response.status_code)
    # print(response.text)
    s.cookies.save()


def check_login_status():
    check_url = "http://www.ibizsim.cn/games/mygames"
    resp = s.get(check_url, headers=header, allow_redirects=False)
    if resp.status_code != 200:
        return False
    else:
        return True


if __name__ == "__main__":
    s.cookies.load()
    login_status = check_login_status()
    if login_status == False:
        username, password = '821621930@qq.com', 'Whoareyou59820'
        authenticity_token = get_token()
        login(authenticity_token, username, password)
        print("Login by username and password")
    else:
        print("login by cookies")
    response = s.get("http://www.ibizsim.cn/games/man_machine",
                     headers=header, allow_redirects=False)
    response.encoding = response.apparent_encoding                
    print(response.status_code)
    print(response.text)
