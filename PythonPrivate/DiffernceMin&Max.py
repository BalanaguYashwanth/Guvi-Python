a=int(input('enter the value in a'))
b=[]
min=0
max=0
for i in range(a):
    b.append(input('enter the values in array'))
    
min=b[0]
max=b[0]
for i in range(a):
    if(min>b[i]):
        min=b[i]
    if(max<b[i]):
        max=b[i]
        
print(int(max)-int(min))
