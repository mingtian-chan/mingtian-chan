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

for key in character:
    if type(character[key]) is str or int:
        print(f'{key} : {character[key]}')
    elif type(character[key]) is dict:
        for item_key in character[key]:
            print(item_key,':', character[key][item_key])
    elif type(character[key]) is list:
        for skill in character[key]:
            print(key, ":", skill)

# if type(character[key]) is str or int:
# if type(character[key]) is str or type(character[key]) is int:
# 이 두 문장의 차이점 : is str 까진 판별인데 위에건 int 로 그냥 아무조건 없어서 true 로 출력
# is str or is int 로 해야 조건문 or 조건문 으로 활용이 됨