import numpy as np


def solution(img):
    answer = []
    for a in img:
        temp_list = []
        for b in a:
            temp_num = 0
            for c in range(len(b)):
                if c == 0:
                    temp_num = temp_num + (b[c] * 0.3)
                elif c == 1:
                    temp_num = temp_num + (b[c] * 0.5)
                else:
                    temp_num = temp_num + (b[c] * 0.2)
            temp_list.append(round(temp_num, 2))
        answer.append(temp_list)
    answer = np.array(answer)
    return answer


img =np.random.randint(0,256,size= (10,10,3))

print(solution(img))