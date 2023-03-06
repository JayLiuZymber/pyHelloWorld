#!/usr/bin/python3
# list comprehension
list1 = ['Bob', 'Tom', 'alice', 'Jerry', 'wendy', 'Smith']
list2 = [name.upper() for name in list1 if len(name)>3]
print(list2)

list3 = [i for i in range(30) if i % 3 == 0]
print(list3)

list4 = [name.title() if name.startswith('a') else name.upper() for name in list1]
print(list4)

# -----------------------------------------------------------------------------
dict1 = ['Google', 'Python', 'Youtube']
dict2 = {key: len(key) for key in dict1}
print(dict2)

dict3 = {x: x**2 for x in (2,4,6)}
print(dict3)
print(type(dict3))

# -----------------------------------------------------------------------------
set1 = {i**2 for i in (1,2,3)}
print(set1)

set2 = {x for x in 'abdaceabadac' if x not in 'abc'}
print(set2)
print(type(set2))

# -----------------------------------------------------------------------------
tuple1 = (x for x in range(1,10))
print(tuple1)
print(tuple(tuple1))
