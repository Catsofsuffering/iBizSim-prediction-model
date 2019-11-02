# -*- coding: utf-8 -*-

# urls

token_url = 'http://www.ibizsim.cn/main/login'
login_url = 'http://www.ibizsim.cn//center/trylogin'
check_url = 'http://www.ibizsim.cn/games/mygames'
gu_url = 'http://www.ibizsim.cn/games/mygames'
tn_url = 'http://www.ibizsim.cn/main/myteam'

# headers

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

referer = ''
referer_header = {
    'Host': 'www.ibizsim.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'close',
    'Referer': referer,
    'Upgrade-Insecure-Requests': '1',
    'If-None-Match': '"92cb8a089131707b97b015c23e7073a7"'
}


# form_read

# 定义价格price_list
price_list = []
# 定义促销promotion_list
promotion_list = []
# 定义供货support_list
support_list = []
# 定义生产product_list
product_list = []
# 定义发展develop_list
develop_list = []
# 定义财务finance_list
finance_list = []

# 因为range函数，行列范围中的up项与实际相比加1

# 价格行列范围
price_low_row = 7
price_up_row = 11
price_low_col = 71
price_up_col = 76
# 促销行列范围
promotion_row = 11
promotion_low_col = 71
promotion_up_col = 75
# 供货行列范围
support_low_row = 14
support_up_row = 18
support_low_col = 71
support_up_col = 75
# 生产行列范围
product_low_row = 20
product_up_row = 24
product_low_col = 71
product_up_col = 76
# 发展行列范围
develop_row = 26
develop_low_col = 71
develop_up_col = 75
# 财务行列范围
finance_row = 29
finance_low_col = 71
finance_up_col = 76

# form_write

# 上期发债卷数
bond_row = 4
bond_col = 8
# 上期期末本金
principal_row = 5
principal_col = 8
# 上期期末企业状况
conditions_low_row = 4
conditions_up_row = 22
conditions_low_col = 4
conditions_up_col = 6
# 上期期末产品状况1
product1_low_row = 24
product1_up_row = 40
product1_low_col = 5
product1_up_col = 12
# 上期期末产品状况2
product2_low_row = 42
product2_up_row = 46
product2_low_col = 4
product2_up_col = 9
# 上期公共报表价格
price_low_row = 50
price_up_row = 70
price_low_col = 4
price_up_col = 20
# 上期市场份额
market_low_row = 73
market_up_row = 93
market_low_col = 4
market_up_col = 20
# 上期主要指标
indicators_low_row = 95
indicators_up_row = 115
indicators_low_col = 4
indicators_up_col = 12
