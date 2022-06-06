hap = 0
a, b = 0, 0
while True :
    a = int(input("더할 첫번째 수를 입력하세요:"))
    if a==0:
        break
    b = int(input("더할 두번째 수를 입력하세요:"))
    print(" %d + %d = %d" %(a, b, a+b))
    print("반복문 탈출을 원할 시 첫번째 수에 0을 입력하세")
