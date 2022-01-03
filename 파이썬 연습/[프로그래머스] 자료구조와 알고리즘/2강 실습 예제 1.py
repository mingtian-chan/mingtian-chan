def solution(L, x):
    if L[-1] < x:
        L.append(x)
        return L
    for i in L:
        if x < i:
            L.insert(L.index(i), x)
            break
    return L

print(solution([20, 37, 58, 72, 91], 65))