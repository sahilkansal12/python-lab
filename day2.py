Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ls
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    ls
NameError: name 'ls' is not defined
>>> 01925
SyntaxError: invalid token
>>> x="\0958\u0959\u095A"
>>> print(x)
 958ख़ग़
>>>  x="\u0958\u0959\u095A"
 
SyntaxError: unexpected indent
>>> x="\u0958\u0959\u095A"
>>> print(x)
क़ख़ग़
>>> x="\u0958\u0959\u095A" print(x)
SyntaxError: invalid syntax
>>> import time
>>> st=time.time()
>>> for i in range(100000)
SyntaxError: invalid syntax
>>> for i in range(100000):
	z=i*i
	end for
	
SyntaxError: invalid syntax
>>> for i in range(100000):
	z=i*i
	end

	
Traceback (most recent call last):
  File "<pyshell#17>", line 3, in <module>
    end
NameError: name 'end' is not defined
>>> time.time()
1567918741.0765524
>>> datetime.date(year-2019, month=9, day=8)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    datetime.date(year-2019, month=9, day=8)
NameError: name 'datetime' is not defined
>>> import datetime
>>> datetime.date(year-2019, month=9, day=8)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    datetime.date(year-2019, month=9, day=8)
NameError: name 'year' is not defined
>>> datetime.date?
SyntaxError: invalid syntax
>>> datetime.date(year-2019, month=9, day=8, hour=10, minute =20, second=12)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    datetime.date(year-2019, month=9, day=8, hour=10, minute =20, second=12)
NameError: name 'year' is not defined
>>> datetime.date(year=2019, month=9, day=8hour=10, minute =20, second=12)
SyntaxError: invalid syntax
>>> datetime.date(year=2019, month=9, day=8, hour=10, minute =20, second=12)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    datetime.date(year=2019, month=9, day=8, hour=10, minute =20, second=12)
TypeError: function takes at most 3 keyword arguments (6 given)
>>> import datetime
>>> d1==datetime.date(year=2019, month=9, day =8)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    d1==datetime.date(year=2019, month=9, day =8)
NameError: name 'd1' is not defined
>>> d1=datetime.date(year=2019, month=9, day =8)
>>> d2=datetime.date(year=2019, month=10, day =15)
>>> d2-d1
datetime.timedelta(days=37)
>>> t1=datetime.datetime(year=2019, month=9, day=8, hour=10, minute =20, second=12)
>>> t2=atetime.datetime(year=2019, month=10, day=10, hour=10, minute =20, second=12)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    t2=atetime.datetime(year=2019, month=10, day=10, hour=10, minute =20, second=12)
NameError: name 'atetime' is not defined
>>> t2=datetime.datetime(year=2019, month=10, day=10, hour=10, minute =20, second=12)
>>> td=datetime.timedelta(days=1, hours=10)
>>> t1
datetime.datetime(2019, 9, 8, 10, 20, 12)
+
>>> t1+td
datetime.datetime(2019, 9, 9, 20, 20, 12)
>>> t1
datetime.datetime(2019, 9, 8, 10, 20, 12)
>>> t1+td
datetime.datetime(2019, 9, 9, 20, 20, 12)
>>> t1.strftime("%d/%m/%y")
'08/09/19'
>>> t1.strftime("%d/%m/%y %H:%M:%S")
'08/09/19 10:20:12'
>>> datetime,strptime("%m/%d/%Y %H:%M: %S")
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    datetime,strptime("%m/%d/%Y %H:%M: %S")
NameError: name 'strptime' is not defined
>>> datetime.strptime("%m/%d/%Y %H:%M: %S")
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    datetime.strptime("%m/%d/%Y %H:%M: %S")
AttributeError: module 'datetime' has no attribute 'strptime'
>>> datetime.datetime.strptime("%m/%d/%Y %H:%M: %S")
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    datetime.datetime.strptime("%m/%d/%Y %H:%M: %S")
TypeError: strptime() takes exactly 2 arguments (1 given)
>>> 
