#------------------------------------------------R-2.4
class Flower():
    def __init__(self,flower,petals,price):
        self.flower=flower
        self.petals=petals
        self.price=price
    def show(self):
        print(self.flower)
        print(self.petals)
        print(self.price)
    def alter(self,flower,petals,price):
        self.flower=flower
        self.petals=petals
        self.price=price

a=input("enter flower name")
b=int(input("enter no of petals"))
c=float(input("enter price of flower"))
o=Flower(a,b,c)

while True:
    d=input("1 to change values, 2 to print values, exit to exit")
    if d=="1":
        a = input("enter flower name")
        b = int(input("enter no of petals"))
        c = float(input("enter price of flower"))
        o.alter(a, b, c)
    elif d=="2":
        o.show()
    else:
     exit()

#------------------------------------------------R-2.9 - C-2.25
class Vector:
 def __init__(self, d):
  try:
   iter(d)
   self._cord = d
  except:
   self._cord = [0] * d
  print("iiii",self._cord)

 def __setitem__(self, key, value):
  self._cord[key] = value

 def __getitem__(self, item):
     return self._cord[item]

 def __len__(self):
  return len(self._cord)

 def __sub__(self, size, e):
  vec = [0] * size
  for i in range(0, len(e)):
   vec[i] = self._cord[i] - e[i]
  return vec

 def __neg__(self, vec2):
  for i in range(len(vec2)):
   vec2[i] = -1 * vec2[i]
  return vec2

 def __add__(self, other):
  beta = [0, 0, 0]
  print(beta)
  for i in range(len(other)):
   beta[i] = other[i] + self._cord[i]
  return beta

 def __radd__(self, other):
  beta = Vector(3)
  print("wtwtwtwtw", beta)
  for i in range(len(other)):
   beta[i] = other[i] + self._cord[i]
   print("ffffffff", beta)
  return beta

 def __str__(self):
  return str(self._cord)

 def __eq__(self, other):
     n=True
     for i in range(0, len(other)):
         if other._cord[i] != self._cord[i]:
             n=False
     return n

 def __ne__(self, other):
     return self._cord == other._cord

 def __lt__(self, other):
     for i in range(len(other)):
       if other._cord[i] >= self._cord[i]:
           pass
       else:
           return False
     return True

 def __mul__(self, other):
     try :
         iter(other)
         v=[0]*len(other)
         print("yyyy",v)
         for i in range(len(other)):
             print("tttttt",i)
             try:
              v[i]=self._cord[i]*other._cord[i]
              print("xcxc", v[i])
             except:
                 print("trytry")

                 v[i]=self._cord[i]*other[i]
                 print("funfun",v[i])
         return v
     except:
         v=[0]*len(self)
         for i in range(0,len(self)):
             v[i]=self._cord[i]*other
         return v

     def __iter__(self):
         return self

     def __next__(self):
         v=[0]*len(self)
         for i in range(len(self)):
             v[i]=self._cord[i]
             return v[i]


a = Vector(3)
n = Vector(3)
j = Vector(3)
a.__setitem__(0, 10)
a.__setitem__(1, 10)
a.__setitem__(2, 10)
e = a.__sub__(3, [1, 2, 3])
print(e)
f = a.__neg__([1, 4, 7])
print(f)
print(len(a))

bbb = a + [1, 2, 8]
print(bbb)

b = [3, 2, 1] + a
print("----090---",b)

v=Vector([1,2,4,6])

n.__setitem__(0,2)
print(n!=j)

print("--g--",[7,9,0]+n)
print("--g",n+[7,9,0])

j.__setitem__(0,7)
print("jnjn",n)
print("jnjn",j)
print("---wwwwww--",n*[1,4,2])
print("wwwwww------",n*7)
print("jjjj",n*j)


#------------------------------------------------C-2.26
class SequenceIterator:
    def __init__(self,sequence):
        self._seq=sequence
        self._k=-1
    def __len__(self):
        return len(self._seq)
    def __next__(self):
        self._k +=1
        if self._k < len(self._seq):
            return(self._seq[len(self)-1-self._k])
        else:
            raise StopIteration

    def __iter__(self):
        return self

a=SequenceIterator([1,2,3])
print(next(a))
print(next(a))
print(next(a))

#------------------------------------------------R-2.27
class Range:
    def __init__(self,start,stop=None,step=1):
        if step==0:
            raise ValueError("step cannot be 0")
        if stop is None:
            start,stop = 0,start
        self._length=max(0,(stop-start+step-1)//step)
        self._start=start
        self._step=step

    def __len__(self):
        print("GGGGG")
        return self._length
    def __getitem__(self, k):
        print("&&&&&&")
        if k<0:
            k+=len(self)
        if not 0<=k<self._length:
            print("^^^^^^")
            raise IndexError("out of range")
        print("########")
        return (self._start + k * self._step)

    def __contains__(self, item):
        print("++++++")
        if((self[len(self)-1]-self[0])%self._step)==0 and item <= self[len(self)-1]:
            print("-----")
            return True
        print("!!!!!!!!")
        return False

    def __eq__(self, other):
        if self==other:
            return True
        return False

    def __le__(self, other):
        if self<=other:
            return True
        return False

a=Range(0,11,2)
print(2 in Range(2,10,2))

#------------------------------------------------C-2.28 - C-2.30
class CreditCard:
    def __init__(self, customer, bank, acnt, limit):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 400

    def get_customer(self):
        return self._customer

    def _get_bank(self):
        return self._bank

    def get_account(self):
        return self._account

    def get_limit(self):
        self._limit

    def get_balance(self):
        return self._balance

    def charge(self, price):
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        self._balance -= amount

class PredatoryCreditCard(CreditCard):
    def __init__(self,customer,bank,acnt,limit,apr):
        super().__init__(customer,bank,acnt,limit)
        self._apr=apr
        self._a=0
        #Here a cannot be defined in
    def charge(self,price):
        success=super().charge(price)
        if not success:
            self._balance+=5
        return success

    def minimum_payment(self,v):
        if v==(1/100* self._balance):
            print("Paid minimum payment")
        else:
            v=(1/100* self._balance)+(1/1000* self.get_balance())
            print("Fine: ",v)


    def process_month(self):
        self._a+=1
        if self._balance>0:
          if self._a>10:
           monthly_factor=pow(1+self._apr,1/12)
           self._balance+=monthly_factor-1
          else:
              monthly_factor = pow(1 + self._apr, 1 / 12)
              self._balance += monthly_factor



a=PredatoryCreditCard("ffff","sss","noidea",4000,7)
a.process_month()
print(a._balance)
a.process_month()
print(a._balance)
a.process_month()
print(a._balance)
a.process_month()
print(a._balance)
print("\n")
a.minimum_payment((a._balance/100))
a.minimum_payment((a._balance/99.99))

#------------------------------------------------C-2.31
class Progression:
    def __init__(self,start=0,c=0):
        self._current=start
        self._c=c

    def _advance(self):
        self._current+=self._c

    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer=self._current
            self._advance()
            return answer

    def __iter__(self):
        return self

    def print_progression(self,n):
        print(" ".join(str(next(self)) for j in range(n)))


class extends(Progression):
    def __init__(self,a=2,b=200):
        self._a=a
        self._b=b
        super().__init__(self._a, self._b-self._a)

    def diff(self,n):
        super().print_progression(n)


a = extends(4,20)
a.diff(10)

#------------------------------------------------C-2.32
class Progression:
    def __init__(self,start=0):
        self._current=start

    def _advance(self,x):
        self._current =x

    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer=self._current
            x=self._current**(1/2)
            self._advance(x)
            return answer

    def __iter__(self):
        return self

    def print_progression(self,n):
        print(" ".join(str(next(self)) for j in range(n)))


class extends(Progression):
    def __init__(self,a=65536,n=2):
        self._a=a
        super().__init__(self._a)

    def diff(self,n):
        super().print_progression(n)


a=extends()
a.diff(4)

#----------------------------------------------------------------------------------------------------------P-2.33
class E:
    def __init__(self,seq):
        self._elements=seq

    def endi(self):
     a=0
     b=0
     try:
      for i in self._elements:                                 # here use logic of "+" "-" elements
         if i=="+" or i=="-":
            a=self._elements.index(i)
            break
      for j in range(a+1,len(self._elements)):                # here use logic of index by remaining length
         if self._elements[j]=="+" or self._elements[j]=="-":
            b=j
            break
     except:
         print("\nCOMPILATION ERROR 02")                      # check for invalid values or terms directly without x
         exit()
     self.calculate(a,a+b)

    def calculate(self,start,end):
        j=0
        if start==0 and exit==0:                                        # here check because if a=0,b=0 is same term for
            print("\nCOMPLETION SUCCEESSFUL 01")                        # last element hence check here seperately for it
            exit()
        else:
         for i in range(start+1,end):
            a=self._elements[i]                                          # break into parts , check and combine
            if a=='^':
                j=1
                b=''.join([self._elements[x] for x in range(start,i-1)])
                try:                                                       # try to check if in form like x^2
                 b = int(b) * int(self._elements[i + 1])                   # without number behind x
                 print(self._elements[start],abs(b),end="",sep='')
                except:
                 print(self._elements[i-2],self._elements[i + 1], end="", sep="")
                if self._elements[i+1]=="+" or self._elements[i+1]=="-":
                    print("",end="")
                elif self._elements[i+1]=="1":                                   # seperate into 3 cases for easier calculation
                     print(self._elements[i-1],"^",0,end="",sep="")              # and use sep="" to eliminate default spacing " "
                else :                                                           # for x after number eg. 45x^2 --> x^2
                     print(self._elements[i-1],"^",int(self._elements[i+1])-1,end="",sep="")
                break

            if i==end-1 and j==0:                                                 # check if no x at all just number
              print("+0",end="")
        self._elements=[self._elements[x] for x in range(end,len(self._elements))]
        self.endi()


a=list(input("enter polynomial:\t"))                                # () to break to indidual, [] for combined
a.insert(len(a),"+")                                                # add element "+" at end for final value loop termination above
if a[0] != "-":
    a.insert(0,"+")                                                 # add element "+" at index 0 for loop initiation above
p=E(a)
p.endi()




#------------------------------------------------------------------------------------------------P-2.34
import matplotlib.pyplot as plt
with open("C:\\Users\\HP\\Pictures\\ab.txt","r+") as f:
 a=f.read()
print(a)
a=list(a)
print(a)
w=[]
for i in range(0,len(a)):
 b=ord(a[i])
 if b>64 and b<91 or b>96 and b<123:
  w.append(chr(b))
r=list((a.count(x),x) for x in set(w))
print(r)
z=[]
x=[]
n=[]
for i in range(0,len(r)):
  z.append(r[i][0])
  x.append(r[i][1])
  n.append(i)
plt.xticks(range(len(r)),x)
plt.bar(n,z)
plt.show()

#------------------------------------------------------------------------------------------------P-2.35
class a:
    def __init__(self):
        self._z=[]
        print("-----02")

    def a1(self):
        for i in range(0,11):
            self._z.append(i)
        print("^^^^^  ",end="",sep="")
        return self._z

class a3(a):
    def __init__(self,e):
     print("====03")
     self._z=e
     print(self._z)

    def a4(self):
      if len(self._z) >-1:
        for i in range(0, 11):
            self._z.pop(0)
            print(self._z)


for i in range (0,4):
    print("-----01")
    p=a()                    # pass values from one class ,  its methods to
    e=p.a1()                 # another class , looping them together is
    m=a3(e)                  # possible, and multiple classes interactions
    m.a4()                   # can be created , updated and used.



#------------------------------------------------------------------------------------------------P-2.36 P-2.37
import random
a=["FISH","BEAR","FISH","FISH","BEAR","FISH","FISH","BEAR","NONE","FISH","BEAR","NONE","FISH","FISH","NONE","FISH"]
empty=[]
for i in range(0,len(a)):           # indexes of "NONE"
    if a[i]=="NONE":
        empty.append(i)

for _ in range(0,170):
 value=random.randint(1,len(a)-2)
 shift=random.choice([-1,1])
 print("values - ",value,"-",shift)

 if a[value] != a[value+shift] :                          # Remove dissimilar
    if a[value]=="FISH" and a[value+shift]=="BEAR":
        a[value]="NONE"
        empty.append(value)
        print("AAAA - ", a)
    elif a[value+shift]=="FISH" and a[value]=="BEAR":
        a[value+shift]="N0NE"
        empty.append(value+shift)
        print("AAAA - ",a)
 elif a[value]=="BEAR" or a[value]=="BEAR"  and a[value+shift]=="FISH" or a[value]=="FISH":    # Copy similar
    v = random.choice(empty)
    print("copy - ",v)
    a[v] = a[value]
    empty.remove(v)
    print("XXXX - ",a)





