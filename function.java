def fib(n):
    a=0
    b=1
    print(a)
    print(b)
    if n==1:
        print(a)
    else:
    
        for i in range(2,n):
            c=a+b
            a=b
            b=c
    
            print(c)
fib(1)
