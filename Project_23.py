n = 10
for i in range(n-3):    
    print(" "*(n-i-1),end="")
    for j in range(i+1):
        if j %2 == 0:
            print("*","",end="")    
        else:
            print("-","",end="")    
    print()
for i in range(n-1):
    if i >=2:
        print(" "*(n-i-1),end="")    
        for j in range(i+1):
            if j % 2 == 0:
                print("-","",end="")    
            else:
                print("*","",end="")    
        print()

for i in range(n-5):
        print(" "*(n-3),end="")    
        for j in range(3):        
            print("|","",end="")    
        print() 