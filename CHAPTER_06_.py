'''
a=[]
with open("C:\\Users\\HP\\Pictures\\GODZILLA_.txt" , 'r+') as fd:                                                ######
    for line in fd.readlines():
     a.append(line)
'''

b=[1,2,3,4]
a=[None]*len(b)*2         # 8 times                                                                              #######
print(a)

a=-2%4
print(a)

for i in range(3,0,-1):    # for reverse give step                                                               #######
    print("---",i)

a=[1,2,3,4]
a.reverse()                                                                                                      #######
print(a)

a=[1,2,3,4]
print(a[-1])      # goddammit negative                                                                           #######

a="\\gh"
for i in a:
    if i=="\\":      # not for a="\gh"
        print(i)

class amazing:
    def __init__(self):
        self._a=9
    def aa1(self,):
        self.aa2()     # we to use self. for methods , not for functions                                     #########
    def aa2(self,):
        pass


a=[[1,7]]
i=0
for j in range(0,4):     # adding value afterwards, even though it was not                                  #########
    print(j,a[i])        # there before executing the loop and value added
    i+=1                 # simultaneously
    a.append([0,0])
    if i==9:
        exit
'''0[1, 7]
   1[0, 0]
   2[0, 0]
   3[0, 0]'''


a=9; b=4; c=7
if b<c<a:               # multiple statement check                                                           ########
    print(c)



#---------------------------------------------------------------------------R-6.3, C-6.18
def transfer(S,T=[]):
    T=[None]*len(S)             # either this way                                                            ########
    for i in range(0,len(S)):
        T[i]=S[len(S)-i-1]
    return T
S=[1,2,3,7,9,11]
#T=[None]*len(S)                # or this way
print(transfer(S))



#---------------------------------------------------------------------------R-6.4
def recursive(S,i):
    if i==0:
        print(S.pop(0))
        quit                 # exit the function
    else:
        print(S.pop(i))
        i-=1
        recursive(S,i)
S=[1,2,4,7,9,13]
i=len(S)-1
recursive(S,i)
print("exit works")          # print works after exit, but not for exit()                                    ########



#-------------------------------------------------------------------------R-6.5
def reversey(S):
        t=[None]*len(S)
        for i in range(0,len(S)):
            t[i]=S[i]
        for j in range(0,len(S)):
            S[j]=t[len(t)-j-1]
        return S

S=[1,2,4,7,9,13]
print(reversey(S))



#-------------------------------------------------------------------------R-6.6
def brackets(eq):
    a=[]
    for i in range(0,len(eq)):
        if eq[i]=="[" or eq[i]=="{" or eq[i]=="(" or eq[i]=="]" or eq[i]=="}" or eq[i]==")":
           a.append(eq[i])
    print("-----a",a)
    for i in range(0,len(a)):
        b = ""
        for j in range(0,len(a)):
          if a[i]!=None:
           if b=="":
              if a[i]=="[":
                  b="]"
              elif a[i]=="{":
                  b="}"
              elif a[i]=="(":
                  b=")"
           elif b==a[j]:
             if (j-i)%2!=0:
               a[i]=None
               a[a.index(b)]=None
             else:
                print("failed",a)
                return
    print("success",a)

s="[1+{3+4}2-((6-4/7)]"
brackets(s)
print("fffffffffff")
s="[1+{3+4}2-([]6-4/7)]"
brackets(s)



#-------------------------------------------------------------------------R-6.11
from collections import deque
queue = deque('name')                                                                                         #########
queue = deque(['name',7])
print(queue)



#-------------------------------------------------------------------------R-6.13,R-6.14
class dequeueue:
    def __init__(self,D):
        self._deque=D
        self._queue=[None]*len(D)*2
        self._stack=[None]*len(D)*2
        self._start=int(len(D)/2)
        self.deque()
        self.stack()

    def deque(self):
        c=0
        for i in range(self._start,len(self._deque)+self._start):
            self._queue[i]=self._deque[c]
            c+=1
        print(self._queue)

    def stack(self):
        for i in range(0,len(self._deque)):
            self._stack[i]=self._deque[i]
        print(self._stack)

d=[1,2,3,4,5,6,7,8]
D=dequeueue(d)



#-------------------------------------------------------------------------C-6.16, C-6.17
class stacky:
    def __init__(self,m):
        self._data=[]
        self._maxlen=m

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        if len(self._data)==0:
            return True
        return False

    def push(self,val):
        if len(self._data)+1<=self._maxlen:
             self._data.append(val)
             print("---------------------")
        else:
            print("Max capacity reached")

    def top(self):
        if self.is_empty():                       # take care of self , ()                                     ########
            print("TypeError : empty stack")
            return
        return self._data[-1]                      # get the last item of list by this or by                   ########
                                                   # using  self._data[len(self._data)-1]
    def pop(self):
        if self.is_empty():
            print("TypeError : empty stack")
        a=self._data.pop()
        print("---------xxxxxxx",self._data)
        return a

S=stacky(3)
S.push(1)
S.push(4)
print(S.top())                                    # take case of ()                                           #########
print(S.pop(),", element pop occurs")
S.push(9)
S.push(16)
S.push(17)



#-------------------------------------------------------------------------C-6.19
def tags(input):
    c1=""
    c2=[]
    for i in range(0,len(input)):
        if input[i]=="<":
          for j in range(i,len(input)):
             if input[j]!=" " and input[j]!=">" :
               c1=c1+input[j]
             else:
                 break
        elif input[i]==">":
            c1=c1+input[i]
            if c1[1] !="/":
                c2.append(c1)
                c1=""
            elif c1[1]=="/":
                c1=c1.replace("/","")              # here use str.replace(old_symbols, new_symbols) and it     ########
                c2.append(c1)                      # replaces all the instances and returns changed copy
                c1=""
    a=[(c2.count(x),x) for x in c2]
    for i in range(0,len(a)):
        if a[i][0]%2!=0:
            print("non-matching tags")
            return
    print("tags",c2)
    print("count",a)
    print("matching tags")

i="k<mm > ljj </mm >kjj <mm01> <//mm01 > "
tags(i)



#--------------------------------------------------------------------------------------C-6.20
import itertools                                                                                   #####################
print([x for x in itertools.permutations([1,2,3,4])])

import itertools                                                                                   #####################
print([x for x in itertools.combinations([1,2,3,4],3)])
# [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]


'''
a[start:stop:step]

x[:]                # [x[0],   x[1],          ..., x[-1]    ]
x[low:]             # [x[low], x[low+1],      ..., x[-1]    ]
x[:high]            # [x[0],   x[1],          ..., x[high-1]]
x[low:high]         # [x[low], x[low+1],      ..., x[high-1]]
x[::stride]         # [x[0],   x[stride],     ..., x[-1]    ]
x[low::stride]      # [x[low], x[low+stride], ..., x[-1]    ]
x[:high:stride]     # [x[0],   x[stride],     ..., x[high-1]]
x[low:high:stride]  # [x[low], x[low+stride], ..., x[high-1]]

x[::-stride]        # [x[-1],   x[-1-stride],   ..., x[0]    ]
x[high::-stride]    # [x[high], x[high-stride], ..., x[0]    ]
x[:low:-stride]     # [x[-1],   x[-1-stride],   ..., x[low+1]]
x[high:low:-stride] # [x[high], x[high-stride], ..., x[low+1]]
'''

#explicit means that it is expressly stated and made obvious -- overt/obvious/manual.
#implicit means that it is not obvious, it is implied. hidden/assumed/automatic.

#The following code is an in-place permutation of a given list, implemented as a generator.
# Since it only returns references to the list, the list should not be modified outside the
# . The solution is non-recursive, so uses low memory. Work well also with multiple copies
# of elements in the input list.
class stack_permutaion_non_recursive:
      def __init__(self,A):
          self._list=A

      def enqueue(self,value):          # objects(lists) not copied when passed to the function hence they show last
          self._list.append(value[:])   # altered value The problem is in your list reference in enqueue, you have
                                        # n! references to the same list. Every time you change one element, you are
                                        # changing all of them. Hence [:] used to create copy of value and then pass
                                        # to append, rather than to directly append value that passes it by reference.
      def __repr__(self):
          return str(self._list)

def operations():
       a=[3,4,2,1]
       c=[3,4,2,1]
       l=[None]*len(a)
       i=1;j=0
       D=stack_permutaion_non_recursive([])
       D.enqueue(a)
       while True:
           if i%2!=0:                      # LOGIC:
               a[3],a[2]=a[2],a[3]         # 43(21)     43(12)              , interchange index 2,3
               D.enqueue(a)                # 4(3)1(2)   42(13)   42(31)     , interchange index 1,3 then 2,3
               i+=1                        # 4(2)3(1)   41(23)   41(32)     , interchange index 1,3 then 2,3
           elif i%2==0:                    # 3...
               a[3],a[1]=a[1],a[3]         # 2...                         (same logic for all)
               D.enqueue(a)                # 1...
               i+=1
           if i%6==0:
               print(j)
                                        # for j=3 then check(1) if j==4 interchanging(2) values then values (3)generated
               j += 1                   # above then j=4 then check if j==4 , fail hence stop. If order was 1,3,4 then
               if j == 4:               # error as j=4 but interchanging only up to 3.(COMMON MISTAKE).
                 print(D.__repr__())           # repr returns value hence print used
                 return
               a[0], a[j] = a[j], a[0]         # simultaneous assignment syntax

operations()

'''NOTE:
sometimes we can't see the entire pathway_mind_map/steps of the algorithm in mind so see the general trend, recursion , 
patterns and make code accordingly to those recursions. you will only need minor tweaks here and there but the majority
of the code will be completed ツ '''


#---------------------------------------------------------------------------------------C-6.21
'''
This is the old-school way to do it. It’s elegant nonetheless. It uses the incredible property
that all numbers from 1 up to 2ⁿ are distinct. If we would write those numbers in base 2…those
1 and 0 bits could be interpreted like:

Consider the number 5 in binary 101b. >> is just a shift (or equivalently, division by 2n) and
& 1 masks out all but the least significant bit.

(101b >> 0) & 1 = (101b & 1) = 1
(101b >> 1) & 1 = ( 10b & 1) = 0
(101b >> 2) & 1 = (  1b & 1) = 1

So once wen understand how the bit-extraction works, we need to understand why bit-extraction is
equivalent to subset inclusion: Here's how we map from binary numbers 0-7 to subsets of {A,B,C}

0: 0 0 0   => {     }
1: 0 0 1   => {    A}
2: 0 1 0   => {  B  }
3: 0 1 1   => {  B A}
4: 1 0 0   => {C    }
5: 1 0 1   => {C   A}
6: 1 1 0   => {C B  }
7: 1 1 1   => {C B A}

And clearly we have listed all subsets.
'''

def get_subsets(fullset):
  listrep = list(fullset)
  subsets = []
  for i in range(2**len(listrep)):
    subset = []
    for k in range(len(listrep)):
      if i & 1<<k:
        subset.append(listrep[k])
    subsets.append(subset)
  return subsets

subsets = get_subsets(set([1,2,3]))
print(subsets)
print(len(subsets))



#---------------------------------------------------------------------------------------C-6.22
n="((5+2)*(8-3))/(4)"
num=["1","2","3","4","5","6","7","8","9","0"]
sym=["+","-",'/',"*"]
x=[]
s=""
for i in range(0,len(n)):
    if n[i]==")":
        x.append(s)
        s=""
    elif n[i] in num:
        x.append(n[i])
    elif n[i] in sym:
        s=s+n[i]
print(x)
x="".join([str(v) for v in x])    # take care of () brackets of join ,
print(x)                          # and [] of list comprehension



#---------------------------------------------------------------------------------------C-6.28
class ArrayQueue:
    MAXLEN=6

    def __init__(self):
        self._data=[None]*ArrayQueue.MAXLEN
        self._size=0
        self._front=int(ArrayQueue.MAXLEN/2)

    def __len__(self):
        return self._size

    def _is_empty(self):
        return self._size==0                                                                       ####################

    def _first(self):
        if self._size==0:
            print("Queue is empty")
            return
        return self._data[self._front]

    def _dequeue(self):
        if self._size==0:
            print("Queue is empty")
            return
        d=self._data[self._front]
        self._data[self._front]=None
        self._front=(self._front+1)%(len(self._data))
        self._size-=1
        return d


    def _enqueue(self,value):
        self._size+=1
        if self._size>ArrayQueue.MAXLEN:
            print("Space exceeded")
            return
        p=(self._front+self._size)%(len(self._data))
        self._data[p]=value

    def __repr__(self):
        print(self._data)

O=ArrayQueue()
O._enqueue(7)
O._enqueue(8)
O._enqueue(9)
O._enqueue(6)
O._enqueue(5)
O._enqueue(2)
O.__repr__()
O._enqueue(3)
O.__repr__()



#---------------------------------------------------------------------------------------C-6.29
class ArrayQueue:
    MAXLEN=6

    def __init__(self):
        self._data=[None]*ArrayQueue.MAXLEN
        self._size=0
        self._front=int(ArrayQueue.MAXLEN/2)

    def __len__(self):
        return self._size

    def _is_empty(self):
        return self._size==0

    def _first(self):
        if self._size==0:
            print("Queue is empty")
            return
        return self._data[self._front]

    def _dequeue(self):
        if self._size==0:
            print("Queue is empty")
            return
        d=self._data[self._front]
        self._data[self._front]=None
        self._front=(self._front+1)%(len(self._data))
        self._size-=1
        return d


    def _enqueue(self,value):
        self._size+=1
        if self._size>ArrayQueue.MAXLEN:
            print("Space exceeded")
            return
        p=(self._front+self._size)%(len(self._data))
        self._data[p]=value

    def __repr__(self):
        print(self._data)

    def _rotate(self):
        a=self._data[(self._front+1)%len(self._data)]
        self._data[(self._front+1)%len(self._data)]=None
        p=(self._front+self._size+1) % (len(self._data))
        self._data[p]=a
        self._front=(self._front+1)%len(self._data)



O=ArrayQueue()
O._enqueue(7)
O._enqueue(8)
O._enqueue(9)
O._enqueue(6)
O.__repr__()

O._rotate()
O._rotate()
O._rotate()
O.__repr__()



#---------------------------------------------------------------------------------------P-6.32
class Deque:
    def __init__(self):
        self._data=[None]*5
        self._size=0
        self._front=2
        self._back=1
        self._back_cy=1
        self._c=1

    def __len__(self):
        return self._size

    def _is_empty(self):
        return self._size==0

    def _first(self):
        if self._size==0:
            print("Queue is empty")
            return
        return self._data[self._front]

    def _dequeue(self):
        if self._size==0:
            print("Queue is empty")
            return
        d=self._data[self._front]
        self._data[self._front]=None
        self._front=(self._front+1)%(len(self._data))
        self._size-=1
        return d

    def _ed_dequeue(self):
        if self._size==0:
            print("Queue is empty")
            return
        if self._back>=self._back_cy:
            d = self._data[self._back_cy]
            self._data[self._back_cy]=None  # NEGATIVE INDEXING DUDE 3,2,1,0 and now from len(n) -1,-2,-3 ##############
            self._back_cy -= 1
        return d


    def _enqueue(self,value):
        self._size+=1
        if self._size==len(self._data):
            self._resize()
        p=(self._front+self._size)%(len(self._data))
        self._data[p]=value


    def _st_enqueue(self,value):
        self._size+=1
        if self._size==len(self._data):
            self._st_resize()
        if self._back>-1:
         self._data[self._back]=value
         self._back-=1
        else:
            self._back=len(self._data)-1
            self._data[self._back]=value
            self._back-=1

    def _st_resize(self):
        a=[None]*len(self._data)*2
        j=0
        c=0
        if  self._back<=self._back_cy:
            for i in range(self._back_cy,self._back-1,-1):
                a[c]=self._data[self._back_cy-c]
                c+=1
        elif self._back>self._back_cy:
            for i in range(self._back,len(self._data)):
               a[c]=self._data[i]
               c+=1
            for i in range(0,self._back_cy+1):
                a[c]=self._data[i]
                c+=1

        self._back=len(self._data)-self._size
        self._back_cy=len(self._data)-1
        print("-------",self._back_cy,self._back)
        self._data=a


    def _resize(self):
        a=[None]*len(self._data)*2
        j=0
        for i in range(self._front+1,(self._front+1+self._size)):
            b=i%len(self._data)
            a[j]=self._data[b]
            j+=1
        self._data=a
        self._front=-1


    def __repr__(self):
        print(self._data)



Q=Deque()
Q._st_enqueue(5)
Q._st_enqueue(6)
Q._st_enqueue(7)
Q._st_enqueue(8)
Q.__repr__()
Q._st_enqueue(9)
Q.__repr__()
Q._st_enqueue(10)
Q.__repr__()
Q._ed_dequeue()
Q.__repr__()
Q._ed_dequeue()
Q.__repr__()
Q._ed_dequeue()
Q.__repr__()
Q._ed_dequeue()
Q.__repr__()
Q._ed_dequeue()
Q.__repr__()
Q._ed_dequeue()
Q.__repr__()



#---------------------------------------------------------------------------------------P-6.34
a="52+48-*4/"
b=["+","-","/","*"]
x=[""]*len(a)
k=0
e1=0;e2=0
for i in range(0,len(a)):
    if a[i] in b:
        for j in range(1,i,2):
         if a[i-j] not in b:
            print(a[i],i-1)
            x.insert(i-j,a[i])
            break
         else:
            pass
    else:
        k+=1
        if k%2!=0:
         x[i]="("+a[i]
         e1+=1
        else:
         x[i]=a[i]+")"
         e2+=1
if e2!=e1:
    x.append(")")
print(x)
x="".join([v for v in x])
x=eval(x)                      # eval converts string mathematical equation to a directly executable equation   ########
print(x)                       # and evaluates the output of the equation















