# coding=utf-8
from selenium import webdriver
import os

def add_path():
    current_path = os.path.abspath(os.path.dirname(__file__))
    # 读取的字符c是小写，PATH无法识别
    current_path.replace("c","C",1) 
    # print (current_path)
    # 将webdriver临时添加到PATH中
    os.environ["PATH"] += ";"+current_path
    # print(os.environ["PATH"])

def login(username,password):
    browser = webdriver.Chrome()
    browser.get("http://www.ibizsim.cn/main/login")
    time.sleep(2)
    name = browser.find_element_by_name("name")
    name.send_keys("账号")
    passwd = browser.find_element_by_name("password")
    passwd.send_keys("密码")
    login_button = browser.find_element_by_name("commit")
    login_button.click()

if __name__ == "__main__":
    add_path()
    username = "821621930@qq.com"
    password = "Whoareyou59820"
    login(username,password)