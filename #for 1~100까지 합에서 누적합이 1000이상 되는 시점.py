# 1~100까지의 합에서 누적합이 1000이 이상이 되는 시점 알기
hap, i = 0, 0
for i in range(1, 101, 1):
    hap = hap + i
    if hap >=1000:
        break
    
print("1~100까지의 합에서 누적합이 1000이 이상이 되는 시점: %d 합은 %d" % (i, hap))
