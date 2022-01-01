# map() 과 filter ()

# map(함수, 리스트) 리스트의 각 요소를 함수에 넣어서 만들어진 새로운 값을 리스트로 반환

# filter(함수, 리스트) 리스트를 함수에 넣고 출력된 값이 True 의 경우에 그 요소를 반환

# map()의 반환값은 map 객체, filter()의 반환값 또한 filter 객체

# lambda는 함수 선언 안하고 함수 바로 쓸 수 있게 햊무
# 예시
output_a = map(lambda x: x**2, [1,2,3,4,5])
# 이처럼 함수가 들어가야 할 자리에 람다x : 함수식 하면 더 깔끔하게 만들 수 있다.


numbers = [1,2,3,4,5,6]
print("::".join(map(str,numbers)))  # join은 int는 못 쓴다 str으로 join가능

numbers = list(range(1,10+1))

print('홀수만 추출하기')
print(list(filter(lambda x: x % 2 == 1, numbers)))
print('3이상 7미만 추출하기')
print(list(filter(lambda x: 3 <= x < 7, numbers)))
print('제곱해서 50미만 추출하기')
print(list(filter(lambda x: x**2 < 50, numbers)))

