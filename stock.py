# 네이버를 통해 주식 정보를 가져와 csv파일로 저장.

import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok="

filename = '시가총액.csv'
#엑셀파일에서 한글이 깨지는 경우 encoding='utf8' -> 'utf-8-sig' 
f = open(filename, 'w', encoding='utf8', newline="")#newline="" 안하면 각 줄마다 띄어쓰기됨
writer = csv.writer(f)

title = 'N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE'.split("\t")
writer.writerow(title)

for i in range(1, 4): #페이지당 50
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    stocks = soup.find('table', attrs={'class':'type_2'}).find('tbody').find_all('tr')    
    for stock in stocks:
        
        cols = stock.find_all('td')

#길이가 1인 경우(쓸모없는경우) -> 아래까지 가지말고 지나가라는 의미(다음 for문 진행)
        if len(cols) <= 1: 
            continue
        data = [col.get_text().strip() for col in cols]
        # print(data)
        writer.writerow(data)