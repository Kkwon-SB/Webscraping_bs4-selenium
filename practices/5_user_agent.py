#user agent를 사용하는 이유 : 
#무분별한 크롤링과 서버 과부하를 막기 위해 사람이 직접 접속한게 아니라 
#프로그램을 통하여 접속하는 것을 차단하는 사이트들이 있다. 즉, 나에 대한 정보를 주어 
#단순 request로 가져올 수 없는 정보를 가져오기 위함

import requests

url = "http://nadocoding.tstory.com"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}


res = requests.get(url, headers=headers)
res.raise_for_status()
with open("nadocoding.html", 'w', encoding='utf8') as f:
    f.write(res.text)














