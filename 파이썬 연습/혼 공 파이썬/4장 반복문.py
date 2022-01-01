for i in range(5):
    pass
for i in range(0, 5):
    pass

for i in range(0,10,3):
    pass

# range 마지막 숫자는 들어가지 않음.

key_list = ["name", 'hp', 'mp', 'level']
value_list = ['기사', 200, 30, 5]
character = {}
for i in range(4):
    character[key_list[i]] = value_list[i]

print(character)

counter= 0
for character in '안녕하세요': # 반복문의 ilterable이 str 타입이면, 글자로 반복하게되는데, 이때 무조건 글자가 들어갈 필요는 없음
    # print('-',character)
    counter += 1
    print(i)