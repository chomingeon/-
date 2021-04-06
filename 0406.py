Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  4 2021, 13:27:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Users/User/AppData/Local/Programs/Python/Python39/1.py
Traceback (most recent call last):
  File "C:/Users/User/AppData/Local/Programs/Python/Python39/1.py", line 1, in <module>
    a.b=input
NameError: name 'a' is not defined
>>> 
= RESTART: C:/Users/User/AppData/Local/Programs/Python/Python39/1.py
Traceback (most recent call last):
  File "C:/Users/User/AppData/Local/Programs/Python/Python39/1.py", line 1, in <module>
    a,b = input
TypeError: cannot unpack non-iterable builtin_function_or_method object
>>> 
= RESTART: C:/Users/User/AppData/Local/Programs/Python/Python39/1.py
Traceback (most recent call last):
  File "C:/Users/User/AppData/Local/Programs/Python/Python39/1.py", line 1, in <module>
    a,b = input
TypeError: cannot unpack non-iterable builtin_function_or_method object
>>> 
= RESTART: C:/Users/User/AppData/Local/Programs/Python/Python39/1.py
3
Traceback (most recent call last):
  File "C:/Users/User/AppData/Local/Programs/Python/Python39/1.py", line 1, in <module>
    a,b = input()
ValueError: not enough values to unpack (expected 2, got 1)
>>> File "C:/Users/User/AppData/Local/Programs/Python/Python39/1.py", line 1, in <module>Tom
SyntaxError: invalid syntax
>>> 
= RESTART: C:/Users/User/AppData/Local/Programs/Python/Python39/1.py

= RESTART: C:/Users/User/AppData/Local/Programs/Python/Python39/1.py

= RESTART: C:/Users/User/AppData/Local/Programs/Python/Python39/1.py
name age :Tom 13
Traceback (most recent call last):
  File "C:/Users/User/AppData/Local/Programs/Python/Python39/1.py", line 1, in <module>
    a,b = input("name age :")
ValueError: too many values to unpack (expected 2)
>>> 
= RESTART: C:/Users/User/AppData/Local/Programs/Python/Python39/1.py
name age :Tom 13
Tom is 13 years old
>>> 
= RESTART: C:/Users/User/AppData/Local/Programs/Python/Python39/1.py
a b 입력: a
Traceback (most recent call last):
  File "C:/Users/User/AppData/Local/Programs/Python/Python39/1.py", line 5, in <module>
    a,b = map(int, input('a b 입력:').split())
ValueError: invalid literal for int() with base 10: 'a'
>>> 
= RESTART: C:/Users/User/AppData/Local/Programs/Python/Python39/1.py
a b 입력:a b
Traceback (most recent call last):
  File "C:/Users/User/AppData/Local/Programs/Python/Python39/1.py", line 5, in <module>
    a,b = map(int, input('a b 입력:').split())
ValueError: invalid literal for int() with base 10: 'a'
>>> 

= RESTART: C:/Users/User/AppData/Local/Programs/Python/Python39/1.py
>>> 
a b 입력:1 2
1 = 2 = 0.500000
>>> 
= RESTART: C:/Users/User/AppData/Local/Programs/Python/Python39/1.py
a b 입력:10 3
10 / 3 = 3.333333
>>> 
= RESTART: C:/Users/User/AppData/Local/Programs/Python/Python39/1.py
a b 입력:10 3
10 / 3 = 3.333
>>> 
= RESTART: C:/Users/User/AppData/Local/Programs/Python/Python39/1.py
name age :Tom 13
Tom is 13 years old
a b 입력:
= RESTART: C:/Users/User/AppData/Local/Programs/Python/Python39/1.py
{:>8} 3
x{:>6} 12
------------
Traceback (most recent call last):
  File "C:/Users/User/AppData/Local/Programs/Python/Python39/1.py", line 12, in <module>
    print('{:>7)'.format(a*b))
ValueError: unmatched '{' in format spec
>>> 
= RESTART: C:/Users/User/AppData/Local/Programs/Python/Python39/1.py
{:>8} 3
x{:>6} 12
------------
     36
>>> 
= RESTART: C:/Users/User/AppData/Local/Programs/Python/Python39/1.py
       3
x    12
------------
     36
>>> 
= RESTART: C:/Users/User/AppData/Local/Programs/Python/Python39/1.py
       3
x     12
------------
     36
>>> 
= RESTART: C:/Users/User/AppData/Local/Programs/Python/Python39/1.py
       3
x     12
------------
      36
>>> 