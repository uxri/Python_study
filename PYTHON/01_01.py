'''
print("안녕하세요")
print("안녕하세요")
print("안녕하세요")
'''
'''
for i in range(0,3,1):
    print("안녕하세요")

for i in range(0,3,1):
    print("%d : 안녕하세요" % i)

for i in range(2,-1,-1):
    print("%d : 안녕하세요" % i)
'''
'''
for 변수 in range(시작값,끝값+1,증가값):
    실행문장
'''
'''
# 1~5까지 숫자들을 차례로 출력
for i in range(1, 6,1):
    print("%d" % i)

for i in range(1, 6,1):
    print("%d" % i,end="  ")
'''
'''
hap = 1+2+3+4+5+6+7+8+9+10
print("1에서 10까지 합: %d" % hap)
'''
'''
hap = 0 #hap 초기화

for i in range(1, 11, 1):
    hap = hap + i
    
print("1에서 10까지 합: %d" % hap)
'''
'''
hap = 0 

for i in range(1, 101, 1):
    hap = hap + i
    print("1에서 100까지  합: %d" % hap)
'''
'''
hap = 0 

for i in range(51, 101, 2):
    hap = hap + i
    print("50에서 100까지 홀수의 합: %d" % hap)
'''
'''
hap = 0
num = 0

num = int(input("값을 입력하세요 : "))

for i in range(1, num+1, 1):
    hap = hap + i
print("1에서 %d까지 합: %d" % (num,hap))
'''
i = 0
dan = 0

dan = int(input("단을 입력하세요"))

for i in range(1, 10,1):
    print("%d  X %d = %2d" % (dan, i, dan*i))
    


