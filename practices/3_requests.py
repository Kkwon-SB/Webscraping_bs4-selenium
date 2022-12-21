import requests
res = requests.get("http://google.com")
res.raise_for_status()#올바른 request.get과정이 이뤄짐

# print('응답코드: ', res.status_code)
# if res.status_code == requests.codes.ok: #200이랑 같은 의미
#     print("normal")
# else:
#     print("error_code : ",res.status_code)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)





























