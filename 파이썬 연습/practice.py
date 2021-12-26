numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for number in numbers:
    if number % 2 == 0:
        print(f'{number} 는 홀수입니다')
    else:
        print(f'{number}는 짝수입니다.')

for number in numbers:
    print(f'{number}는 {len(str(number))} 자릿 수 입니다.')

list_of_list = [[1, 2, 3], [4, 5, 6, 7], [8, 9]]

for lst in list_of_list:
    for element in lst:
        print(element)

lst_5 = [1,2,3,4,5,6,7,8,9]
output = [[], [], []]

for number in lst_5:
    output[(number-1) % 3].append(number)

print(output)