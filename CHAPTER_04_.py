#----------------------------------------------R-4.1
def maxi(S,n):
    b=S[n]
    if n==len(S)-1:
        return S[n]
    elif b>maxi(S,n+1):
        return b
    else:
        return maxi(S,n+1)

S=[1,0,2,7,9,8]
n=0
print(maxi(S,n))


#----------------------------------------------R-4.2
def power(a,b):
    if b==1:
        return a
    else:
        return a*power(a,b-1)
a=2;b=6
print(power(a,b))


#----------------------------------------------R-4.3
def power2(a,b):
    if b==1:
        return a
    else:
        res1=power2(a,b//2)
        res2=res1*res1
        if b%2==1:
            res2=res2*a
        return res2
a=2;b=6
print(power2(a,b))


#----------------------------------------------R-4.6
def harmonica(a,n):
    if n==1:
        return 1/a
    else:
        return (1/a)*harmonica(a,n-1)
a=3
n=3
print(harmonica(a,n))


#----------------------------------------------R-4.7
def integer(a,n):
    if n<3:
        return a
    else :
        return str(f"{integer(a//1000,n-3)},{a%1000}")
a=1234567
b=7
print(integer(a,b))


#----------------------------------------------C-4.9
def func(S,n=0):
     if n==len(S)-1:
          return S[n]
     elif func(S,n+1)>S[n]:
          return func(S,n+1)
     else:
          return S[n]
S=[1,2,7,4,3,9,0,5]
print(func(S))

def func2(S, n=0):
    if n == len(S) - 1:
        return S[n]
    elif func2(S, n + 1) < S[n]:
        return func2(S, n + 1)
    else:
        return S[n]
S = [1, 2, 7, 4, 3, 9, -2, 5]
print(func2(S))


#----------------------------------------------C-4.10
def funv(a,n=0):
    if a>=2:
      print(a)
      return funv(a/2,n+1)
    else:
        return n

a=33
print(funv(a))


#----------------------------------------------C-4.11
def num(S):
   if(len(S)>1):
    for i in range(1,len(S)-1):
        if S[0]==S[i]:
            print("Copycat:",S[0])
    del(S[0])
    num(S)

S=[1,2,6,3,7,1,3,2,4]
num(S)



#----------------------------------------------C-4.12
def mul(a,b):
     c=max(a,b)
     d=min(a,b)
     if d>0:
         return c+mul(c,d-1)
     else:
         return 0

print(mul(9,7))



#----------------------------------------------C-4.14
def hanoi(n,a,b,c):
    if n==1:
        print("moving disk %d from %s to %s"%(n,a,b))
        return
    hanoi(n-1,a,c,b)
    print("moving disk %d from %s to %s" % (n, a, b))
    hanoi(n-1,c,b,a)
hanoi(3,"A","C","B")


#----------------------------------------------C-4.15
def subs(l):
    if l == []:
        return [[]]
    print(l[1:],"-------------------01")
    x = subs(l[1:])
    print(x,"--------------------02")
    print(l[0],"-----------------------03")
    print( x + [[l[0]] + y for y in x],"---------------------04")
    return( x + [[l[0]] + y for y in x])

print (subs([1, 2, 3]))


#------------------------------------------------C-4.16
def reversy(n,i):
    if i>=0:
     print(n[i],end=" ")
     reversy(n,i-1)
    else:
        quit()
n=[1,2,3,4,5,6]
reversy(n,5)


#------------------------------------------------C-4.17
def rev(a,n):
    if a==0:
     for i in range(0,int((len(n)+1)/2)+1):
         z=n[i]
         y=rev(len(n)-i-1,n)
         if z==y:
             print(z,end=" ")
    elif a>=int((len(n)+1)/2):  #beware of for if/else,index +-1
            return n[a]         #difference for position, length.

n=[1,2,3,4,3,2,1]
print((len(n)+1)/2)   #float
rev(0,n)


#------------------------------------------------C-4.18
def line(n,i,v=0,c=0):
    if i>=0:
        if n[i]=="a" or n[i]=="e" or n[i]=="i" or n[i]=="o" or n[i]=="u":
            line(n,i-1,v+1,c)
        else:
            line(n,i-1,v,c+1)   #here we do not return value like conventional ways
    else:                       #instead we have total value sum at last recursion.
        print('v=',v,"c=",c)
        quit()

n=["a","e","p","u","h"]
print(line(n,len(n)-1))


#------------------------------------------------C-4.19
def value(n,i):
    if n[i]%2!=0:
        c=n[i]
        n.pop(i)
        n.append(c)
    if i==0:
        print(n)
        quit()
    value(n,i-1)

n=[1,2,3,4,5,6,7,8,9]
value(n,len(n)-1)


#------------------------------------------------C-4.20
def value(n,i,check):
    if n[i]>check:
        c=n[i]
        n.pop(i)
        n.append(c)
    if i==0:
        print(n)
        quit()
    value(n,i-1,check)

n=[1,12,11,4,5,6,7,8,9]
check=5
value(n,len(n)-1,check)


#------------------------------------------------C-4.21
def value(n,sum,n1=0,i=0,turn=1):

   if turn==1:
    for i in range(0,len(n)):
     n1=n[i]
     value(n,sum,n1,i,turn=2)   #we use turn to limit no of recursions
                                #by using specific conditions, etc.
   elif turn==2:
    for i in range(i,len(n)):
      n2=n[i]
      if n1+n2==sum:
         print("solution ",n1,",",n2)
         quit()
    return                      #when we want to return nothing

n=[1,2,3,4,5,6,7,8,9,10]
sum=16
value(n,sum)


#------------------------------------------------C-4.22
def pow(a,b,p=1):
    for _ in range(0,b):
        p=p*a
    return p
print(pow(3,3))



#--------------------------------------------------P-4.24
def permutations(S,n,v7,v6,v5,v4,v3,v2,v1,c=0):
    for i in range(0,n):     #n is 10 cause 0-9
        if c==0:
         print("----------------------------------------------------------------------xyzdelta")
         permutations(S,n,v7,v6,v5,v4,v3,v2,v1=i,c=c+1)
        if c==1 and v1!=i :
         permutations(S,n,v7,v6,v5,v4,v3,v2=i,v1=v1,c=c+1)
        if c==2 and v1!=i and v2!=i:
         permutations(S,n,v7,v6,v5,v4,v3=i,v2=v2,v1=v1,c=c+1)
        if c==3 and v1!=i and v2!=i and v3!=i:
         permutations(S,n,v7,v6,v5,v4=i,v3=v3,v2=v2,v1=v1,c=c+1)
        if c==4 and v1!=i and v2!=i and v3!=i and v4!=i:
         permutations(S,n,v7,v6,v5=i,v4=v4,v3=v3,v2=v2,v1=v1,c=c+1)
        if c==5  and v1!=i and v2!=i and v3!=i and v4!=i and v5!=i:
         permutations(S,n,v7,v6=i,v5=v5,v4=v4,v3=v3,v2=v2,v1=v1,c=c+1)
        if c==6  and v1!=i and v2!=i and v3!=i and v4!=i and v5!=i and v6!=i:
         permutations(S,n,v7=i,v6=v6,v5=v5,v4=v4,v3=v3,v2=v2,v1=v1,c=c+1)
        if c==7 :
            print("----------------------------------------------------------",v1,v2,v3,v4,v5,v6,v7)
            results=check(S,n,v7=v7,v6=v6,v5=v5,v4=v4,v3=v3,v2=v2,v1=v1)
            if results==True:
                print("SUCCESSFUL")
                quit()
            else:
                return
    if c!=0:
            print("returned")
            return


def check(S,n,v7,v6,v5,v4,v3,v2,v1):
    global q
    L1=["p","o","t"]
    L2=["p","a","n"]
    L3=["b","i","b"]
    for i in range(0,len(S)):
        elem=S[i]
        c=0
        if i==0:
            c=v1
        elif i==1:
            c=v2
        elif i==2:
            c=v3
        elif i==3:
            c=v4
        elif i==4:
            c=v5
        elif i==5:
            c=v6
        elif i==6:
            c=v7
        for j in range(0,3):
            if S[i]==L1[j]:
                L1.remove(L1[j])
                L1.insert(j,c)
            if S[i]==L2[j]:
                L2.remove(L2[j])
                L2.insert(j,c)
            if S[i]==L3[j]:
                L3.remove(L3[j])
                L3.insert(j,c)
    for i in range(0,3):
        if L1[i]+L2[i]==L3[i]:
            pass
        else:
            q=q+1
            print("condition failed",q,"-----",v1,v2,v3,v4,v5,v6,v7)
            return False
    print("-------------------------------------------",L1,"+",L2,"=",L3)
    return True

global q
q=0
S=["p","o","t","a","n","b","i"]
permutations(S,n=10,v7=11,v6=11,v5=11,v4=11,v3=11,v2=11,v1=11,c=0)


#--------------------------------------------------P-4.25
def func1(lines,lenth,val=-1):
    if val != -1:
        print(lenth*"-",val,end="\n")
    for i in range(0,len(lines)):
     print(lines[i])
    return

def func2(val,middles):
    rows=int(math.pow(2,middles-1))
    a=[0]*(rows)
    step=rows
    times=middles
    for i in range(middles,0,-1):    # using logic n/2, n/4, n/8 ..... step size
        step=int(step/2)             # and changing value along the steps if==0
        if step>=1:                  # in the length n and starting from 0 evertime.
         times = times - 1
         for i in range(0,rows,step):
            if a[i]==0:
             a[i]=times*"-"

    a.pop(0)
    for i in range(0,len(a)):
         if a[i]==0:
                a.pop(i)
                a.insert(i,"-")
    func1(a,5,val)
    quit()

import math
func2(1,6)
