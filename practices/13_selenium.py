#자신의 웹 브라우저 드라이버를 설치해야 한다. (크롬)
#현재 브라우저의 버전과 드라이버의 버전을 맞춰주어야 한다.
#웹 브라우저 버전 확인 ->크롬창에서  chrome://version/
#드라이버 설치 : https://chromedriver.chromium.org/downloads
#압축 해제 후 자신의 vscode폴더에 드라이버exe파일을 옮기면 끝
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#[오류]Failed to read descriptor from node connection: 
#시스템에 부착된 장치가 작동하지 않습니다. (0x1F)  -> 에러를 제거하기 위한 코드
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

browser = webdriver.Chrome() #드라이버의 경로를 넣어주어야 한다. 같은 경로에 있을 경우 빈칸 가능

# 1.네이버 이동
browser.get("https://naver.com")

# 2.로그인 버튼 클릭
elem = browser.find_element(By.CLASS_NAME, "link_login") #기존 명령어 변경됨
elem.click()
time.sleep(1)
# 3. id pw입력
browser.find_element(By.ID, "id").send_keys('tnsqls1234')
browser.find_element(By.ID, "pw").send_keys('Kdnjfem12@') #네이버 로그인이 안됨?
time.sleep(1)
# 4.로그인 버튼 클릭
browser.find_element(By.ID, "log.login").click() #2번의 과정을 한줄로 요약

# time.sleep(2) #3초 대기 후 다음 코드 진행

# # 5.id pw 다시 입력
# browser.find_element(By.ID, "id").clear()#text 제거
# browser.find_element(By.ID, "id").send_keys('11111')

# # 6.html정보 가져오기
# print(browser.page_source)

# # 7. 브라우저 종료
# browser.close() #현재 탭만 종료
# browser.quit() #전체 브라우저 종료




