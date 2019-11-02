# -*-coding=utf-8-*-
import requests
import re
import http.cookiejar as cookielib
from settings import *

# 获取已经保存在ibizsimCookies.txt的cookie值
s = requests.session()
s.cookies = cookielib.LWPCookieJar(filename="ibizsimCookies.txt")
s.cookies.load(ignore_discard=True, ignore_expires=True)

# 获取决策提交表单对应的authenticity_token值
# 需要登陆后的cookies值
def get_formput_token(game_id, team_id):
    referer = "http':/'/www.ibizsim.cn/games/welcome?gameid=" + game_id + \
        "&teamid=" + team_id

    get_url = "http://www.ibizsim.cn/games/decision?gameid=" + \
        game_id + "&type=raw&teamid=" + team_id + "&mode = old"

    response = s.get(get_url, headers=referer_header)
    # print(response.status_code)
    pat = 'name=\"authenticity_token\" type=\"hidden\" value=\"(.*?)\"'
    authenticity_token = re.findall(pat, response.text)[0]
    return authenticity_token

# 提交决策

def formput(authenticity_token, param, team_id, game_id, user_id, period_id):
    url = "http://www.ibizsim.cn/games/make_decision?teamid=" + team_id

    referer = "http://www.ibizsim.cn/games/decision?gameid=" + game_id + \
        "&mode=old&teamid=" + team_id + "&type=raw"

    param = {
        'utf8': '✓',
        'authenticity_token': authenticity_token,
        'decision[price11]': data[0],
        'decision[price12]': data[1],
        'decision[price13]': data[2],
        'decision[price14]': data[3],
        'decision[adver1]': data[4],
        'decision[price21]': data[5],
        'decision[price22]': data[6],
        'decision[price23]': data[7],
        'decision[price24]': data[8],
        'decision[adver2]': data[9],
        'decision[price31]': data[10],
        'decision[price32]': data[11],
        'decision[price33]': data[12],
        'decision[price34]': data[13],
        'decision[adver3]': data[14],
        'decision[price41]': data[15],
        'decision[price42]': data[16],
        'decision[price43]': data[17],
        'decision[price44]': data[18],
        'decision[adver4]': data[19],
        'decision[promotion1]': data[20],
        'decision[promotion2]': data[21],
        'decision[promotion3]': data[22],
        'decision[promotion4]': data[23],
        'decision[shipment11]': data[24],
        'decision[shipment12]': data[25],
        'decision[shipment13]': data[26],
        'decision[shipment14]': data[27],
        'decision[shipment21]': data[28],
        'decision[shipment22]': data[29],
        'decision[shipment23]': data[30],
        'decision[shipment24]': data[31],
        'decision[shipment31]': data[32],
        'decision[shipment32]': data[33],
        'decision[shipment33]': data[34],
        'decision[shipment34]': data[35],
        'decision[shipment41]': data[36],
        'decision[shipment42]': data[37],
        'decision[shipment43]': data[38],
        'decision[shipment44]': data[39],
        'decision[output11]': data[40],
        'decision[output12]': data[41],
        'decision[output13]': data[42],
        'decision[output14]': data[43],
        'decision[r_and_d1]': data[44],
        'decision[output21]': data[45],
        'decision[output22]': data[46],
        'decision[output23]': data[47],
        'decision[output24]': data[48],
        'decision[r_and_d2]': data[49],
        'decision[output31]': data[50],
        'decision[output32]': data[51],
        'decision[output33]': data[52],
        'decision[output34]': data[53],
        'decision[r_and_d3]': data[54],
        'decision[output41]': data[55],
        'decision[output42]': data[56],
        'decision[output43]': data[57],
        'decision[output44]': data[58],
        'decision[r_and_d4]': data[59],
        'decision[men_hire]': data[60],
        'decision[men_release]': data[61],
        'decision[machine_buy]': data[62],
        'decision[raw_m_buy]': data[63],
        'decision[bank_loan]': data[64],
        'decision[debentures]': data[65],
        'decision[gov_s]': data[66],
        'decision[dividends]': data[67],
        'decision[wage_rate]': data[68],
        'decision[game_id]': game_id,
        'decision[user_id]': user_id,
        'decision[period_id]': period_id,
        'commit': '提交'
    }
    response = s.post(url, data=param, headers=referer_header)
    response.encoding = response.apparent_encoding
    pat = "提交决策成功"
    if len(re.findall(pat, response.content)) == 0:
        print("Failed to submit decisions")
    else:
        print("Succesfully submited decisions")
    #    print(re.findall(pat, response.content)[0])
    return response


if __name__ == "__main__":
    # import login
    import form_read
    game_id = '177430'
    team_id = user_id = '351328'
    period_id = '3376977'
    authenticity_token = get_formput_token(game_id, team_id)
    data = form_read.write_data(form_read.filename, 5)
    response = formput(authenticity_token, data, team_id,
                       game_id, user_id, period_id)
    #response.encoding = response.apparent_encoding
    # print(response.text)

"""
    login.s.cookies.load(ignore_discard=True, ignore_expires=True)
    login_status = login.check_login_status()
    if login_status == False:
        username, password = '821621930@qq.com', 'Whoareyou59820'
        authenticity_token = login.get_token()
        login.login(authenticity_token, username, password)
        print("Login by username and password")
    else:
        print("login by cookies")
"""
