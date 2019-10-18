# -*-coding=utf-8-*-
import requests


def formput(param):
    url = "http://www.ibizsim.cn/games/make_decision?teamid=" + team_id

    # referer = "http://www.ibizsim.cn/games/decision?gameid=" + game_id + "&mode=old&periodid=" + period_id + \
    #    "&teamid=" + team_id + "&type=raw"
    referer = "http://www.ibizsim.cn/games/decision?gameid=" + game_id + "&mode=old" + \
        "&teamid=" + team_id + "&type=raw"

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Length': '2063',
        'Content-Type': 'application/x-www-form-urlencoded',
        # 'Cookie': cookies,
        'Host': 'www.ibizsim.cn',
        'Origin': 'http://www.ibizsim.cn',
        'Referer': referer,
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }

    r = requests.session()
    r.headers.update(headers)

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
    response = r.post(url, data=param)
    response.encoding=response.apparent_encoding 
    if response.status_code == 200:
        return response.text
    return response
    # response.encoding = 'utf-8'
    # html = response.content
    # html_doc=html.decode("utf-8","ignore")
    # print(html_doc.encode("utf-8-sig"))
    # print(response.text)
    #pat = "提交决策成功"
    # if len(re.findall(pat, response.content)) == 0:
    #    print("Failed to submit decisions")
    # else:
    #    print("Succesfully submited decisions")
    #    print(re.findall(pat, response.content)[0])


if __name__ == "__main__":
    from login import *
    from form_read import *
    username, password = '821621930@qq.com', 'Whoareyou59820'
    game_id, user_id, period_id = '177430', '351328', '3376977'
    team_id = user_id
    authenticity_token = get_token()
    login(authenticity_token, username, password)
    data = excel_data(filename, 5)
    html = formput(data)
    # with open('result.txt', 'w') as f:
    #    f.write(html)
    #    f.close()
    print(html)
