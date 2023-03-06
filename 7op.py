#!/usr/bin/python3
a = 21
b = 10
print('a=', a)
print('b=', b)

c = a+b
print(c)
c = a-b
print(c)
c = a*b
print(c)
c = a/b
print(c)
c = a%b
print(c)
c = a//b
print(c)
# -----------------------------------------------------------------------------

a = 2
b = 3
c = a**b
print(c)

a = 21
b = 10
if a == b:
    print('a=b')
else:
    print('a!=b')

if a != b:
    print('a!=b')
else:
    print('a=b')

if a < b:
    print('a<b')
else:
    print('a>=b')

if a > b:
    print('a>b')
else:
    print('a<=b')

a = 5
b = 20
if a <= b:
    print('a<=b')
else:
    print('a>b')

if b >= a:
    print('b>=a')
else:
    print('b<a')
# -----------------------------------------------------------------------------
a = 21
b = 10
c = a+b
print(c)

c += a
print(c)
c *= a
print(c)
c /=a
print(c)
c = 2
c %= a
print(c)
c **= a
print(c)
c //= a
print(c)
e = [1,2,3,4,5,6,7,8,9,10,11]
if( n := len(e)) > 10:
    print(f'list is to long ({n})')

# -----------------------------------------------------------------------------
# a = 60
a = 0b00111100
# b = 13
b = 0b00001101

c = a&b
print(c)
c = a|b
print(c)
c = a^b
print(c)
c = ~a
print(c)
c = a<<2
print(c)
c = a>>2
print(c)
# -----------------------------------------------------------------------------
a = 10
b = 20
if a and b:
    print('a and b 都為true')
else:
    print('a and b 有一個不為true')

if a or b:
    print('a and b 都為true, 或只有一個為true')
else:
    prin('a and b 都不為true')

a = 0
if a and b:
    print('a and b 都為true')
else:
    print('a and b 有一個不為true')

if a or b:
    print('a and b 都為true, 或只有一個為true')
else:
    prin('a and b 都不為true')

if not(a and b):
    print('a and b 都為false, 或只有一個為false')
else:
    print('a and b 都為true')

# -----------------------------------------------------------------------------
a = 10
b = 20
list = [1, 2, 3, 4, 5]
if (a in list):
    print('a in list')
else:
    print('a not in list')

if (b not in list):
    print('b not in list')
else:
    print('b in list')

a = 2
if (a in list):
    print('a in list')
else:
    print('a not in list')

# -----------------------------------------------------------------------------
a = 20
b = 20
if a is b:
    print('a and b equ')
else:
    print('a and b not equ')

if id(a) == id(b):
    print('a and b equ')
else:
    print('a and b not equ')

b = 30
if a is b:
    print('a and b equ')
else:
    print('a and b not equ')

if a is not b:
    print('a and b not equ')
else:
    print('a and b equ')

a = [1,2,3]
b = a
print(b is a)
print(b == a)
b = a[:]
print(b is a)
print(b == a)
# -----------------------------------------------------------------------------
a = 20
b = 10
c = 15
d = 5
e = (a+b)*c /d
print(e)
e = ((a+b)*c)/d
print(e)
e = (a+b)*(c/d)
print(e)
e = a+(b*c)/d
print(e)

x = True
y = False
z = False
if x or y and z:
    print('yes')
else:
    print('no')

# print(1<>2) #error
