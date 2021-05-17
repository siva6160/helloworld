import math
def sum(a,b):
    a+=b
    return a
def sub(a,b):
    a-=b
    return a
def div(a,b):
    q=a/b
    r=a%b
    print(q,r)
def mul(a,b):
    a*=b
    return a
def sr(a):
    s=math.sqrt(a)
    return s
while(True):
    print("eneter your choice")
    print("\n 1.ADDITION","\n 2.SUBSTRACTION","\n 3.DIVISION","\n 4.multipication","\n 5.sqare root")
    ch=int(input('>'))
    if ch==1:
        print("enter two numbers")
        num1=int(input('>'))
        num2=int(input('>>'))
        s=sum(num1,num2)
        print(s)
    elif ch==2:
        print("eneter two numbers")
        num1=int(input('>'))
        num2=int(input('>>'))
        h=sub(num1,num2)
        print(h)
    elif ch==3:
        print("enter two numbers")
        num1=int(input(">>"))
        num2=int(input(">>"))
        y=div(num1,num2)
        print(y)
    elif ch==4:
        print("enetr two numers")
        num1=int(input('>'))
        num2=int(input('>'))
        m=mul(num1,num2)
        print(m)
    elif ch==5:
        print("enter two number")
        num1=int(input(">"))
        a=sr(num1)
        print(a)
    
        
