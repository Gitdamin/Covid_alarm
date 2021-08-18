# :bulb: 코로나 확진자수 전송 서비스 :bulb:
>#### 라즈베리파이 기기와 카카오채널 플랫폼을 활용한 서비스
_____________
## :dizzy: 배경
<img src="https://user-images.githubusercontent.com/86276347/129881730-6cb1fb0c-734e-4629-a6d0-96d8266e4cac.JPG" width="600px" height="125px" title="33" alt="33"></img><br/>
> NAVER 검색/ 코로나 확진자수/ 2021-08-14
* 2021-08-14 일자 기준 코로나19 감염 확진자수는 여전히 줄지 않는 추세
* 많은 사람들이 코로나19로 인해 불안감이 높아짐
* 매일 인터넷에 접속하여 검색하는 것은 비효율적
* 능동적인 웹 크롤링 방식을 활용해 사용자에게 매일 코로나 확진자수를 전송해주는 서비스 고려
________
## :dizzy: 기능 및 내용
### 구성도 :fire: 
<img src="https://user-images.githubusercontent.com/86276347/129881719-f6798ce9-4b72-49ef-9c24-e03c3df6f753.jpg" width="450px" height="225px" title="33" alt="33"></img><br/>
<br/>

### 사용 기술 :fire: 

* *Selenium*을 사용하여 라즈베리파이 기기 자체에서 인터넷 접속
* 접근성과 이용성 향상 고려 
* 카카오 채널을 활용하여 능동적으로 사용자에게 알림
* 웹 페이지 내에서 검색어를 입력 후 원하는 값의 ```XPath``` 분석을 통해 ```element``` 값 받아옴
```python
element = driver.find_element_by_xpath('//*[@id="_cs_production_type"]/div/div[4]/div/div[3]/div[1]/div/table/tbody/tr[1]/td[3]/span').text
```
* 해당 ```element``` 값을 다시 메시지 창에 입력 후 전송
* 사용자는 매일 아침 인터넷 접속 없이도 카카오톡을 통해 '오늘의 확진자 수' 인지
<br/>

### 알고리즘 순서 :fire: 

1. 아침 10시 정각
2. 라즈베리파이 코드 작동 시작
3. 크롤링(소프트웨어 자동화)을 통해 인터넷(크롬) 접속 
4. 네이버 접속 및 검색어 자동 입력 
5. 원하는 ```value```를 ```element``` 값으로 받아오기
6. 사용자의 카카오 채널에 접근 및 로그인
7. 사용자에게 보낼 메시지와 element 값 전송
8. 사용자는 카카오톡을 통해 '오늘의 확진자 수' 전달받음. 
__________
## :dizzy: 사용 예시

* 사용자가 원하는 시간으로 조정 가능
>주의) 확진자 수가 새롭게 업데이트 되는 시각 이후로 조정
```python
#알림 전송 시간 
Time = 10  
```
<br/>
  
* 사용자의 위치에 따라 ```city``` 다르게 설정
```python
# 지역 예시
city = '서울'
naver_input = urllib.parse.quote(city + ' 코로나 확진자')
CovidURL = 'https://search.naver.com/search.naver?ie=utf8&query='+ naver_input
```
<br/>

* 사용자가 실제 전달받는 메시지 예시<br/>
<img src="https://user-images.githubusercontent.com/86276347/129438621-d11b5785-eab6-4ec6-810e-5b99a4408b9d.jpg" width="580px" height="100px" title="11" alt="11"></img><br/>
