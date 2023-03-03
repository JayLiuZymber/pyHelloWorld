#!/usr/bin/python3
#Number
#int, float, bool, complex
print('#int type')
a, b, c, d=20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))

a=111
print(isinstance(a, int)) #true

class A:
    pass
class B(A):
    pass
print(isinstance(A(), A))   #true
print(type(A()) == A)       #true
print(isinstance(B(), A))   #true
print(type(B()) == A)       #false

print('bool type')
print(issubclass(bool, int))#true
print(True==1)  #true
print(False==0) #true
print(True+1)   #2
print(False+1)  #1
print(1 is True)    #false
print(0 is False)   #false

var1 = 1
var2 = 10
print("var1=", var1)
print('var2=', var2)
#del var1
del var1, var2

print('#float type')
print(3*7)
print(2/4)
print(2//4)
print(17%3)
print(2**5)

a, b=1, 2
print(a, b)
print(3e+26j)

print('#string type')
word = 'Python'
print(word[0], word[5])
print(word[-1], word[-6])

print('#list type')
list = ['abcd', 786, 2.23, 'python', 70.2]
tinylist = [123, 'runood']
print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(tinylist *2)
print(list + tinylist)

a = [1, 2, 3, 4, 5, 6]
a[0] = 9
a[2:5] = [13, 14, 15]
print(a)
a[2:5] = [] #del [2],[3],[4]
print(a)
a[2:5] = [23, 24, 25, 26, 27] #褫眕崝樓
print(a)
print(a[1:4:2])

def reverWord(inputWord):
    input = inputWord.split(' ')
    input = input[-1::-1]

    output = ' '.join(input)
    return output

if __name__=="__main__":
    input = 'I link python'
    reinput = reverWord(input)
    print(reinput)

print('#tuple type')
tuple = ('abcd', 786, 2.23, 'python', 70.2)
tinytuple = (123, 'python')
print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tinytuple *2)
print(tuple + tinytuple)

b=(1, 2, 3, 4, 5, 6)
print(b[0])
print(b[1:5])
#b[0] = 11 #error

tup1=()
tup2=(20,)
print(tup1)
print(tup2)

print('#set type')
s = {'Google', 'Taobao', 'Python', 'Facebook', 'Zhihu', 'Baidu'}
print(s)

if 'Python' in s:
    print('Python in set')
else:
    print('Python not in set')

a = set('abcdbcd')
b = set('xyabxyz')
print(a)
print(a - b)
print(b - a)
print(a | b)
print(a & b)
print( a ^ b)

print('#dictionary type')
dict1 = {}
dict1['one'] = "No.1"
dict1[2] = "No.2"
tinydict = {'name':'python', 'code':1, 'site':'www.python.org'}
print(dict1['one'])
print(dict1[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())

dict2 = {}
dict2 = dict([ ('Python', 1), ('Google', 2), ('Youtube', 3)]) #建構函式
print(dict2)

dict3 = {x: x**2 for x in (2, 4, 6)}
print(dict3)

dict4 = {}
dict4 = dict(Python=1, Google=2, Youtube=3)
print(dict4)

x=0x41
print(chr(x))
print(ord('A'))
print(hex(x))
print(oct(x))
