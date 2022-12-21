import re
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

for i in range(1,6):
    print('현재 페이지 : ',i)
    url = "https://browse.gmarket.co.kr/search?keyword=%EB%85%B8%ED%8A%B8%EB%B6%81&k=32&p={}".format(i)
    res = requests.get(url,headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'lxml')

    items = soup.find_all('div', attrs={'class':"box__component box__component-itemcard box__component-itemcard--general"})

    for item in items:
        name = item.find('span', attrs={'class':"text__item"}).get_text()
        ori_price = item.find('strong', attrs={'class':"text text__value"}).get_text()
        event = item.find('span', attrs={'class':"box__tag box__tag-card"})
        event2 = item.find('span', attrs={'class':"box__tag box__tag-gift"})
        if event:
            event = event.get_text()
        else:
            event = ''

        if event2:
            event2 = event2.get_text()
        else:
            event2 = ''

        print('상품명 : ',name, '\n가격 :', ori_price , '\n',event, event2, '\n\n')
