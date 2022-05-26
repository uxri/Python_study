#for i in range(1,100,1):
#    print("for문을 %d문 실행" %i)
#    break


#hap = 0
#a,b=0,0


#while True:
#    a=int(input("더할 첫번째 수를 입력하세요"))
#    if a==0:
#        break
#    b=int(input("더할 두번째 수를 입력하세요"))
#    print("%d + %d = %d" %(a, b, a+b))

#    print("0을 입력해서 반복문을 탈출")



#누적합이 1000이상이 되는 시점 알기
hap,i = 0,0
for i in range(1,101):
    hap = hap+i

    if hap>=1000:
        break

print("1~100까지의 합에서 누적합이 1000이상이 되는 시점 : %d" %i)

#1~100까지의 합에서 3의 배수는 제외(continue 사용)
#hap,i = 0,0

#for i in range(1,101,1):
#    if i%3==0:
#        continue
#    hap=hap+i

#print("1~100까지의 합에서 3의 배수는 제외 : %d" %hap)
