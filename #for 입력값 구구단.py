#입력값 구구단
dan=0

dan = int(input("단 수를 입력하세요 : "))

for i in range(1,10,1):
    print("%d x %d = %2d" % (dan, i, dan*i))
