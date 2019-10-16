# -*- coding: UTF-8 -*-
# 用于设置初始化的环境
import os

def check_selenium():
    try:
        output = os.popen('pip install selenium')
        print output.read()
        print("succesfully installed selenium")
    except:
        print output.read()

def set_path():
    try:
        # path = os.path.abspath(os.path.dirname(os.getcwd()))
        path = os.path.abspath('.')
        print path
        command = 'setx /m PATH "%PATH%;'+path+'"'
        output = os.popen(command)
        print output.read()
        print("succesfully set the path")
    except:
        print output.read()


if __name__ == "__main__":
    check_selenium()
    set_path()