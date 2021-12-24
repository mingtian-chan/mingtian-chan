# 프로그램이 처리할 수 있는 모든것 = data, 자료
# 자료형 data type - 문자열 string , 숫자 number, 불 boolean

print(type('안녕하세요'))
# str ( string 문자열)
print(type(234))
# int  ( integer 정수)

# escape character : \ 와 조합해서 쓰는 문자
# 종류 \' \" \n \t \\ 등

# 여러줄 문자열 ''' ~~~~~~~` 하고 무슨 지랄을 해도 ''' 로 끝나면 그 사이는 전부 처리해줌

print('''
가나다라 마바사
아자차카 타파하
''')  # 줄바꿈을 의도적으로 한거

print('''\
가나다라 마바사
아자차카 타파하\
''')  # 줄바꿈을 의도적으로 안해줌

# 문자열끼린 + 가 되지만, 문자열과 숫자는 + 가 안됨

# indexing 문자열의 순서를 보는데, 0부터 시작함 -1은 젤끝 안녕하세요안녕하세요 > -5-4-3-2-101234 순임
# 인덱싱을 하더라도, 원본이 변하지는 않음

# 정수 int ( integer), 부동소수 float ( floating point)

# string_a = input('입력 a: ')
# string_b = input('입력 b: ')
# int_a = int(string_a)
# int_b = int(string_b)
# print('문자열 자료 :', string_a + string_b)
# print('숫자 자료 : ', int_a + int_b)

# 변수 선언 - 변수를 생성함, 변수 할당 - 변수에 값을 넣는것 ex a = 1, 변수 참조 - 변수에서 값을 꺼내는 것

# format함수
print('{}'.format('123'))

print('{:d}'.format(12))  # 기본출력
print('{:5d}'.format(12))  # 5칸만큼 오른쪽으로 땡기고 뒤에서부터 채우기
print('{:5d}'.format(12345123))  # 5칸보다 적은데 적어야하는게 많으면 그냥 주욱 적어버림( 글자 형식을 못 맞춤)
print('{:10d}'.format(12))  # 10칸
print('{:05d}'.format(12))  # 5칸을 오른쪽으로 댕기고 뒤에서부터 채우고 남는칸은 0으로 채움
print('{:010d}'.format(12))  # 10칸

print('{:0.3f}'.format(12.1234))  # 소숫점 세자리
print('{:15.3f}'.format(12.1234))  # 15칸을 당기고 소숫점 세자리 컷
print('{:0.2f}'.format(12.1234))  # 소숫점 두자리
print('{:0.1f}'.format(12.1234))  # 소숫점 한자리

print ('{:g}'.format(12.0))  # 의미없는 .0 에서 0 제거

# # is OO() 문자열이 ㅇㅇ 인지 True or False 로 반환

# isalnum() 문자열이 알파뱃 + 숫자
# isalpha() 문자열이 알파뱃
# isidentifier() 문자열이 식별자로 사용될 수 있는지  ## 처음 알았음 important
# isdecimal() 문자열이 정수형태인지
# isdigit() 문자열이 숫자로 인식될 수 있는지
# isspace() 문자열이 전부 공백인지
# islower() 문자열이 모두 소문자인지
# isupper() 문자열이 모두 대문자인지

print('AlPhabet'.isalpha())  # 알파벳인지 ? True
print('Alphabet'.islower())  # 모두 소문자인지? False
# print(1123.isdigit()) -  syntax error 왜냐? 문자열을 판독해야하는데 숫자가 들어갔기때문

# find() , rfind()
print('안녕안녕하세요'.find('안녕'))  # 왼쪽에서부터 제일 빠른 '안녕'을 찾음
print('안녕안녕하세요'.find('안세요'))  # 없으면 -1을 출력

print('Geg'.find('G'))  # 대문자 G 를 찾기  다르단 점 !
print('Geg'.find('g'))  # 소문자 g 를 찾기

a = input('첫번쨰 숫자: ')
b = input('두번째 숫자: ')
print('{} + {} = {}'.format(a, b, int(a)+int(b)))