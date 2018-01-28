# 博客爬虫

> 下载博客，并转成Markdown的形式

## 使用的python库

* beautifulsoup4
* requests
* html2text

## 目录
* csdn.py csdn博客爬虫

* jianshu.py 简书博客爬虫

* juejin.py 掘金文章爬虫

* segmentfault.py segmentfault文章爬虫

* zhihu.py 知乎的文章

## 使用方法举例

```
import html2md

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
```