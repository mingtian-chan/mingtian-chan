# 랜덤의 진실 : 사실 진짜 랜덤이 아님, 시드 있으면 임의로 원하는 값을 만들어 낼 수 있다.
import random
import numpy as np

np.random.seed(0)
print('seed == 0')
print(np.random.rand(5))
print(np.random.rand(10))

print('seed == 0')
np.random.seed(0)
print(np.random.rand(5))
print(np.random.rand(10))

print('seed == 2')
np.random.seed(2)
print(np.random.rand(5))
print(np.random.rand(10))

print(np.random.randint(10, size=10))
print(np.random.randint(10, 20, size=10))
print(np.random.randint(10, 20, size=(3, 5)))

# random 시드는 시드를 따로 제공하지 않으면 시스템 시간을 시드로 사용함

# 참고 https://ichi.pro/ko/numpy-laendeom-sideu-yecheug-ganeunghan-nansu-saengseong-geekscheoleom-126492530333368