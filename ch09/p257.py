"""
 날짜 : 2021/03/10
 이름 : 이승환
 내용 : 교재 p257 - 원격 서버에서 수집 예
"""


url = 'http://www.naver.com/index.html'

res = urllib.request.urlopen(url)
data = res.read()

src = data.decode("utf-8")
print(src)

html = BeautifulSoup(src, 'html.parser')
print(html)

a = html.find('a')
print('a tag :', a)
print('a tag')

