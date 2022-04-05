#크롬으로 접속 & 네이버에 '서울 코로나 확진자' 검색
#확진자 수를 입력받아 element 값에 저장 
#개인 카카오 채널 로그인 & 확진자 수 입력 후 전송 

from selenium import webdriver
from time import sleep 
import datetime
import urllib

city = '서울'  #사용자의 위치
naver_input = urllib.parse.quote(city + ' 코로나 확진자')
CovidURL = 'https://search.naver.com/search.naver?ie=utf8&query='+ naver_input
Time = 10  #알림 전송 시간 

def kakao():
    
    #kakao_setting
    id = '~'  #개인 아이디
    pw = '~'  #개인 비밀번호

    KaKaoURL = 'https://accounts.kakao.com/login/kakaoforbusiness?continue=https://center-pf.kakao.com/'
    ChatRoom = '~'  #사용자가 설정한 개인 채널의 주소
    options = webdriver.ChromeOptions()
      
          
    #크롬 드라이버 로드
    driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', options=options)
    driver.implicitly_wait(3)
    
    #user-agent 변경
    options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.187")  
    
    #kakao 드라이버 로드
    driver.get(CovidURL)
    sleep(5)
    #확진자수 읽어오기
    element = driver.find_element_by_xpath('//*[@id="_cs_production_type"]/div/div[4]/div/div[3]/div[1]/div/table/tbody/tr[1]/td[3]/span').text
    
    #login
    driver.get(KaKaoURL)
    sleep(3)
    driver.find_element_by_id('id_email_2').send_keys(id)
    driver.find_element_by_id('id_password_3').send_keys(pw)
    driver.find_element_by_xpath('//*[@id="login-form"]/fieldset/div[8]/button[1]').click()
    sleep(1)
        
    #채팅방 로드
    driver.get(ChatRoom)
    sleep(1)
    
    #글 작성
    driver.find_element_by_id('chatWrite').send_keys('오늘 ' + city + '의 신규 확진자수는 ' + element + '명 입니다.')  #메시지 작성
    driver.find_element_by_xpath('//*[@id="kakaoWrap"]/div[1]/div[2]/div/div[2]/div[2]/form/fieldset/button').click()  #전송버튼
    
   
    sleep(2)
    driver.quit()
    sleep(1)
    # exit()
    

while True:
    
    now = datetime.datetime.now()
    if (now.hour == Time) : 
        
           kakao()
    
   
      
 
       
