# def solution(L, x):
#     newL = []
#     for i in L:
#         if i == x:
#             newL.append(L.index(i))
#             L[L.index(i)] = 'new'
#     if len(newL) == 0:
#         answer = [-1]
#     else:
#         answer = newL
# return answer


def solution(L, x):
    answer = []
    for idx, num in enumerate(L):  # enumerate 함수를 이용해서 풀면 더 쉬움
        if num == x:
            answer.append(idx)

    if len(answer) == 0:
        answer.append(-1)

    return answer

print(solution([64, 72, 83, 72, 54], 72))

