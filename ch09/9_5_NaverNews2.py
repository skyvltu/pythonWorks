"""
 날짜 : 2021/03/09
 이름 : 이승환
 내용 : 파이썬 가상 브라우저를 이용한 네이버 뉴스 수집
"""
from selenium import webdriver
from openpyxl import Workbook
from datetime import datetime

browser = webdriver.Chrome('./chromedriver.exe')

browser.get('http://naver.com')

btn_news = browser.find_element_by_css_selector('#NM_FAVORITE > div.group_nav > ul.list_nav.NM_FAVORITE_LIST > li:nth-child(2) > a')
btn_news.click()

btn_sokbo = browser.find_element_by_css_selector('#lnb > ul > li:nth-child(2) > a')
btn_sokbo.click()


workbook = Workbook()
sheet = workbook.active

i = 0

while True:
    tags_title = browser.find_elements_by_css_selector('#main_content > div.list_body.newsflash_body > ul > li > dl > dt:nth-child(2) > a')
    tags_dl = browser.find_elements_by_css_selector('#main_content > div.list_body.newsflash_body > ul > li > dl')

    for tit in tags_title:
        print(tit.text)

    for dl in tags_dl:
        #print(tit.text)
        try:
            title  = dl.find_element_by_css_selector('dt:nth-child(2) > a')
            writer = dl.find_element_by_css_selector('dd > span.writing')
            now    = "{:%Y-%m-%d}".format(datetime.now())

            sheet.append([writer.text, title.text.strip(), now])

        except:
            print('예외발생...')

    tags_paging = browser.find_elements_by_css_selector('#main_content > div.paging > a')
    tags_paging[0].click()

    i += 1

    # 10번까지 제목 출력 후 종료
    if i > 8:
        break

workbook.save('C:/Users/user/Desktop/News2.xlsx')
workbook.close()

browser.quit()