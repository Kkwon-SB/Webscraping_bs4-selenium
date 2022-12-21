import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

cartoons = soup.find_all("a", attrs={"class":"title"}) #하나가 아닌 전체 가져옴
#class속성이 title인 모든 'a' element를 반환
for index,i in enumerate(cartoons):
    print(index+1 , i.get_text())