'''
a = 99
if a < 100:
    print("100보다 작군요")
'''
'''
a = 200
if a < 100:
    print("100보다 작군요")
    print("거짓이므로 이 문장은  안 보이겠죠?")

print("프로그램 끝")
'''
'''
a = 200
if a < 100:
    print("100보다 작군요")
else:
    print("100보다 크군요")
'''
'''
a = 200
if a < 100:
    print("100보다 작군요")
    print("참이면 이 문장도 보이겠죠")
else:
    print("100보다 크군요")
    print("거짓이면 이 문장도 보이겠죠")
print("프로그램 끝")
'''
#문제 : 입력한 숫자가 짝수인지 홀수인지를 계산하는 프로그램을 완성하시오.
'''
a = int(input("정수를 입력하세요 :"))
if a % 2 ==0:
    print("짝수입니다")
else:
    print("홀수입니다")

#정수를 입력하세요 : 125
#홀수입니다
'''
'''
a = int(input("정수를 입력하세요 :"))
if a % 5==0:
    print("5의 배수입니다")
else:
    print("5의 배수가 아닙니다")
'''
'''
a = int(input("정수를 입력하세요 :"))
if a % 5==0 or a%3==0:
    print("3의 배수 또는 5의 배수입니다")
else:
    print("3의 배수 또는 5의 배수가 아닙니다")
'''
'''
a = int(input("정수를 입력하세요 :"))
if a % 5==0 and a%3==0:
    print("3의 배수 이고 5의 배수입니다")
else:
    print("3의 배수이면서 5의 배수가 아닙니다")
'''
'''
a = 25

if a> 50:
    if a<100:
        print("50보다 크고 100보다 작다.")
    else:
        print("100보다 크다")
else:
    print("50보다 작군요")
'''
'''
score = int(input("점수를 입력하세요 : "))

if score >= 90:
    print("A")
else:
    if score >=80:
        print("B")
    else:
        if score >=70:
            print("C")
        else:
            if score >=60:
                print("D")
            else:
                print("F")
print("학점입니다")
'''
score = int(input("점수를 입력하세요 : "))

if score >= 90:
    print("A")
elif score >=80:
    print("B")
elif score >=70:
    print("C")
elif score >=60:
    print("D")
else:
    print("F")
print("학점입니다")
        
