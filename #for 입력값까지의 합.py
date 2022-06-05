#입력한 값까지 합 구하기
hap = 0
num = 0
num = int(input("값을 입력하세요 : "))
for i in range(1, num+1, 1):
    hap = hap + i
print("1에서 %d까지 합: %d" % (num,hap))
