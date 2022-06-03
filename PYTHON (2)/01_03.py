'''
for i in range(0,3,1):
    print("%d : 안녕하세요" % i)

i=0
while i<3:
    print("%d : 안녕하세요" % i)
    i =i+1
'''
'''
시작값
while 끝값:
    실행문장
    증가값
    '''
# 1에서 10까지합(while문으로)
'''
hap = 0
i=0

i = 1
while i<11:
    hap = hap + i
    i = i +1
    
print("1에서 10까지합(while문으로) : %d" % hap)
'''
'''
while(1):
    print("ㅋ", end = "")
'''

hap = 0
a, b = 0, 0

while True:
    a = int(input("더할 첫 번째 수를 입력하세요 : "))
    b = int(input("더할 두 번째 수를 입력하세요 : "))
    hap = a+b
    print("%d + %d = %d" % (a, b, a+b))
    
