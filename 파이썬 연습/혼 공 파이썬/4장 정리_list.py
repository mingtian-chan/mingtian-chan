# 리스트와 반복문
# list = 대괄호 사이에  element를 집어넣어서 만듬, 인덱싱- 0부터 시작
list_a = [1,2,3,4,5,6]
print(id(list_a))
list_a[0] = '변경'
print(id(list_a))  # 리스트의 요소를 바꾸더라도 리스트의 id는 바뀌지 않는다. 메모리 위치는 바뀌지 않는다
print(list_a)  # 리스트의 요소를 쉽게 바꿀 수 있다.
list_a.append(7)
print(id(list_a))
print(list_a)  # 요소를 append 해도 리스트가 저장된 위치는 변하지 않는다.

# 파이썬 메모리 관련 copy deepcopy 참조 할 부분 : https://goodthings4me.tistory.com/81

print(list_a[0][1])  # 결괏값 : 경 , 왜 why? 리스트의 첫번째 요소의 1번 인덱스를 프린트했으니까 - 리스트 접근 연산자를 이중으로 사용
lst_lst = [[1, 2, 3, 4], [5, 5, 6, 7, 8], ['a', 'b', 'c', 'd', 'd'],['abcd', 'efgh']]
print(lst_lst[2][2])  # 결괏값 : c 리스트가 두개인 경우에도 쓸 수 있음
print(lst_lst[3][0][2])  # 결괏값 : c 큰 리스트에서 요소 리스트의 원소에서 인덱싱을 할 경우에 사용

# 리스트의 값을 변경하는 방법!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!11
# 1. lst[원하는 위치] = 원하는 값   / 으로 인덱싱해서 직접 바꾸어 준다.

# 2. enumerate 와 for 을 이용해서 리스트 내 모든 원소 바꾸기
my_list=[5,10,7,5,6,8,5,15]
print('바뀌기 전 :',my_list)
for index, value in enumerate(my_list):  # for enumerate 이용하면 리스트에 있는 모든 원소를 바꾸기 좋음
    #  enumerate 함수 참조 : https: // wikidocs.net / 20792
    if value == 5:
      my_list[index] = 9

print('바뀐 후 :',my_list)

# 리스트에 값을 추가해주는 방법

# 1. 리스트를 슬라이싱해서 중간에 원하는 값을 넣는 방법
lst = [1,2,3,4,5,6]
print(id(lst))
lst = lst[:4] + [3] + lst[5:]  # 이 경우에는 리스트 메모리 저장공간이 바뀜
print(id(lst))
print(lst)

# 2. insert 함수 이용
lst.insert(0,5)  # 리스트.insert(넣고싶은 위치 인덱스, 넣고싶은 요소)
print(lst)
print(id(lst))  # 이 경우 리스트 메모리 저장공간 바뀌지 않음


# 3. extend 함수이용
lst.extend([1,2,3])  # 매개변수로 리스트를 사용하는데, 원래있던 리스트에서 새로운 리스트 요소를 모두 추가해해줌
print(lst)
print(id(lst))  # insert 를 여러 번 실행한 효과를 내준다. 저장공간 바뀌지 않음

# 리스트에 내용을 지우는 방법

# 1. del 리스트명[인덱스]
del lst[1]
print(lst)  # 리스트 인덱스 1번을 지움
print(id(lst))  # 저장공간 바뀌지 않음

del lst[1:4]
print(lst)  # 한번에 여러 개 지울 수 있음
print(id(lst))  # 저장공간 안바뀜

# 2. pop() 함수  _ 리스트명.pop[인덱스]
lst.pop(0)
print(lst)
print(id(lst))  # 저장공간 바뀌지 않음

# 3. remove() 함수  리스트.remove(지우고싶은 값)
lst.remove(3)
print(lst)  # 제일 왼쪽에 있는 값을 지움

# 4. clear() 함수  리스트.clear()
lst.clear()
print(lst)  # 싹 다 지움
print(id(lst))


