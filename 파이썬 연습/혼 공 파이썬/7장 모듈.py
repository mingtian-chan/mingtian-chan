# import 모듈  : 원하는 모듈을 가져옴
# 모듈이름.메소드이름 or 모듈이름.변수이름

# 모듈. 을 쓰기 싫다면?
# from 모듈이름 import 함수 or 변수이름
# -> 함수()나 변수를 바로 사용 가능

# from math * 를 하게되면 모두 가져오게 되는데, 이로 충돌이 일어날 수 있다, 그래서 조심해야함
# as 구문, 좀 짧게 줄여서 쓸 수 있게 함
# 예시 import numpy as np
# np.넘파이모듈의 함수이름()

# datetime 모듈
import datetime
now = datetime.datetime.now()
output_c = now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초")
output_d = (f"{now.year}년 {now.month}월 {now.day}일 {now.hour}시 {now.minute}분 {now.second}초")
print(output_c)
print(output_d)