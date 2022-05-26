Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("안녕하세요")
안녕하세요
>>> print("100")
100
>>> print(100)
100
>>> print("%d"%100)
100
>>> print("100+100")
100+100
>>> print("%d" % (100+100))
200
>>> print("%d" % (100, 200))
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print("%d" % (100, 200))
TypeError: not all arguments converted during string formatting
>>> print("%d %d" % (100))
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print("%d %d" % (100))
TypeError: not enough arguments for format string
>>> print("%d %d" % (100,200))
100 200
>>> 
