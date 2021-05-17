import math as m
def pow(num,p):
    res=num**p
    return res
num=int(input("enter a number"))
p=int(input("enter a num"))
s=pow(num,p)
print(s)
print(m.pow(num,p))
print(m.sqrt(num))
print(m.ceil(num))
print(m.floor(num))
