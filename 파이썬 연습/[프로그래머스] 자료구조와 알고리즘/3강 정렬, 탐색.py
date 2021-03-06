# 정렬의 방법

# sorted(L,key = lambda x : x['score'],reverse = True)
# L.sort(key = lambda x : x['Name']

# 선형탐색 : 길이가 길어질수록 비례해서 시간이 들음 : O(n)의 시간이 든다고 볼 수있지

# 이진탐색 : 리스트의 원소가 일단 크기순으로 정리되어있어야 됨 : O(log n)

def solution(L, x):
    lower = 0
    upper = len(L) -1
    idx = -1
    while lower <= upper:
        middle = int((lower+upper)//2)
        if x == L[middle]:
            idx = middle
            break
        elif x > L[middle]:
            lower = middle+1
        else:
            upper = middle-1


print(solution([2, 3, 5, 6, 9, 11, 15],6))