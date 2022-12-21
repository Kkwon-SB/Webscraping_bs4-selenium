import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=796218&weekday=wed"
res = requests.get(url)
# print(res.text) #request 결과만 나옴 성공 & 실패
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup)
cartoons = soup.find_all("td", attrs={"class":"title"})
stars = soup.find_all("div", attrs={"class":"rating_type"})
# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"]
# print('title : ',title)
# print('Link : ','https://comic.naver.com'+link) # 실제 링크란과 맞춰주어야 함

total = 0

for cartoon, star in zip(cartoons,stars):
    print(cartoon.a.get_text(),': https://comic.naver.com'+ cartoon.a["href"], '평점 : ',star.strong.get_text() )
    total += float(star.strong.get_text())

print('\n평점 평균 : ',total/len(cartoons))













