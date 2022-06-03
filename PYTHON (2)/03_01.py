Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("%d" % 123)
123
print("%5d" % 123)
  123
print("%05d" % 123)
00123
print("%f" % 123.45)
123.450000
print("%7.1f" % 123.45)
  123.5
print("%7.3f" % 123.45)
123.450
print("%s" %"Python")
Python
print("%10s" %"Python")
    Python
print("\t탭키\t연습")
	탭키	연습
print("글자가 '강조' 되는 효과")
글자가 '강조' 되는 효과
print("글자가 "강조" 되는 효과")
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print('글자가 "강조" 되는 효과')
글자가 "강조" 되는 효과
print("글자가 \"강조\" 되는 효과")
글자가 "강조" 되는 효과
boolVar, intVar, floarVar, strVar = True, 0, 0.0,""
type(tboolVar), type(intVar), type(floarVar), type(strVar)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    type(tboolVar), type(intVar), type(floarVar), type(strVar)
NameError: name 'tboolVar' is not defined. Did you mean: 'boolVar'?
type(boolVar), type(intVar), type(floarVar), type(strVar)
(<class 'bool'>, <class 'int'>, <class 'float'>, <class 'str'>)
boolVar, intVar, floarVar, strVar = False, 100, 123.45,"안녕"
boolVar, intVar, floarVar, strVar
(False, 100, 123.45, '안녕')
a=100
a
100
10=100
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
가=100
가
100
ㄱ=100
ㄱ
100
a = 100
a ==100
True
a ==200
False
s1 = "100"
s1
'100'
s2 = "100.123"
s2
'100.123'
int(s1)
100
float(s2)
100.123
s3 = "9999"
s3+1
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    s3+1
TypeError: can only concatenate str (not "int") to str
s3+"1"
'99991'
int(s3)+1
10000
a=100
a+'1'
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a+'1'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
a+1
101
str(a)+'1'
'1001'
b = 100.123
str(b)+'1'
'100.1231'
b+1
101.123
a=10
a = a+5
a
15
a=10
a +=5
a
15
a -=5; a
10
a *=5; a
50
a /=5; a
10.0
a //=5; a
2.0
a %/=5; a
SyntaxError: invalid syntax
a %=5; a
2.0
a **=5; a
32.0
