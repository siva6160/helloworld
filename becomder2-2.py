def largest(a=0,b=0,c=0):
    print(a)
    print(b)
    print(c)
    if a>b and a>c:
        print("a is largest")
    elif b>a and b>c:
        print( "b is largest")
    elif c>a and c>b:
        print("c is largest")
a=int(input("enter anumber"))
b=int(input("enter a  number"))
c=int(input("enetr a number"))
largest(a,b,c)
