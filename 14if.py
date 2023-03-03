#!/usr/bin/python3
#if
i=100
if i: #不等於0的所有值
    print('1)if true')
    print(i)

i=10.2
if i:
    print('11)if true')
    print(i)

i=-5
if i:
    print('12)if true')
    print(i)

j=0
if j:
    print('2)if true')
    print(j)
print('byebye')

age = int(input('輸入你家狗的年齡:'))
# print()
if age <= 0:
    print('逗我玩!')
elif age == 1:
    print('相當於人14歲')
elif age == 2:
    print('相當於人22歲')
elif age > 2:
    human = 22 + (age-2)*5
    print("對應人年齡:", human)

g = 7
ans = -1
print('猜數字')
while g != ans:
    g = int(input('輸入數字:'))
    if g == ans:
        print('答對了')
    elif g < ans:
        print('猜太小')
    elif g > ans:
        print('猜太大')

def http_error(num):
    match num:
        case 400:
            return 'Bad request'
        case 404:
            return 'Not found'
        case 418:
            return "I'm a teapot"
        case 401|403:
            return 'Not allowed'
        case _:
            return "wrong with the internet"
        
n=400
print(http_error(n))    

