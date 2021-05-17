n,r1,r2=map(int,input("enter").split())
for i in range(1,r2+1):
     if i%r1 and i%n:
          continue   
          print(n,i,n*i)
    
