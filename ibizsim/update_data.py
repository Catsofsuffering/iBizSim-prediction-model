# -*- coding=utf-8 -*-
import requests
from bs4 import BeautifulSoup
import http.cookiejar as cookielib

# 获取已经保存在ibizsimCookies.txt的cookie值
s = requests.session()
s.cookies = cookielib.LWPCookieJar(filename="ibizsimCookies.txt")
s.cookies.load(ignore_discard=True, ignore_expires=True)

