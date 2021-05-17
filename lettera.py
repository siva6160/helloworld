n=int(input("enter the no of no rows"))
for i in range(0,7):
    for j in range(0,6):
        if i==1 and j==2 or i==i+1 and j==j-1:
            print("*")
        
    print()
