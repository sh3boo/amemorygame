import random
# first we call random library  which will help in this mission to random
letters=['a','b','c','d','e','f','g','h','i','j']
z=2*letters
random.shuffle (z)
num=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,1,5,16,17,18,19,20]
print("WELCOME to the memory game!",num)
p1=0
p2=0
while(num!=['*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*']):
        print("player1 turn")
        n1=int(input("choose a number from the list above "))
        n2=int(input("choose another number from the list above "))
        num[n1-1]=z[n1-1]
        num[n2-1]=z[n2-1]
        print(num)
        if(num[n1-1]==num[n2-1]):
            num[n1-1]=num[n2-1]=z[n1-1]=z[n2-1]="*"
            p1=p1+1
            print ("p1=",p1,num)
        else:
            num[n1-1]=n1
            num[n2-1]=n2
            print("p1=",p1,num)
            print("player2 turn")
            n3=int(input("choose a number from the list above "))
            n4=int(input("choose another number from the list above "))
            num[n3-1]=z[n3-1]
            num[n4-1]=z[n4-1]
            print(num)
        if(num[n3-1]==num[n4-1]):
            num[n4-1]=num[n3-1]=z[n4-1]=z[n3-1]='*'
            p2=p2+1
            print ("p2=",p2,num)
        else:
            num[n3-1]=n3
            num[n4-1]=n4
            print("p2=",p2,num)
if(p1>p2):
    print("player one wins!!!")
elif(p2>p1):
    print("player 2 wins!!!")
else:
    print("Draw")

