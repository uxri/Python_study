#구구단 행별로 정렬 (단 별로 가로)

for k in range(2,10,1):
    for i in range(1,10,1):
        print("%d X %d = %2d" % (k,i,i*k), end=("   "))
    print("")
