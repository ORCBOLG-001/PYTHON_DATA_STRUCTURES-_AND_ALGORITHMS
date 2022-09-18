def gig(n):
    n.append(0)              #original passed list changes because we make
    n[1]=13                  #change in orignal list and not a copy like                     ##########################
                             #b=a and that points to refrences of a but
n=[1,2,3]                    #as soon any change in b seperate refrences
gig(n)                       #are created for those changes for b.
print(n)


a=[0]*7         #initialize array                                                              ###########
print(a)
b=[None]*7      #initialize array
print(b)

a=[1,2,3,4,5,6,7]
b=a
c=list(a)
a[0]=4
print(a,b)
#[4, 2, 3, 4, 5, 6, 7] [4, 2, 3, 4, 5, 6, 7]
print(a,c)
#[4, 2, 3, 4, 5, 6, 7] [1, 2, 3, 4, 5, 6, 7]


a=[1,2,3,4]
b=[1,2,3,4]
a.extend(b)               # extend vs append                                                   ###########
print(a)
a=[1,2,3,4]
b=[1,2,3,4]
a.append(b)
print(a)
#[1, 2, 3, 4, 1, 2, 3, 4]
#[1, 2, 3, 4, [1, 2, 3, 4]]


for i in range(9):                                                                              ##########
    print(i)

a=[1,2,3,4,5,6,7]
b=a[0:5]      #calling method                                                                   ##########
a[0]=0
print(a,b)

a.extend(b)    #add list 2 to another list 1
print(a)       #from the end index of list 1

x="jsk 09-5#$%# fhd"
l='__'
l=l.join(i for i in x if i.isalpha())                                                            #########
print(l)


#---------------------------------------------------R-5.1
import sys
a=[1,2]
for i in range(0,30):
    a.append(0)
    print(sys.getsizeof(a))      #size that variable takes in memory                             #########


#--------------------------------------------------R-5.2
print("\n")
import sys
a=[]
v=0
for i in range(0,30):
    a.append(None)
    z=sys.getsizeof(a)
    if v==0:
        v=z
        print(len(a))
    elif z!=v:
        v=z
        print(len(a))


#--------------------------------------------------R-5.3
print("\n--")
import sys
a=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
b=list(a)          #make a copy of values to a new location in memory                              #########
for i in b:
    a.remove(i)     #remove mutates the original list as it directly
                    #changes value directly at reference location
    print("size =",sys.getsizeof(a),", i =",i,", a",a)


#----------------------------------------------------------------------------------R-5.4
import ctypes
class dynamicarray:
    def __init__(self):
     self._n=0                   #actual elements
     self._capacity=1            #max size
     self._array=self.formation(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self,k):
        if 0<=k and k<self._n:
          return self._array[k]
        elif k>=-self._n:
          return self._array[self._n+k]

        print("out of bound")

    def append(self,v):
        if self._capacity>self._n :
            self._array[self._n]=v
        elif self._capacity==self._n:
            self.change(self._capacity)
            self._array[self._n]=v
        else:
            print("limit exceeded")
            quit()
        self._n+=1

    def change(self,c):
        Z=self.formation(2*c)
        for i in range(self._n):
            Z[i]=self._array[i]
        self._array=Z
        self._capacity=2*self._capacity

    def formation(self,c):
        return(c*ctypes.py_object)()        #take care of brackets outside                                 #########

    def arr(self):
        D=[0]*self._n
        for i in range(0,self._n):
            D[i]=self._array[i]
        return(D)


Q=dynamicarray()
print(len(Q))
Q.append(8)
Q.append(119)
print(len(Q))
Q.append(6)
Q.append(7)
Q.append(1)
Q.append(0)
print(Q.__len__())
Q.append(15)
Q.append(11)
print("elements",Q._n,"capacity",Q._capacity,"array",Q.arr())                #take care of brackets           #########

print("----",Q.__getitem__(-8))                                       #1.    #this is how we call getitem
print(Q.__getitem__(2))                                                      #for object Q of the class
print(Q[1])                                                           #2.    #dynamicarray()

print("----",Q.__getitem__(-9))




#------------------------------------------------------------------------------------R-5.6
import ctypes
class dynamicarray:
    def __init__(self):
     self._n=0                   #actual elements
     self._capacity=1            #max size
     self._array=self.formation(self._capacity)

    def append(self,v):
        if self._capacity>self._n :
            self._array[self._n]=v
        elif self._capacity==self._n:
            self.change(self._capacity)
            self._array[self._n]=v
        else:
            print("limit exceeded")
            quit()
        self._n+=1

    def change(self,c):
        Z=self.formation(2*c)
        for i in range(self._n):
            Z[i]=self._array[i]
        self._array=Z
        self._capacity=2*self._capacity

    def formation(self,c):
        return(c*ctypes.py_object)()        #take care of brackets outside

    def arr(self):
        D=[0]*self._n
        for i in range(0,self._n):
            D[i]=self._array[i]
        return(D)

    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    def insert(self,k,value) ->list:
        a=[0]*(self._n+2)
        if k>=0 and k<=self._n:
          a=self._array[:k]+[value]+self._array[k:self._n]    #insert value without shifting elements 1 by 1    ########
        return a                                              #eg.
                                                                # a=[1,4,5,6,7,3,2,9,0]
                                                                # a=a[:4]+[88]+a[4:9]
                                                                # print(a)

Q=dynamicarray()
Q.append(1)
Q.append(2)
Q.append(3)
print(Q.arr())
print(Q.insert(1,9))
     #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


#------------------------------------------------------------------------------------R-5.7
def logiv(A):
    n=len(A)
    return sum(A)-((n-1)*n)/2    #mathematics sum of n natural numbers                                 #######

A=[1,2,3,4,5,6,7,8,9,4]
print(logiv(A))


#------------------------------------------------------------------------------------R-5.8
from time import time                                                                                 ########
def pops(t,x):
     a=[None]*t
     s=time()
     q=t

     if x==1:
      tc = t
      for _ in range(t):
           tc=tc-1
           a.pop(tc)
     elif x==2:
      cc=int(t/2)-1
      for _ in range(int(t/2)):
           a.pop(cc)
           cc=cc-1
     elif x==3:
      for _ in range(t):
           a.pop(0)

     e=time()                                                                                           ########
     return(e-s)/q


print(pops(100000,1))
print(pops(100000,2))
print(pops(100000,3))


#------------------------------------------------------------------------------------R-5.10
shift=4
x="ABCDEFGHI"
x=list(x)
x2="".join(chr(ord(a)+shift) for a in x)   #chr   #ord  #join   #list comprehension                     #########
print(x2)


#------------------------------------------------------------------------------------R-5.11
a=[[1,2,3],[4,5,6],[7,8,9]]
n=3
sum=0
for i in range(0,n):
    for j in range(0,n):
        sum=sum+a[i][j]
print(sum)


#------------------------------------------------------------------------------------R-5.12
#a=[[1,2,3],[4,5,6],[7,8,10]]
#n=3
#z=sum([a[i][j] for i in range(0,n) for j in range(0,n)])    #sum using list comprehension and sum()     ##########
#print(z)


#------------------------------------------------------------------------------------C-5.13
def func(n):
 if str(type(n))=="<class 'int'>":             #type used for conditional statements                     ##########
  a=[n]
 elif str(type(n))=="<class 'list'>":
  a=n
 print(type(n),a)
 v=0
 for i in range(0,90):
    a.append(None)
    z=sys.getsizeof(a)
    if v==0:
        v=z
        print(len(a))
    elif z!=v:
        v=z
        print(len(a))

import sys
func(1)
print("\n")
func(2)
print("\n")
func([7,1,3,4,7,8,0])


#------------------------------------------------------------------------------------C-5.14
def gelly(a,n):
 for _ in range(n):
    b=random.randint(0,n-1)
    print(b)
    if b not in a:                  #or use a.count(b)<0 to see if None
        for i in range(0,n):
            if a[i]==None:
                a[i]=b
                break
            else:
                pass
 print("changed :",a)

import random
n=17
a=[None]*17
for i in a:
    if i==None:
        gelly(a,n)
        print("returned:",a)
print("result :",a)


#------------------------------------------------------------------------------------C-5.16, C-5.17, C-5.18, C-5.19
import ctypes
class dynamicarray:
    def __init__(self):
     self._n=0                   #actual elements
     self._capacity=1            #max size
     self._array=self.formation(self._capacity)

    def append(self,v):
        if self._capacity>self._n :
            self._array[self._n]=v
        elif self._capacity==self._n:
            self.change(self._capacity)
            self._array[self._n]=v
        else:
            print("limit exceeded")
            quit()
        self._n+=1

    def change(self,c):
        Z=self.formation(2*c)
        for i in range(self._n):
            Z[i]=self._array[i]
        self._array=Z
        self._capacity=2*self._capacity

    def formation(self,c):
        return(c*ctypes.py_object)()        #take care of brackets outside

    def arr(self):
        D=[0]*self._n
        for i in range(0,self._n):
            D[i]=self._array[i]
        return(D)

    def __str__(self):
        b=[0]*self._n                           #create new array as if we send self._array                ############
        for i in range(0,self._n):              #we get object reference
            b[i]=self._array[i]
        return f'({b})'                         #type error string returned must be type str               ############
                                                #for print(Q) below outside class.
    def pop(self):
        new=[0]*(self._n-1)
        for i in range (0, self._n-1):
            new[i]=self._array[i]
        if len(new)<int(self._capacity/4):
            self._capacity=self._capacity/2
        self._n=self._n-1
        print('capcity:',self._capacity)
        return new



Q=dynamicarray()
Q.append(1)
Q.append(2)
Q.append(3)
Q.append(4)
Q.append(5)
Q.append(6)
Q.append(7)
Q.append(8)
Q.append(9)
Q.append(10)
Q.append(11)
Q.append(12)
Q.append(13)
print(Q)
print(Q.pop())
print(Q.pop())
print(Q.pop())
print(Q.pop())
print(Q.pop())
print(Q.pop())
print(Q.pop())
print(Q.pop())
print(Q.pop())
print(Q.pop())
print(Q.pop())
print(Q.pop())


#------------------------------------------------------------------------------------------------------C-5.21
from time import time
document=["a","b","c","d","e","f","a","b","c","d","e","f","a","b","c","d","e","f","a","b","c","d","e",
          "f","a","b","c","d","e","f","a","b","c","d","e","f","a","b","c","d","e","f""a","b","c","d",
          "e","f","a","b","c","d","e","f","a","b","c","d","e","f","a","b","c","d","e","f","a","b","c","d","e",
          "f","a","b","c","d","e","f","a","b","c","d","e","f","a","b","c","d","e","f""a","b","c","d"]*100000

s=time()
letters1=""
for c in document:
    if c.isalpha():
        letters1+=c
e=time()                                              #Time they took for completion                        ###########
print(e,s,e-s,len(letters1))                          #9.013304233551025 , slowest


f=time()
letters2=""
temp=[]
for c in document:
    if c.isalpha():
        temp.append(c)
letters2="".join(temp)
g=time()
print(g,f,g-f,len(letters2))                          #2.1315112113952637


h=time()
letters3=''
letters3="".join([c for c in document if c.isalpha()])
i=time()
print(i,h,i-h,len(letters3))                          #1.1109821796417236 , fastest


j=time()
letters4=""
letters4="".join(c for c in document if c.isalpha())
k=time()
print(k,j,(k-j),len(letters4))                        #1.5089998245239258


#------------------------------------------------------------------------------------------------------C-5.22
from time import time
a=["a"]
b=["b"]*10000000
s=time()
for i in b:
    a.append(i)
e=time()                 #Time they took for completion                                                    ###########
print(e-s)               #1.5797088146209717

a2=["a"]
b2=["b"]*10000000
s1=time()
a2.extend(b2)
e1=time()
print(e1-s1)             #0.04911923408508301 , fastest


#------------------------------------------------------------------------------------------------------C-5.23
from time import time
a1=time()                           #Time they took for completion                                     ###########
s=[7 for _ in range(0,100000000)]   #4.390850305557251
a2=time()
print(a2-a1)

b1=time()
s2=[]
for _ in range(0,100000000):        #8.870333671569824
    s2.append(7)
b2=time()
print(b2-b1)


#------------------------------------------------------------------------------------------------------C-5.24
from time import time
def remove(t, x):
    a = [7] * t
    b = [None] * int(t / 2)
    b.extend([7] * int(t / 2))
    q = t
    tc = t

    s = time()
    if x == 1:
        for _ in range(0, len(a)):   # removed element from last, tail
            tc = tc - 1              # 1.0944366455078125e-06
            a[tc] == 7
            a.remove(7)

    elif x == 2:
        for _ in range(int(t / 2)):  # removed element from mid, and subsequent n/2                    ############
            b.remove(7)              # and elements on right are shifted leftwards
    elif x == 3:                     # 7.679338455200196e-05

        for _ in range(t):     # removed element from start, head
            a.remove(7)        # 1.3178825378417968e-06

    e = time()
    return (e - s) / q


print(remove(10000, 1))
print(remove(10000, 2))
print(remove(10000, 3))



#------------------------------------------------------------------------------------------------------C-5.25
from time import time
x1=time()
a=[1,2,7,3,7,4,5,7,6,7,8,9,7,0,7,2,3,7,4,7,6,7]*1000       #here count takes O(n) time, and loop             #########
b=a.count(7)                                                #takes O(n) time hence it takes extra
for _ in range(0,b):                                        #time for count(), hence slower.
        a.remove(7)                                          #1.3468880653381348
x2=time()
print(x2-x1)


x3=time()
a=[1,2,7,3,7,4,5,7,6,7,8,9,7,0,7,2,3,7,4,7,6,7]*1000       #0.024965763092041016 , fastest
for i in range(0,len(a)):
       try:
        if a[i]==7:
            a.pop(i)
       except:
           break
x4=time()
print(x4-x3)


#------------------------------------------------------------------------------------------------------C-5.26
a=[1,2,3,4,6,7,8,9,0,7,7,7,7,10,11,12,13,14,15,16,17]
b=[(a.count(x),x) for x in a]
b=max(b)
print(b)


#------------------------------------------------------------------------------------------------------C-5.27
import math
l=[4,7,35,19,9,13,24,7]
s=len(l)
n=int(math.log2(s))+1
check=1
for _ in range(0,n):
        check=check*2
for i in l:
    if i>check:
        print(i)


#------------------------------------------------------------------------------------------------------C-5.29
a=[[1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14]]
b=[[2,"a"],[4,"b"],[6,"c"],[14,"d"],[10,"e"]]
for i in range(0,len(a)):
    for j in range(0,len(b)):
        if a[i][1]==b[j][0]:
            c=a[i]
            d=b[j][1]
            c.append(d)
            print(c)


#------------------------------------------------------------------------------------------------------C-5.30
import random
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
n=4
l=[]
for i in range(0,n):
    l.append(a[i*5:(i+1)*5])
random.shuffle(l)

print(l)
g=len(l[0])
n=len(l)
p=0
pl=[0]
pl[0]=l[0]
for _ in range(0,len(l)):
 for i in range(1,n):
  print("--------------------00",pl)
  for j in range(0,len(pl)):
    if pl[j]!=0:
      if l[i][g-1]+1==pl[j][0]:
         print("----------------------------------------------002",pl)
         if pl.count(l[i])==0:
          pl.insert(j,l[i])
          print("----------------------------------------------003",pl)
      elif l[i][0]==pl[j][g-1]+1:
         print("----------------------------------------------004",pl)
         if pl.count(l[i])==0:
           pl.insert(j+1,l[i])
           print("----------------------------------------------005",pl)

print("result :",pl)


#------------------------------------------------------------------------------------------------------C-5.31
def funky(i,a,n,l):
 if l==i:
   return 0
 else:
  sum=0
  for k in range(0,n):
    sum=sum+a[i][k]
  i=i+1
  sum=sum+funky(i,a,n,l)
  return sum

a=[[2,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]*4
print(a)
n=4
l=len(a)
print(funky(0,a,4,l))



#------------------------------------------------------------------------------------------------------P-5.32
a=[[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]]
b=[[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]]
c=[]
for i in range(0,len(a)):
    m=[]
    for j in range(0,len(a[0])):
        t=[]
        for k in range(0,len(a[0][0])):
            t.append(a[i][j][k]+b[i][j][k])
        m.append(t)
    c.append(m)
print(c)



#------------------------------------------------------------------------------------------------------P-5.33
class matrix():
    def __init__(self,a):
      self._a=a

    def __add__(self,b):
        self._b=b
        c=[]
        for i in range(0,len(self._b)):
            m=[]
            for j in range(0,len(self._b[0])):
                m.append(self._a[i][j]+self._b[i][j])
            c.append(m)
        return c

    def __mul__(self,e):
        self._e=e
        qq=[]
        for i in range(0,len(self._a)):               #elements in a, (total rows) for multiplying with        #########
         x = 0                                        #the columns of b
         m = []
         for _ in range(0, len(self._e[0])):          #elements b,(total columns) for multiplying with
            c=0                                       #the columns of a
            su=0
            for j in range(0,len(self._e)):           #elements in a(1 row) or, elements of b(total rows in 1 column )
                c=self._a[i][j]*self._e[j][x]
                print("---------------whys :",i,j,"-",j,x,"---",self._a[i][j],self._e[j][x])
                su=su+c
            m.append(su)
            print("------",qq,su)
            x=x+1
         qq.append(m)
        return qq

a=[[1,2,3],[4,5,6]]
b=[[1,2],[4,5],[7,8]]
Q=matrix(a)
#print(Q+b)
print(Q*b)

a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[1,2,3],[4,5,6],[7,8,9]]
Q=matrix(a)
#print(Q+b)
print(Q*b)



#------------------------------------------------------------------------------------------------P-5.34, P-5.35, P-5.36
class CaesarCipher:
    def __init__(self,shift):
        self._shift=shift

    def encrypt(self,message):
        return self._transform(message,self._shift)

    def decrypt(self,secret):
        return self._transform(secret,-self._shift)

    def _transform(self,original,disp):
        msg=list(original)
        print("message",msg)
        for k in range(len(msg)):
                if msg[k]==" ":
                    pass
                elif disp>0:
                     if ord(msg[k])+disp>90:
                        msg[k]=chr(64+(ord(msg[k])+disp)%90)
                     else:
                       msg[k]=chr(ord(msg[k])+disp)
                elif disp<0:

                     if ord(msg[k])+disp<65:
                         msg[k]=chr(90-(64-(ord(msg[k])+disp)))
                     else:
                        msg[k]=chr(ord(msg[k])+disp)
        return "".join(msg)

if __name__=="__main__":
    cipher=CaesarCipher(3)
    message="END OF TIMES ZABC"
    coded=cipher.encrypt(message)
    print("Secret ",coded)
    answer=cipher.decrypt(coded)
    print("Message",answer)



#------------------------------------------------------------------------------------------------P-5.37
import random
class CaesarCipher:
    def __init__(self,shift):
        self._shift=shift
        enc=[None]*26
        for i in range(26):
           enc[i]=chr(65+i)
        random.shuffle(enc)
        self._tortoise=enc
        print(enc)
        self._solution={}

    def encrypt(self,message):
        return self._transform(message,1)

    def decrypt(self,secret):
        return self._transform(secret,0)

    def _transform(self,original,c):
        msg=list(original)
        for k in range(len(msg)):
            if c==1:
                if msg[k]==" ":
                    pass
                else:
                    msg[k] = self._tortoise[k]
            elif c==0:
                if msg[k]==" ":
                    pass
                else:
                    msg[k]=self._solution.get(msg[k])
        self.lang(original,msg)
        return "".join(msg)

    def lang(self,org,msg):
        cc={}
        for i in range(0,len(msg)):
            cc={msg[i]:org[i]}
            self._solution.update(cc)
        print(self._solution)


if __name__=="__main__":
    cipher=CaesarCipher(3)
    message="END OF TIMES ZABC"
    print(message)
    coded=cipher.encrypt(message)
    print("Secret ",coded)
    answer=cipher.decrypt(coded)
    print("Message",answer)













