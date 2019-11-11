from bs4 import BeautifulSoup
import re
import csv
def load_xml(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        xml = f.read()
    return xml

def parse(filepath):
    content = load_xml(filepath)
    soup = BeautifulSoup(content, 'xml')
    # 获取每一个sentences
    sentences = soup.find_all('sentence')
    data = []
    for sentence in sentences:
        # 每一个sentence 的 text 标签
        text = sentence.find('text').text
        aspectTerms = sentence.find_all('aspectTerm')
        for aspectTerm in aspectTerms:
            term = aspectTerm['term']
            ## 有换行和多行的情况
            term = re.sub(r'\s{2,}', '', term)
            polarity = aspectTerm['polarity']
            polarity = re.sub(r'\s{2,}', '', polarity)
            temp = [text,term,polarity]
            data.append(temp)
    return data

def write2csv(data):
    output_file = 'test.csv'
    with open(output_file,'w',encoding='utf-8') as f: 
        f.write(','.join(['text', 'term', 'polarity']) + '\n')
        for line in data:
            f.write(','.join(line) + '\n')


if __name__ == "__main__":
    # test()
    filepath = './Laptops train data.xml'
    data = parse(filepath)
    write2csv(data)