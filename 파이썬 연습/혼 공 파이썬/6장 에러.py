# 프로그램 실행 전에 일어나는 오류 : syntax error 구문오류
# 프로그램 실행 후에 일어나는 오류 : exception 예외 , or runtime error 런타임 오류

# 예외처리 : 조건문 , try except 구문 이용  <- 많이 씀

# try except else
# try : 예외가 발생할 가능성이 있는 코드
# except : 예외가 발생했을 때 실행하는 코드
# else : 예외가 발생하지 않았을때 실행하는 코드
# finally : 예외가 발생하든 말든 실행되는 코드

# test() 함수를 선언합니다.
def nottest():
    print("test() 함수의 첫 줄입니다.")
    try:
        print("try 구문이 실행되었습니다.")
        return
        print("try 구문의 return 키워드 뒤입니다.") # 얘는 써지지 않는 코드임
    except:
        print("except 구문이 실행되었습니다.")
    else:
        print("else 구문이 실행되었습니다.")
    finally:
        print("finally 구문이 실행되었습니다.")
    print("test() 함수의 마지막 줄입니다.")

# test() 함수를 호출합니다.
nottest()

# 함수를 선언합니다.
def write_text_file(filename, text):
    # try except 구문을 사용합니다.
    try:
        # 파일을 엽니다.
        file = open(filename, "w",encoding='UTF8')
        # 여러 가지 처리를 수행합니다.

        # 파일에 텍스트를 입력합니다.
        file.write(text)
    except Exception as e:
        print(e)
    finally:
        # 파일을 닫습니다.
        file.close()

# 함수를 호출합니다.
write_text_file("test.txt", "안녕하세요!",)

numbers= [1,2,3,4,5,6,7]
inputint = int(input('값을 입력하세요: '))
try:
    print('-{}는 {}위치에 있습니다'.format(inputint,numbers.index(inputint)))
except:
    print('{}는 리스트에 없습니다'.format(inputint))
print()

print('---정상적으로 종료되었습니다.---')