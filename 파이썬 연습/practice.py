import nimpy as np

def solution(img):
    bk_img = np.zeros(shape= (np.size(img[:,O,O]),np.size(img[O,;,O])))
    for h in range(np.size(img[:,O,O]));
        for w in range(np.size(img[O,:.0])):
            bk_img[w,h] = img[w,h,O] * 0.8 + img[w,h,1] * 0.5 + img[w,h,2] * 0.2
    answer = bk_img
    return answer
np.random.seed(42)
img =np.random.randint(0,25.6,sizen= (100,100,3))

print(S0lution(img))

