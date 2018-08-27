#!/usr/bin/env python
import argparse
import requests

class Ecnu:
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def login(self):
        url = "https://login.ecnu.edu.cn/include/auth_action.php"

        postData ={
            'action': 'login',
            'username': self.username,
            'password': self.password,
            'ac_id': 1,
            'save_me': 0,
            'ajax': 1,
        }

        res = requests.post(url=url,data=postData)
        if res.status_code == 200:
            print(self.username,"login successful")


if __name__ == "__main__":
    ## 创建参数解析对象
    parser = argparse.ArgumentParser()

    ## 添加需要解析的参数
    parser.add_argument('-u',required=True,help="your student id for ecnu")
    parser.add_argument('-p',required=True,help="your password for public database")

    ## 解析参数
    args = parser.parse_args()

    ## 获取用户名和密码
    username = args.u
    password = args.p

    ## 创建Ecnu对象
    ecnu = Ecnu(username,password)
    ecnu.login()
