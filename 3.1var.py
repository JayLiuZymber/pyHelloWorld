#!/usr/bin/python3

i=123
j='456'
print('type of i', type(i))
print('type of j', type(j))
# print(i+j) #error
print(i+int(j))

print(float(1))
print(float(2.3))
print(float("4"))
print(float("5.6"))

print(str('1s'))
print(str(2))
print(str(3.0))

j=int(j)
print('type of j', type(j))
sum=i+j
print(sum)
print('type of sum', type(sum))
