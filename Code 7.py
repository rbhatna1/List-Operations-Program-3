def space(): #To make it look good and have proper demarcations
    print()
    print("**********************************************************")
    print()
    

def even(list):
    print("The even numbers in the list are:",end=" ")
    for a in list:
        if a%2==0:
            print(a,end=" ")
        else:
            print(end="")
            
def odd(list):
    print("The odd numbers in the list are:",end=" ")
    for a in list:
        if a%2!=0:
            print(a,end=" ")
        else:
            print(end="")
            
def evenlist(list):
    n=int(input("Enter the starting range"))
    m=int(input("Enter the ending range"))
    evenlist=[]
    for a in range(n,m+1):
        if list[a]%2==0:
            evenlist.append(list[a])
    print("The even list is:",evenlist)

def oddlist(list):
    n=int(input("Enter the starting range"))
    m=int(input("Enter the ending range"))
    oddlist=[]
    for a in range(n,m+1):
        if list[a]%2!=0:
            oddlist.append(list[a])
    print("The odd list is:",oddlist)
        
            
def number(list):
    positive=0
    negative=0
    for a in list: #Check this in this code
        if a>=0:
            positive+=1
        else:
            negative+=1
    print("The numbers of positive numbers in the list are:",positive)
    print("The number of negative numbers in the list are:",negative)

choice=0

while choice!=6:
    print("Plese choose from one of the following options")
    print("1)Returning the even numbers")
    print("2)Returning the odd numbers")
    print("3)Returning the even list")
    print("4)Returing the odd list")
    print("5)Returing the number of positive and negative numbers")
    print("6)In order to exit the program")
    choice=int(input("Enter the choice"))
    
    if choice==1:
        space()
        list=eval(input("Enter the list"))
        even(list)
        space()
    
    elif choice==2:
        space()
        list=eval(input("Enter the list"))
        odd(list)
        space()
        
    elif choice==3:
        space()
        list=eval(input("Enter the list"))
        evenlist(list)
        space()
        
    elif choice==4:
        space()
        list=eval(input("Enter the list"))
        oddlist(list)
        space()
        
    elif choice==5:
        space()
        list=eval(input("Enter the list"))
        number(list)
        space()