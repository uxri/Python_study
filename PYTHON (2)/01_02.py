'''
for i in range(0,3,1):
    print("안녕 : i 의 값 %d" % i)

for k in range(0,2,1):
    print("안녕 : k 의 값 %d" % k)
'''
'''
for i in range(0,3,1):
    for k in range(0,2,1):
        print("안녕 : i 의 값 : %d         k 의 값 : %d" % (i,k))
'''
'''
for i in range(2, 10, 1): # i는 단
    for k in range(1, 10, 1): # k는 각단에 1~9까지를 뒤에서 곱하는 수
        print("%d X %d = %2d" % (i, k, i*k))
    print("") # 한줄 띄우는 것
'''
for i in range(1, 10, 1): # i 1~9까지를 뒤에서 곱하는 수
    for k in range(2, 10, 1): # k가 단
        print("%d X %d = %3d" % (k, i, i*k),end="   ")
    print("")  # 줄바꿈

