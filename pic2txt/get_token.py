import requests
import ssl,sys
# 获取token
# 填入 自己的APIKEY 和SK
api_key = "uCQOHvpqP3456789G7KCFsGi"
secret_key = "cIq2345678906C5G0EehQ5"
host =  'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+api_key+'&client_secret='+secret_key

headers = {
    'Content-Type':'application/json;charset=UTF-8'
}

res = requests.get(url=host,headers=headers).json()
print(res['access_token'])
txt = res['access_token']
with open("token.txt",'w') as file:
    file.write(txt)