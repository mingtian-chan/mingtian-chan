a= int(input())
b= int(input())
print(a*(b%10))  # 첫째자리랑 곱하도록
print(a*((b//10)%10))  # 둘째자리랑 곱하도록
print(a*(b//100))  # 셋째자리랑 곱하도록
print(a*b)