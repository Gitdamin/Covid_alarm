# :bulb: 코로나 확진자수 전송 서비스 :bulb:
>#### 라즈베리파이 기기와 카카오채널 플랫폼을 활용한 서비스
_____________
## :dizzy: 배경
<img src="https://user-images.githubusercontent.com/86276347/129440832-2368b58c-c531-4387-b7bc-38441c8e2808.JPG" width="700px" height="450px" title="33" alt="33"></img><br/>
* 2021-08-14 일자 기준 코로나19 감염 확진자수는 여전히 줄지 않는 추세
* 많은 사람들이 코로나19로 인해 불안감이 높아짐
* 매일 인터넷에 접속하여 검색하는 것은 비효율적
* 능동적인 웹 크롤링 방식을 활용해 사용자에게 매일 코로나 확진자수를 전송해주는 서비스 고려
________
## :dizzy: 기능 및 내용
* *Selenium*을 사용하여 웹 크롤링을 통해 라즈베리파이 기기 자체에서 인터넷 접속
* 접근성이 좋은 카카오 채널을 활용하여 능동적으로 사용자에게 알림이 전송되도록 설정
* 매일 지정된 시간마다 알림이 전송되도록 설정
* 자동으로 코드가 실행되도록 라즈베리파이 
* 사용자는 카카오톡으로 통해 아침마다 확진자수를 빠르게 확인 가능
__________
## :dizzy: 사용
* 현재 거주하는 지역을 기준으로 코로나 확진자수를 전달
```python
city = '서울'
naver_input = urllib.parse.quote(city + ' 코로나 확진자')
CovidURL = 'https://search.naver.com/search.naver?ie=utf8&query='+ naver_input
```
>사용자의 위치에 따라 ```city```의 글자를 다르게 설정
<br/>

* 사용자의 카카오톡으로 전송  
>사용자가 전달받는 메시지 예시  
<img src="https://user-images.githubusercontent.com/86276347/129438621-d11b5785-eab6-4ec6-810e-5b99a4408b9d.jpg" width="780px" height="165px" title="11" alt="11"></img><br/>
<br/>
 
* 전송 시간 설정
```python
Time = 10  #알림 전송 시간
```
>매일 코로나 확진자 수가 업데이트되는 시간에 맞추기
