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
