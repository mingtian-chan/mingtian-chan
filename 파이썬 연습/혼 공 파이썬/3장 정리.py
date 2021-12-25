# boolean
# 연산자 == 같다 != 다르다 <= 작거나 같다 >= 크거나 같다 < 작다 > 크다

# 날짜/ 시간 출력하기
import datetime

now = datetime.datetime.now()

print(now.year, '년')
print(now.month, '월')
print(now.day, '일')
print(now.hour, '시')
print(now.minute, '분')
print(now.second, '초')

print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
))

if now.hour  > 12:
    print('지금은 {}시로 ,오후입니다.'.format(now.hour))
else:
    print('지금은 {}시로, 오전입니다.'.format(now.hour))

# True or False : 뭐가 없으면 False
