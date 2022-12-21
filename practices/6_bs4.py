# XML이란 단순한 문자열을 넘어서서, 내부적으로 트리 구조를 가지고 있는 파일을 표현하기 위해 사용하는 마크업 언어입니다.
# -웹페이지를 보여주기 위해 사용되는 html 파일이 XML의 가장 대표적인 예시입니다.
# -우리가 친숙하게 사용하는 MS Office의 워드, 엑셀, 파워포인트 파일(docx, xlsx, pptx)도 XML의 일종입니다.
# -따라서 XML을 해석하는 프로그램(parser라고 부릅니다.)을 미리 준비해야 html, docx, xlsx, pptx와 같이 우리가 흔히 다루는 파일을 처리할 수 있습니다.
# -Python에서 XML parser로서 주로 이용되는 패키지는 lxml입니다.
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.a) #첫번째에 있는 a태그
# print(soup.find("a", attrs={"class":"Nbtn_upload"})) 
# print(soup.find(attrs={"class":"Nbtn_upload"})) #해당 크래스가 하나라 이런 방식도 가능
#첫번째에 있는 a태그의 attributes(속성)에서 "class":"Nbtn_upload" 인 엘리먼트를 가져옴
# print(soup.find("li", attrs={"class":"rank01"})) 


rank1 = (soup.find("li", attrs={"class":"rank01"})) 
# print(rank1.a.get_text())
# rank2 = rank1.next_sibling.next_sibling #원래 한번 해도 될것 같지만 보이지 않는 개행이 있어서 그런듯
# print(rank2.a.get_text()) #이전으로 가는건previous_element 하면 됨

# rank2 = rank1.find_next_sibling("li") #이런 방법도 있음 
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li") #이런 방법도 있음 
# print(rank3.a.get_text())

# print(rank1.find_next_siblings("li")) #전체 다 가져옴

webtoon = soup.find("a", text="세기말 풋사과 보습학원-69화")
#조건문처럼 a태그의 text가 해당 문장인 a태그 가져오기
print(webtoon)













