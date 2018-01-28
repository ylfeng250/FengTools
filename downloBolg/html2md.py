import requests
import re
import random
import html2text
import os
from bs4 import BeautifulSoup

import csdn
import jianshu
import juejin
import segmentfault

def checkSite(url):
    """
    判断是哪个站点，并使用相应的下载器
    """
    if url.find('csdn') != -1: # csdn
        csdn.downLoad(url)
    elif url.find('jianshu') != -1: # 简书
        jianshu.downLoad(url)
    elif url.find('juejin') != -1: # 掘金
        juejin.downDLoad(url)
    elif url.find('segmentfault') != -1:
        segmentfault.downLoad(url)
    else:
        doelse(url)



def doelse(url):
    useragents = [
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    ]
    headers = {
        'User-Agent': random.choice(useragents)
    }
    res = requests.get(url=url ,headers=headers) # 获取整个html页面
    h = html2text.HTML2Text()
    h.ignore_links = False
    soup = BeautifulSoup(res.text,'html5lib')
    title = soup.title.text # 获取标题
    html = str(soup.body)
    article = h.handle(html)

    pwd = os.getcwd() # 获取当前文件的路径
    dirpath = pwd + '/Else/'
    if not os.path.exists(dirpath):# 判断目录是否存在，不存在则创建新的目录
        os.makedirs(dirpath)
    with open(dirpath+title+'.html','w',encoding=res.encoding) as f:
        f.write(str(html)) # 创建html页面
    with open(dirpath+title+'.md','w',encoding=res.encoding) as f:
        f.write(article) # 创建markdown文件
    
    
if __name__ == "__main__":
    url_list = [
        'http://blog.csdn.net/qq_37482544/article/details/63720726', # csdn
        'https://www.jianshu.com/p/b6220e99df2d', # jianshu
        'https://juejin.im/post/5a68437b6fb9a01ca47aabc6', # juejin
        'https://segmentfault.com/a/1190000011929414', # segmentfault
        'http://www.voidcn.com/article/p-giqfrkhb-bbr.html', # 其他
        'https://www.cnblogs.com/zxqstrong/p/4789105.html'
    ]
    for url in url_list:
        checkSite(url)