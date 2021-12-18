a, b = (map(int, input().split()))


print(a)
print(b)
print(type(a))
print(a+b)

# 막힌 이유

# 1. map 함수를 몰랐음

#  map 함수란 ?
# 기본형 : map(함수, 반복가능한 자료형)
# 반복가능한 자료형에 대해서 계속계속 함수를 진행한다는 뜻!
# 예를들어 map(예를들어 1을 더하는 함수, [1, 2, 3]) 일 경우

#def plus1(a):
#     return a+1

# print(list(map(plus1,[1,2,3])))
# 이때 print(map(~~~)을 하게되면 map 객체가 나오게 됨 즉 원하는 값이 아니죠
# 그래서 원하는 값의 형태로 출력을 바꿔야 함
# 본 문제에선 int 함수를 사용했고, input 을 받은 string 을 split으로 쪼갰고, 쪼갠 원소를 각각 a b 라고 칭한거잖아

# 2. split 함수에 대한 정확한 이해가 없었음!
# 3. input()함수도 제대로 모르고있었음..

# input 함수는 입력받은 값을 string으로 받고있음
# input().split()는 입력받은 값을 스페이스 기준으로 나눠서 스트링으로 줌
# 단 각각을 받으려면 그 갯수만큼 받는 값이 필요해 예를들어
# a,b,c = input().split() 에서 1 2 3 을 넣어야 한다는 뜻
# a = input().split() 이면 string 을 쪼개서 리스트로 만듬
# 예제
# 입력
#  print(a)
# print(type(a))
# 결과
# ['1', '1', '1']
# <class 'list'>

# 참고 블로그 https://ccamppak.tistory.com/38