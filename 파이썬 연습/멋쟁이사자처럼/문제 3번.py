
seq = int(input())
best_grade = input().split()
for i in range(seq-1):
    grade = input().split()
    if int(grade[0]) > int(best_grade[0]):
        best_grade = grade
    elif int(grade[0]) == int(best_grade[0]):
        if int(grade[1]) < int(best_grade[1]):
            best_grade = grade
print(int(best_grade[0]), int(best_grade[1]))








#
# def sol(n):
#
#     lst = input().split('\n')
#     eng, math = (0,0)
#     for n in range(int(lst[0])):
#         if eng < lst[n+1][0]:
#             eng,math = lst[n+1][0], lst[n+1][1]
#
#         if eng == lst[n+1][0]:
#             if math < lst[n+1][1]:
#                 math = lst[n+1][1]
#
#     return (eng,math)
#
