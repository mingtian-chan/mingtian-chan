# 딕셔너리 : {키 : 값} 으로 선언
dict_a = {
    'key_1': 'man',
    'key_2': 'woman',

}
print(dict_a['key_1'])  # 선언시에는 중괄호, 불러올 때는 대괄호로 불러옴

# 추가 : 딕셔너리['키 값'] = '밸류 값'
# 제거 : del 딕셔너리['키 값']

# dic 찾기 : in 키워드 키 in 딕셔너리
# or get() 함수 : get('키 값') 하면 value 값 나옴 but 없는 값을 넣으면 value는 none

for key in dict_a:
    print(f'{key}:{dict_a[key]}')

numbers = [1,2,6,4,8,9,7,6,1,3,4,5,8,4,6,8,7,1,3,4,6,3,4,8,7,9]
counter = {}
for number in numbers:
    if number in counter:
        counter[number] += 1
    else:
        counter[number] = 1

print(counter)
sorted_counter = sorted(counter.items())
print(sorted_counter)
print(dict(sorted_counter)) # dict 이용해서 sort 시킴

character = {
    'name': '기사',
    'level': 12,
    'items': {
        'sword' : '불꽃의 검',
        'armor' : '풀플레이트',
    },
    'skill':['베기','세게 베기','아주 세게 베기']
}
for key in character:
    if type(character[key]) is str or type(character[key]) is int:
        print(f'{key} : {character[key]}')
    elif type(character[key]) is dict:
        for item_key in character[key]:
            print(item_key,':', character[key][item_key])
    elif type(character[key]) is list:
        for skill in character[key]:
            print(key, ":", skill)

            #왜 답지랑 출력이 다르지 ..
    # if type(character[key]) is str or int:
    # if type(character[key]) is str or type(character[key]) is int:
    # 이 두 문장의 차이점 : is str 까진 판별인데 위에건 int 로 그냥 아무조건 없어서 true 로 출력
    # is str or is int 로 해야 조건문 or 조건문 으로 활용이 됨



