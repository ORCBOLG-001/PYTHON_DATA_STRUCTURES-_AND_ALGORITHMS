#-------------------------------------------------------------R-1.1
def is_multiple(n,m):
    if n%m==0:
        return True
    return False
a=is_multiple(5,2)
print(a)

#-------------------------------------------------------------R-1.2
def is_even(k):
    v=k//2
    if k-(v*2)==0:
        return True
    return False
a=is_even(4)
print(a)

#-------------------------------------------------------------R-1.3
a=input("enter values: \t").split()
b=list(int(i) for i in a)
c=sorted(b)
e=c[0],c[len(c)-1]
print(e)

#-------------------------------------------------------------R-1.4
a=int(input("enter number \t"))
b=0
for i in range(1 ,a):
    b+=i*i
print(b)

#-------------------------------------------------------------R-1.5
a=int(input("enter number \t"))
c=sum(i*i for i in range(0,a))
print(c)

#-------------------------------------------------------------R-1.6
a=int(input("eneter number: \t"))
s=0
for i in range(1,a,2):
    s+=i*i
print(s)

#-------------------------------------------------------------R-1.7
a=int(input("eneter number: \t"))
c=sum(i*i for i in range(1,a,2))
print(c)

#-------------------------------------------------------------R-1.8
-(-n)-k

#-------------------------------------------------------------R-1.9
for i in range(50,81,10):
    print(i)

#-------------------------------------------------------------R-1.10
for i in range(8,-9,-2):
    print(i)

#-------------------------------------------------------------R-1.11
a=list(pow(2,i) for i in range(0,9))
print(a)

#-------------------------------------------------------------C-1.13
a=[1,2,3,4,5,6,7]
b=[]
for i in range(len(a),0,-1):
  b.append(i)
print(b)

a=[1,2,3,4,5,6,7]
print(list(reversed(a)))

#-------------------------------------------------------------C-1.14
a=input("enter values \t").split()
b=list(int(i) for i in a)
d=list()
for i in b:
 for j in b:
     if (i*j)%2==1:
         d.append((i,j))
print(d)

#-------------------------------------------------------------C-1.15
a=input("enter values \t").split()
b=list(int(i) for i in a)
d="no duplicate element"
for i in b:
 b.remove(i)
 for j in b:
     if i==j:
         d=i
print(d)

#-------------------------------------------------------------C-1.18
s=0
a=[ i*(i+1) for i in range(1,19,2) ]
print(a)

#-------------------------------------------------------------C-1.19
a=[chr(ord('a')+i) for i in range(0,26)]
print(a)

#-------------------------------------------------------------C-1.20
import random
a=list(input("Enter values \t").split())
x=0
for i in range(0,len(a)):
 n=random.randint(0,len(a)-1)
 x=a[n]
 a[n]=a[i]
 a[i]=x
print(a)

#-------------------------------------------------------------C-1.21
n=[]
while True:
 a=list(input("enter data \t").split())
 n=n+a
 if a[len(a)-1]=='ctrl+D':
  for i in range(len(n)-1,-1,-1):
   print(n[i],end=" ")
  exit()

#-------------------------------------------------------------C-1.22
a=list(input('enter values \t').split())
a=list(int(i) for i in a)
b=list(input("enter values \t").split())
b=list(int(i) for i in b)
c=[]
for i in range(0,len(a)):
  c.append(a[i]*b[i])
print(c)


#-------------------------------------------------------------C-1.23
a=[1,2]
try:
    a[2]=0
except IndexError:
    print("Don't try buffer overflow attacks in python")



#-------------------------------------------------------------C-1.24
a=input("enter string \t").lower()
c=0
for i in range(0,len(a)):
  if(a[i]=='a' or  a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u'):
    c=c+1
print(c)


#-------------------------------------------------------------C-1.25
a=input("enter string \t").lower()
def cod(s):
  b=''
  for i in range(0,len(s)):
    if(ord(s[i])>96 and ord(s[i])<123 or ord(s[i])>64 and ord(s[i])<91):
      b=b+s[i]
  return b
c=cod(a)
print(c)

#-------------------------------------------------------------C-1.26
a=list(input("enter values \t").split())
a=list(int(i) for i in a)
if a[0]+a[1]==a[2]:
     print("a+b=c")
elif a[0]==a[1]-a[2]:
     print("a=b-c")
elif a[0]*a[1]==a[2]:
     print("a*b=c")
else:
    print("none of these")

#-------------------------------------------------------------C-1.27
def factor(n):
    k=1
    m=[]
    while k*k<n:
        if n%k==0:
            yield k
            m.append(n//k)
        k+=1
        if k*k==n:
            yield k
    for i in sorted(m):
     yield i
a=list(factor(100))
print(a)

#-------------------------------------------------------------C-1.28
def norm(v,p=2):
    m=0
    for i in range(0,p):
        m +=v[i]**p
    c=m**(1/p)
    if p==2:
        print("Ecuclidean norm=",c)
    else:
        print("p-norm=",p)
a=int(input("enter p / number of terms\t"))
b=list(input("enter v /the terms\t").split())
b=list(int(i) for i in b)
norm(b,a)

#-------------------------------------------------------------P-1.29
def permute(lst,f=0):
    if f >= len(lst):
        print(lst)
        return
    for s in range(f,len(lst)):
        lst[f],lst[s]=lst[s],lst[f]
        permute(lst,f+1)
        lst[f], lst[s] = lst[s], lst[f]
permute([1,2,3,4])

#-------------------------------------------------------------P-1.30
#error logic building
a=int(input("enter number:\t"))
def bb(a,n=0):
    if a>2:
        bb(a/2,n+1)
    else:
     return n
s=bb(a)
print(s)
#legit solution
def divide(a):
    count = 0
    if a>=2:
        a = a // 2
        count += 1
        divide(a)
        print("-----")
    print(count)
divide(11)

#-------------------------------------------------------------P-1.31
def fun(a, b):
    y = a - b
    n1 = 0
    n2 = 0
    n3 = 0
    n4 = 0
    while y > 0:
        if y % 100 == 0:
            n1 += 1
            y = y - 100
        elif y % 50 == 0:
            n2 += 1
            y = y - 50
        elif y % 10 == 0:
            n3 += 1
            y = y - 10
        else:
            n4 += 1
            y = y - 1
    print("100:", n1, "\n50:", n2, "\n10:", n3, "\n1:", n4)


a = list(input("enter money , charge \t").split())
a1 = int(a[0])
b = int(a[1])
fun(a1, b)

#-------------------------------------------------------------P-1.32
while True:
 a=int(input("enter number 01\t"))
 b=int(input("enter number 02\t"))
 c=input("enter operation\t")
 op = {'+': lambda x, y: x + y,
       '-': lambda x, y: x - y,
       '*': lambda x, y: x * y,
       '/': lambda x, y: x / y}
 z=op[c](a,b)
 print(z)
 n=input("for exit press n \t")
 if(n=='t'):
     exit()


#-------------------------------------------------------------P-1.33
import os
print("ggg")
os.system("cls")


#-------------------------------------------------------------P-1.34
import random
a='I will never spam my friends again.'
a=list(a)

for i in range(0,100):
 b = a.copy()
 for i in range(0,8):
    c=random.randint(0,34)
    b.pop(c)
    d=random.randint(32, 127)
    b.insert(c,chr(d))
 print(''.join(map(str,b)))
