import requests
import base64
import ssl,sys

def pic2txt(pic_path,txt_path):    
    url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic'  
    
    data = {}
    with open("token.txt","r") as file:
        token = file.read()
        data['access_token'] = token
    
    
    #读取图片  
    pic_file=open(pic_path,'rb')  
    image= pic_file.read()  
    file.close()  
    # 图片转base64
    data['image'] = base64.b64encode(image)  
    headers={
        "Content-Type":"application/x-www-form-urlencoded",
        "apikey":"uCQOH345678FsGi"
    }

    res = requests.post(url=url,headers=headers,data=data)
    result = res.json()
    with open(txt_path,"a") as f:
        for line in result["words_result"]:
            print(line["words"],end="")
            f.write(line["words"]+"\n")

def main():
    if len(sys.argv) == 3:  
        pic_path = sys.argv[1] # 图片路径
        txt_path = sys.argv[2] # 导出文字的路径
        pic2txt(pic_path,txt_path)
    else:
        print("输入图片路径和保存文本的路径 eg:pic2txt.py test.png test.txt")

if __name__ == "__main__":
    main()