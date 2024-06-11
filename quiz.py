import time
def timer(t):
    crt=time.time()
    flag=0
    if crt-t>=15:
        flag=1
        return flag
     
def oper(a,ol,n):
    ctm=timer(n)
    if ctm==1:
        print("Time finished")
        return 0
    else:
        answers=[1,2,4,3]
        if a==answers[ol]:
            print("Correct")
            return 1
        else:
            print("Wrong")
            return 0
        
def quiz():
    score=0
    oplp=0       
    print("(1) Which team has the most number of UEFA Champions league?")
    print("1:Real Madrid 2:PSG 3:Liverpool 4:AC Milan")
    n=time.time()
    ans=int(input("Enter your option:"))
    s=oper(ans,oplp,n)
    score=score+s
    oplp=oplp+1

    print("(2) Who has the most international goals in football history?")
    print("1:Chhetri 2:Ronaldo 3:Neymar 4:Messi")
    n=time.time()
    ans=int(input("Enter your option:"))
    s=oper(ans,oplp,n)
    score=score+s
    oplp=oplp+1

    print("(3)Which country holds the most number of FIFA world cups? ")
    print("1:Germany 2:Argentina 3:India 4:Brazil")
    n=time.time()
    ans=int(input("Enter your option:"))
    s=oper(ans,oplp,n)
    score=score+s
    oplp=oplp+1

    print("(4) Who has the won the most number of BALLON'dor in football history? ")
    print("1:Kaka 2:Ronaldo 3:Messi 4:Ronaldinho")
    n=time.time()
    ans=int(input("Enter your option:"))
    s=oper(ans,oplp,n)
    score=score+s
    print("Final score:",score,"out of",oplp+1)

quiz()