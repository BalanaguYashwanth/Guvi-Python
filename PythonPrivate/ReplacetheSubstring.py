a=input()
b=a.split()
c=input()
for i in range(3):
    if(b[i]==c):
        b[i]='go'
        
for i in range(3):
    print(b[i],end=" ")
    
