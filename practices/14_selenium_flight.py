# from os import times_result
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

browser = webdriver.Chrome()
browser.maximize_window()#창 최대화

# 홈 페이지 접속
url = "https://flight.naver.com/"

a = 'https://flight.naver.com/flights/international/ICN-FUK-20220808/FUK-ICN-20220825?adult=1&fareType=Y'

browser.get(a)

#가는 날 선택
time.sleep(2)
browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]").click()

#가는 날짜 선택 
time.sleep(2)
browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[2]/td[2]/button/b").click()


#오는 날 택 선택
browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[1]/div/button[2]/strong").click()

#오는 날 일자 선택
browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[4]/td[5]/button/b").click()

#도착 공항 선택
browser.find_elements(By.CLASS_NAME, "select_code__d6PLz")[1].click()#입력 칸 선택

time.sleep(2)
browser.find_elements(By.CLASS_NAME, "autocomplete_Collapse__tP3pM")[1].click() #1번째 인덱스는 일본
browser.find_elements(By.CLASS_NAME, "autocomplete_Airport__3_dRP")[3].click() #4번째 후쿠오카 선택



# browser.find_elements(By.LINK_TEXT, "오사카").click()

# browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[9]/div[2]/section/section/div/button[6]")#안됨

# browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[9]/div[2]/section/section/button[2]")

# browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[9]/div[2]/section/section/div/button[1]/span/i[1]").click()
# //*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/button[2]
# browser.find_element(By.CLASS_NAME, "autocomplete_input__1vVkF").click()
# browser.find_element(By.CLASS_NAME, "autocomplete_input__1vVkF").send_keys('오사카')
# time.sleep(2)
# browser.find_element(By.CLASS_NAME, "autocomplete_inner__3Owyw").click()


#항공권 검색
browser.find_element(By.CLASS_NAME, "searchBox_txt__3RoCw").click()

#10은 최대 대기 시간
# try:
#     elem = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "concurrent_select_schedule__3O1pT"))[0])
#     print(elem.text)
# finally:
#     pass
    # browser.quit()

# elem = browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[5]/div/div[3]/div[1]/div/button")

WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/div[1]/div[5]/div/div[3]/div[1]/div/button")))

aa = browser.find_elements(By.CLASS_NAME, "concurrent_select_schedule__3O1pT")[0]
print(aa.text)
# //*[@id="__next"]/div/div[1]/div[5]/div/div[3]/div[1]/div/button

browser.find_element(By.CLASS_NAME, "concurrent_ConcurrentList__1EKaB").text

