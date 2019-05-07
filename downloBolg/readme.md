写的一个将博客转成markdown的脚本，目前支持简书，知乎，CSDN,segmentfault,掘金
使用方法 `python html2md.py -u <url>`

由于博客类网站页面渲染方式和反爬技术的变化，这里不再维护。
基本思路是通过分析网页中正文部分，然后通过BeautifulSoup获取html,在通过`tomd.py`转换成markdown