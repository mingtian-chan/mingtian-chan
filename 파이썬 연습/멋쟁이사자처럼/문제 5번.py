
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


# 오목 가능한 가짓수 : 가로로 5개x 12345 y n 세로로 5개 x n y 12345
# 계단식 우하단,x 12345 y 12345  계단식 좌하단x 12345 y 54321

def fiverock(rocks):
    for rock in rocks:

