# 1~100까지의 합에서 3의 배수는 제외(continue문을 사용)
hap, i = 0, 0

for i in range(1, 101, 1):
    if i % 3 == 0:
        continue  
    hap = hap + i

print("1~100까지의 합에서 3의 배수는 제외(continue문을 사용) %d" % hap)
