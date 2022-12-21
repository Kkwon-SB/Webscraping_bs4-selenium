import re
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

for i in range(2021,2016,-1):   #2021~2017까지
    print('현재 페이지 : ',i)
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(i)
    res = requests.get(url,headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'lxml')
    
    images = soup.find_all('img', attrs={'class':'thumb_img'})
    for idx,image in enumerate(images):
        image_url = image['src']
        if image['src'].startswith('//'):
            image_url = 'https:'+image['src']

        # print(image_url)
        image_url2 = requests.get(image_url,headers=headers)
        res.raise_for_status()

        with open("movie{}_{}.jpg".format(i,idx+1), 'wb') as f:
            f.write(image_url2.content)

        if idx >= 4:
            break