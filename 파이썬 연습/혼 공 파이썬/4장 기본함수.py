# enumerate 함수
a = [ 1, 2, 3]
print(a)
print(enumerate(a)) # enumerate 객체가 만들어짐.
print(list(enumerate(a)))
for i, value in enumerate(a):
    print("{}번쨰 요소는 {}입니다.".format(i, value))

# items() 함수 (dictionary 의)
example_dict = {
    '키A' : 'valA',
    'keyB' : 'valB',
    'keyC' : 'valC'

}

for key,val in example_dict.items():
    print(f'dictionary[{key}] : {val}')

# 리스트 내포
# 리스트 이름 = [표현식(fruit) for 반복자(i) in 반복할 수 있는 것(리스트) if 조건문]

# 문자열 연결하기
test = (
    '이렇게'
    '입력해도'
    '하나의 문자열로 연결되어 생성됩니다'
)

print("test",test)
print("type(test)",type(test))


