def A():
    for row in range(6):
        for col in range(7):
            if(((col==0 or col==6) and row!=0) or ((col==2 or col==4 ) and (row==0 or row==3))):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def B():
    for row in range(7):
        for col in range(7):
            if(((row==0 or row==3 or row==6) and col!=1 and col!=3 and col!=5 and col!=6 ) or (col==0) or ((row==1 or row==2 or row==4 or row==5) and col==6)):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def C():
    for row in range(5):
        for col in range(7):
            if(((row==0 or row==4) and col!=0 and col!=1 and col!=3 and col!=5) or (col==0 and (row!=0 and row!=4))):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def D():
    for row in range(5):
        for col in range(7):
            if(((row==0 or row==4) and col!=1 and col!=3 and col!=5 and col!=6) or col==0 or (col==6 and row!=0 and row!=4)):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def E():
    for row in range(7):
        for col in range(7):
            if(((row==0 or row==3 or row==6) and col!=1 and col!=3 and col!=5) or col==0 ):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def F():
    for row in range(7):
        for col in range(7):
            if(((row==0 or row==3) and col!=1 and col!=3 and col!=5) or col==0 ):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def G():
    for row in range(6):
        for col in range(9):
            if((col==0 and row!=0 and row!=5) or ((row==0 or row==5) and (col==2 or col==4 or col==6)) or (row==3 and (col==4 or col==6)) or (col==8 and (row==1 or row==3 or row==4))):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def H():
    for row in range(5):
        for col in range(7):
            if(((col==0 or col==6)) or ((col==2 or col==4 ) and row==2)):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def I():
    for row in range(6):
        for col in range(9):
            if(((row==0 or row==5) and col!=1 and col!=3 and col!=5 and col!=7) or col==4 ):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def J():
    for row in range(5):
        for col in range(9):
            if((col==6 and row!=4) or (col==0 and (row==2 or row==3)) or (row==4 and (col==2 or col==4))):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def K():
    for row in range(7):
        for col in range(7):
            if(col==0 or (col==2 and (row==2 or row==4)) or (col==4 and (row==1 or row==5)) or (col==6 and (row==0 or row==6))):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def L():
    for row in range(5):
        for col in range(9):
            if(col==0 or (row==4 and (col==2 or col==4 or col==6))):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def M():
    for row in range(5):
        for col in range(13):
            if(col==0 or col==8 or (row==1 and (col==2 or col==6)) or (row==2 and col==4)):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def N():
    for row in range(5):
        for col in range(9):
            if(col==0 or col==8 or (row==1 and col==2) or (row==2 and col==4) or (row==3 and col==6)):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def O():
    for row in range(5):
        for col in range(9):
            if(((col==0 or col==8) and row!=0 and row!=4) or ((row==0 or row==4) and (col==2 or col==4 or col==6))):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def P():
    for row in range(6):
        for col in range(7):
            if(col==0 or ((row==0 or row==3) and (col==2 or col==4)) or (col==6 and (row==1 or row==2))):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def Q():
    for row in range(6):
        for col in range(10):
            if(((col==0 or col==8) and (row==1 or row==2 or row==3)) or ((row==0 or row==4) and (col==2 or col==4 or col==6)) or (row==5 and col==9) or (row==3 and col==6)):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def R():
    for row in range(7):
        for col in range(7):
            if(col==0 or ((row==0 or row==3) and (col==2 or col==4)) or (col==6 and (row==1 or row==2 or row==6)) or (row==4 and col==2) or (row==5 and col==4)):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def S():
    for row in range(7):
        for col in range(7):
            if((col==0 and (row==1 or row==2 or row==6)) or (col==2 and (row==0 or row==3 or row==6)) or (col==4 and (row==0 or row==3 or row==6)) or (col==6 and (row==0 or row==4 or row==5))):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def T():
    for row in range(5):
        for col in range(9):
            if((row==0 and col!=1 and col!=3 and col!=5 and col!=7) or col==4 ):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def U():
    for row in range(5):
        for col in range(9):
            if((col==0 and row!=4) or (col==8 and row!=4) or (row==4 and (col==2 or col==4 or col==6))):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def V():
    for row in range(5):
        for col in range(9):
            if((row==0 and (col==0 or col==8)) or (row==1 and (col==1 or col==7)) or (row==2 and (col==2 or col==6)) or (row==3 and (col==3 or col==5)) or (row==4 and col==4)):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def W():
    for row in range(5):
        for col in range(9):
            if(col==0 or col==8 or (row==2 and col==4) or (row==3 and (col==2 or col==6))):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def X():
    for row in range(5):
        for col in range(9):
            if((row==0 and (col==0 or col==8)) or (row==1 and (col==2 or col==6)) or (row==2 and col==4) or (row==3 and (col==6 or col==2))  or (row==4 and (col==8 or col==0))  ):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def Y():
    for row in range(5):
        for col in range(9):
            if((row==0 and (col==0 or col==8)) or (row==1 and (col==2 or col==6)) or (col==4 and row!=0 and row!=1)):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def Z():
    for row in range(5):
        for col in range(9):
            if(((row==0 or row==4) and col!=1 and col!=3 and col!=5 and col!=7) or (row==1 and col==6) or (row==2 and col==4) or (row==3 and col==2)):
                print("*",end="")
            else:
                print(" ",end="")
        print()



def One():
    for row in range(6):
        for col in range(9):
            if(col==4 or (col==0 and row==2) or (col==2 and row==1) or (row==5 and col!=1 and col!=3 and col!=5 and col!=7)):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def Two():
    for row in range(5):
        for col in range(7):
            if((col==0 and (row==1 or row==4)) or (col==2 and row!=1 and row!=2) or (col==4 and row!=1 and row!=3) or (col==6 and (row==1 or row==4))):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def Three():
    for row in range(7):
        for col in range(7):
            if((col==0 and (row==1 or row==5)) or (col==2 and (row==0 or row==6)) or (col==4 and (row==0 or row==3 or row==6)) or (col==6 and row!=0 and row!=3 and row!=6)):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def Four():
    for row in range(5):
        for col in range(9):
            if((col==0 and row!=3 and row!=4) or (row==2 and (col==2 or col==4)) or col==6 ):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def Five():
    for row in range(6):
        for col in range(7):
            if((col==0 and row!=3 and row!=5) or ((col==2 or col==4) and row!=1 and row!=3 and row!=4)  or (col==6 and row!=1 and row!=2 and row!=5)):
               print("*",end="")
            else:
                print(" ",end="")
        print()

def Six():
    for row in range(7):
        for col in range(9):
            if((col==0 and row!=0 and row!=6) or ((col==2 or col==4) and (row==0 or row==3 or row==6)) or (col==6 and (row==1 or row==4 or row==5))):
               print("*",end="")
            else:
                print(" ",end="")
        print()

def Seven():
    for row in range(5):
        for col in range(7):
            if((row==0 and col!=1 and col!=3 and col!=5) or col==6):
               print("*",end="")
            else:
                print(" ",end="")
        print()

def Eight():
    for row in range(7):
        for col in range(9):
            if((col==0 and row!=0 and row!=6 and row!=3) or ((col==2 or col==4) and (row==0 or row==3 or row==6)) or (col==6 and row!=0 and row!=3 and row!=6)):
               print("*",end="")
            else:
                print(" ",end="")
        print()

def Nine():
    for row in range(7):
        for col in range(7):
            if(((row==0 or row==3) and (col==2 or col==4) or (col==0 and (row==1 or row==2)) or (col==6 and row!=0))):
               print("*",end="")
            else:
                print(" ",end="")
        print()




print("Enter any Alphabate:",end="")
text=input()
for i in text.upper():
    print(".....................")

    if i=="A":
        A()
    elif i=="B":
        B()
    elif i=="C":
        C()
    elif i=="D":
        D()
    elif i=="E":
        E()
    elif i=="F":
        F()
    elif i=="G":
        G()
    elif i=="H":
        H()
    elif i=="I":
        I()
    elif i=="J":
        J()
    elif i=="K":
        K()
    elif i=="L":
        L()
    elif i=="M":
        M()
    elif i=="N":
        N()
    elif i=="O":
        O()
    elif i=="P":
        P()
    elif i=="Q":
        Q()
    elif i=="R":
        R()
    elif i=="S":
        S()
    elif i=="T":
        T()
    elif i=="U":
        U()
    elif i=="V":
        V()
    elif i=="W":
        W()
    elif i=="X":
        X()
    elif i=="Y":
        Y()
    elif i=="Z":
        Z()
    elif i=="1":
        One()
    elif i=="2":
        Two()
    elif i=="3":
        Three()
    elif i=="4":
        Four()
    elif i=="5":
        Five()
    elif i=="6":
        Six()
    elif i=="7":
        Seven()
    elif i=="8":
        Eight()
    elif i=="9":
        Nine()

'''
match i:
    case 'A':
        A()
    case 'B':
        B()
'''


