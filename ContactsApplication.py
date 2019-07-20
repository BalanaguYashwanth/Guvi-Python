
a=dict()
def add(name,number):
    a[name]=number
    print(a)
    

def remove(user):
    a.pop(user)    
    
def show():
    print(a)
    
def search(user):
    if user in a:
        print(f"name {name} is exist ")
        
def display(user,number):
    for name,number in a.items():
        print(name,number)

b=input(1.'Add',
       2.'Remove',
       3.'Show',
       4.'Display',
       5.'exit')

i=1    
while (1):
    if b == 'Add':
        name=input()
        number=input()
        add(name,number) 
    elif b == 'Remove':
        user=input("enter your hate person:")
        remove(user)
    elif b == 'Show':
        show()
    elif b == 'Search':
        user=input("enter your loved person:")
        search(user)
    elif b == 'Display':
        user=input("enter your loved person:")
        number=input('enter the person no.:')
        display(user,number)
    elif b == 'exit':
        break    
