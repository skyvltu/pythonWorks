"""
 날짜 : 2021/03/08
 이름 : 이승환
 내용 : 파이썬 크롤링 Selector 실습하기
"""
import requests as req
from bs4 import BeautifulSoup as bs

# 페이지 요청
resp = req.get('http://chhak.kr/py/test1.html')
resp.encoding ='utf-8'
print(resp.text)

# 파싱
dom = bs(resp.text, 'html.parser')

tag_tit = dom.html.body.h1
tag_txt = dom.select_one('#txt')
tag_li1 = dom.select_one('ul > li:nth-child(1)')
tag_li2 = dom.select_one('ul > li:nth-child(2)')
tag_li_last = dom.select_one('ul > li:last-child')
tag_lis = dom.select('ul > li')

print('tit :', tag_tit.text)
print('txt :', tag_txt.text)
print('li1 text :', tag_li1.text)
print('li2 text :', tag_li2.text)
print('li last text :', tag_li_last.text)
print('lis :', tag_lis)

for li in tag_lis
    print('li text :', li.text)
