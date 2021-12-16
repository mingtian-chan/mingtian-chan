import random

FH = open('참가자.txt','r',encoding='UTF8')  # encoding= 'UTF8'을 안 붙일경우 에러남
#  UnicodeDecodeError: 'cp949' codec can't decode byte 0xed in position 6: illegal multibyte sequence
a = FH.readlines()
b =[l.strip() for l in a]
b = random.sample(b,5)
print(f'치킨 당첨자 : {b[:1]}')
print(f'커피 당첨자 : {b[1:]}')
FH.close()
