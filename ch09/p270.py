"""
 날짜 : 2021/03/10
 이름 : 이승환
 내용 : 교재 p270 - news 자료 수집 예
"""
import urllib.request as req
from bs4 import BeautifulSoup

url = "http://media.daum.net"

res =req.urlopen(url)
source = res.read()

source = source.decode("utf-8")

html = BeautifulSoup(source, 'html.parser')

atags = html.select('a[class=link_txt]')


crawling_data = []

cnt = 0
for atag in atags:
    cnt += 1
    atagstr = str(atag.string)
    crawling_data.append(atagstr.strip())

print('수집한 자료 확인')
print(crawling_data)

import pickle

file = open('ch09/data/data.pickle', mode='wb')
pickle.dump(crawling_data, file)

file = open('ch09/data/data.pickle', mode='rb')
crawling_data = pickle.load(file)
print('pickle load')
print('crawling_data')