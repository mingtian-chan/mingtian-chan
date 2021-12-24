import random
try:
    print('UTF8이 아닐경우 ')
    FH = open('참가자.txt','r')  # encoding= 'UTF8'을 안 붙일경우 에러남 -- why?? 한글은 ASCII에서 지원을 안하기때문

    #  UnicodeDecodeError: 'cp949' codec can't decode byte 0xed in position 6: illegal multibyte sequence
    a = FH.readlines()
    b =[l.strip() for l in a] # strip하는 이유 : '\n'을 제거하기위해서
    b = random.sample(b,5)
    print(f'치킨 당첨자 : {b[:1]}')
    print(f'커피 당첨자 : {b[1:]}')
    FH.close()

except:
    print('UTF8을 쓸 경우')
    FH = open('참가자.txt', 'r',encoding='UTF8')  # encoding= 'UTF8'을 안 붙일경우 에러남 -- why?? 한글은 ASCII에서 지원을 안하기때문
    #  UnicodeDecodeError: 'cp949' codec can't decode byte 0xed in position 6: illegal multibyte sequence
    a = FH.readlines()
    b = [l.strip() for l in a]  # strip하는 이유 : '\n'을 제거하기위해서
    b = random.sample(b, 5)
    print(f'치킨 당첨자 : {b[:1]}')
    print(f'커피 당첨자 : {b[1:]}')
    FH.close()
