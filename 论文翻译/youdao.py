import requests
import json
import sys
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
"""
读取pdf转成txt
"""
def pdf_2_txt(pdf) :
    outfile = pdf + '.txt'
    args = [pdf]

    debug = 0
    pagenos = set()
    password = ''
    maxpages = 0
    rotation = 0
    codec = 'utf-8'   #输出编码
    caching = True
    imagewriter = None
    laparams = LAParams()

    PDFResourceManager.debug = debug
    PDFPageInterpreter.debug = debug

    rsrcmgr = PDFResourceManager(caching=caching)
    outfp = open(outfile,'w',encoding="utf8")
    device = TextConverter(rsrcmgr, outfp, codec=codec, laparams=laparams,imagewriter=imagewriter)
    for fname in args:
        fp = open(fname,'rb')
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        #处理文档对象中每一页的内容
        for page in PDFPage.get_pages(fp, pagenos,
                          maxpages=maxpages, password=password,
                          caching=caching, check_extractable=True) :
            page.rotate = (page.rotate+rotation) % 360
            interpreter.process_page(page)
        fp.close()
    device.close()
    outfp.close()
    return outfile
"""
调用有道翻译
"""
def translate(content):
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://www.youdao.com/'
    data = {}
    data['type'] = 'AUTO'
    data['i'] = content
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['ue'] = 'UTF-8'
    data['action'] = 'FY_BY_CLICKBUTTON'
    data['typoResult'] = 'false'
    headers = {
        'Host':'fanyi.youdao.com',
        'Origin':'http://fanyi.youdao.com',
        'Referer':'http://fanyi.youdao.com/',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest',
    }
    res = requests.post(url,data=data,headers=headers)
    # target = res.json()
    # print('翻译的结果：%s' % target['translateResult'][0][0]['tgt'])
    target = res.json()
    count = 0
    # result = target["translateResult"][0][0]["tgt"]
    for items in target["translateResult"]:
        for item in items:
            with open('result.txt','a+',encoding="utf8") as file:
                file.write(item["tgt"]+'\n')
"""
开始逐句翻译
"""
def start_translate(filename):
    with open(filename,'r',encoding="utf8") as infile:
        for line in infile.readlines():
            if len(line) >1 :
                translate(line)
"""
格式化从pdf转成的txt
"""
def format_txt(openfile):
    outputfile = "k"+openfile
    with open(openfile,'r',encoding="utf8") as file:
        lines = file.read().splitlines()
    output = open(outputfile,"a+",encoding="utf8")
    for line in lines:
        if len(line):
            output.write(line[:-1])
        else:
            output.write('\n')
    output.close()

    return outputfile

if __name__ == "__main__":
    inputfile = sys.argv[1]
    pdf_2_txt_file = pdf_2_txt(inputfile)
    format_txt_file = format_txt(pdf_2_txt_file)
    start_translate(format_txt_file)
