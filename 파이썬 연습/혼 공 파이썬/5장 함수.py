# 1. 매개변수
# 함수 ( ) 여기 괄호 안에 들어가는 내용이 매개변수 임
# callme(value, n) 일때 2개 말고 1개나 3개이상이 들어가면 TypeError 일어남
# 가변 매개변수  : 가변매개변수 뒤에는 하나만 쓸 수 있음. 가변 매개변수 뒤에는 일반 매개변수가 올 수 없음
# 기본 매개변수  : 가변 매개변수 뒤에 올 수 있고, 기본으로 지정되어있는 값을 나타냄
# 키워드 매개변수 : a b c 에서 b = 10 c = 100 이런식으로 특정 값 지정해주는 것

# 함수 메모화
dictionary = {
    1: 1,
    2: 1
}

def fibonacci(n):
    if n in dictionary:
        return dictionary[n]
    else:
        output = fibonacci(n-1) + fibonacci(n-2)
        dictionary[n] = output
        return output


def fibonacci(n):
    if n in dictionary:
        # 조기 리턴 방식 # 메모되어 있을 시, 메모된 값 리턴
        return dictionary[n]
    # 메모되어있지 않을 시 값을 구함
    output = fibonacci(n-1) + fibonacci(n-2)
    dictionary[n] = output
    return output

# 마무리 문제
def flatten(data):
    output = []
    for datum in data:
        if type(datum) == list:
            output += flatten(datum)  # 이부분이 재귀적인 부분임 datum을 flatten 함수로 다시 불러왔으니까
        else:
            output.append(datum)
    return output

example = [[1,2,3], [4,[5,6]], 7,[8,9]]
print('원본:', example)
print('변환:', flatten(example))

