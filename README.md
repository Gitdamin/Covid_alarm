# :bulb: 코로나 확진자 수 전송 서비스 :bulb:
>#### 라즈베리파이 기기와 카카오채널 플랫폼을 활용한 서비스
_____________
## :dizzy: 배경
<img src="https://user-images.githubusercontent.com/86276347/129881730-6cb1fb0c-734e-4629-a6d0-96d8266e4cac.JPG" width="520px" height="105px" title="33" alt="33"></img><br/>
> NAVER 검색/ 코로나 확진자수/ 2021-08-14
* 2021-08-14 일자 기준 코로나19 감염 확진자수는 여전히 줄지 않는 추세
* 코로나19로 인한 불안감 증가
* 인터넷에 매일 접속하여 검색하는 것은 비효율적
* 미디어의 능동적인 방식을 활용해 사용자에게 자동으로 확진자 수를 전송해주는 서비스 고려
________
## :dizzy: 기능 및 내용
### 구성도 :fire: 
<img src="https://user-images.githubusercontent.com/86276347/129881719-f6798ce9-4b72-49ef-9c24-e03c3df6f753.jpg" width="450px" height="190px" title="33" alt="33"></img><br/>
<br/>

### 사용 기술 :fire: 

* *Selenium*을 사용하여 라즈베리파이 기기 자체에서 인터넷 접속
* 접근성과 이용성 향상 고려 
* 알고리즘 단순화 + 속도 증가
* 웹 페이지 내에서 검색어를 입력 후 원하는 값의 ```XPath``` 를 바탕으로 ```element``` 값 받아오기
```python
element = driver.find_element_by_xpath('//*[@id="_cs_production_type"]/div/div[4]/div/div[3]/div[1]/div/table/tbody/tr[1]/td[3]/span').text
```
* 카카오 채널을 활용하여 능동적으로 사용자에게 알림 전송
* 해당 ```element``` 값을 메시지 창에 입력 후 사용자에게 전달
* 사용자는 매일 아침 인터넷 접속 없이도 카카오톡을 통해 '오늘의 확진자 수' 인지
<br/>

### 순서 및 흐름 :fire: 

1. 지정한 시각
2. 라즈베리파이 코드 작동 시작
3. 웹 자동화를 통해 인터넷(크롬) 로드 
4. 네이버 접속 및 검색어 자동 입력 
5. 원하는 ```value```를 ```element``` 값으로 받아오기
6. 사용자의 카카오 채널 로드 및 로그인
7. 관련 메시지와 element 값 전송
8. 사용자는 카카오톡을 통해 '오늘의 확진자 수' 전달 받음. 
__________
## :dizzy: 특장점

* 라즈베리파이를 활용하여 효율 증가
* 사용자의 편리성 및 이용성 증가
* 현 시대에 알맞은 서비스
* 사용자의 나이대에 관계없는 서비스
__________
## :dizzy: Setting + Start

```raspberry pi 3+, Selenium, kakao```
<br/>

1. download
```
git clone https://github.com/Gitdamin/Covid_alarm.git
cd Covid_alarm
```
2. 사용자 맞춤 조정
>주의) 확진자 수가 새롭게 업데이트 되는 시각 이후로 조정
```python
# 알림 전송 시간 예시
Time = 10  
.
.
# 지역 예시
city = '서울'
naver_input = urllib.parse.quote(city + ' 코로나 확진자')
```
3. 실제 사용
```covid_alarm.py``` 실행

* 사용자가 실제 전달받는 메시지<br/>
><img src="https://user-images.githubusercontent.com/86276347/129887480-6fe89e9e-a3e8-45c2-a74e-a264c6505d86.JPG" width="440px" height="150px" title="11" alt="11"></img><br/>
