'''
a = 100
b = 50

result = a + b
print('%d + %d = %d ' % (a, b, result))
result = a - b
print('%d - %d = %d ' % (a, b, result))
result = a * b
print('%d - %d = %d ' % (a, b, result))
result = a / b
print('%d / %d = %d ' % (a, b, result))
'''
'''
100 + 50 = 150
100 - 50 = 50
100 * 50 = 5000
100 / 50 = 2
'''
a = int(input("첫번째 숫자를 입력하세요:"))
b = int(input("두번째 숫자를 입력하세요:"))

result = a + b
print(a, "+", b, "=", result)
result = a - b
print(a, "-", b, "=", result)
result = a * b
print(a, "*", b, "=", result)
result = a / b
print(a, "/", b, "=", result)
