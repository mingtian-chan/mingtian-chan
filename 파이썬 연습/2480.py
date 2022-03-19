lst = input().split()

lst_set = set(lst)
lst = list(lst_set)
lst.sort(reverse=True)

if len(lst) == 1:
    print(10000+int(lst[0])*1000)
elif len(lst) ==2:
    print(1000+int(lst[0])*100)
else:
    print(int(lst[0])*100)



# 2. 이렇게 했을 때 틀렸던 점 : lst == 2 일 떄 같은 애가 출력되는게 아니라 큰 애가 출력된거!
# lst = input().split()
#
# lst_set = set(lst)
# lst = list(lst_set)
# lst.sort(reverse= True)
#
# if len(lst) == 1:
#     print(10000+int(lst[0])*1000)
# elif len(lst) ==2:
#     print(1000+int(lst[0])*100)
# else:
#     print(int(lst[0])*100)

# 1. 이렇게 했을 때 틀린 점 : set 는 순서를 가지지 않아서 lst_set[0]은 존재 X
# lst = input().split()
# lst.sort(reverse= True)
# lst_set = set(lst)
#
#
# if len(lst_set) == 1:
#     print(10000+int(lst_set[0])*1000)
# elif len(lst_set) ==2:
#     print(1000+int(lst_set[0])*100)
# else:
#     print(int(lst_set[0])*100)