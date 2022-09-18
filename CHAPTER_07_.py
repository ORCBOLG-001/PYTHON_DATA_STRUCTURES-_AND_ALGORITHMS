class a:
    def b(self,a,b=8):       # method overloading in python , do it all in one function.                      #########
        print(a,b)              # python does not support method overloading by default.
                                # The problem with method overloading in Python is that
                                # we may overload the methods but can only use the latest
k=a()                           # defined method.
k.b(4,7)
k.b(9)

#--------------------------------------------------------------------------------------------
class funimation:
   def __reversed__(self):                                                                                    ##########
      n=[1,2,3,4,5,6,7]
      i=6
      while i >-1:
        yield n[i]             # yield logic
        i-=1

x=funimation()

a=reversed(x)                  # reversed logic
print(next(a))
print(next(a))
print(next(a))

#---------------------------------------------------------------------------------------------

#if a not in X and a not in Y:               #syntax                                                           ########
#---------------------------------------------------------------------------------------------
if 9>None:                                   #does not work                                                     ########
  print("yup")
#---------------------------------------------------------------------------------------------
v="c"+"b"
print(v)
'''cb'''

''' m = 1234                                 #number split by into individual elements by index                ########
    m = list(str(m))                         #split does not work for integer
    print(m)          '''
#---------------------------------------------------------------------------------------------
class abc:
    __slots__ = "bee"
    def __init__(self,j):
        self.bee=j
        print("89",self.bee)
    def figgy(self,r):
        print("9")

a=abc(0)
x=a                                                       # object (a) is passed by reference                  ########
x.bee=1101                                                # to variable (x) any change causes
print(a.bee,x.bee)                                        # both to change


#---------------------------------------------------------------------------------------------------------R-7.1 , R-7.25
class LinkedList:                                                                          #############################
    class _Node:
        print("---------01")                       # here 01 executed, then 03, then 02, 02
        __slots__ = "_element", "_next"            # name must be same as variable inside init

        def __init__(self, element, next):
            self._element = element
            self._next = next
            print("---------02")

    def __init__(self):
        print("---------03")
        self._header = self._Node(None, None)           # self._trailer = self._Node(None, None)
        self._trailer = self._Node("bu0i", None)        # in a way it represents a = class_name()
        self._header._next = self._trailer              # self._Node() is same as calling an instance variable
        self.size=1                                     # self._trailer used to create unique variable each time

    def insert_between(self,value,predecessor):
        newest=self._Node(value,predecessor)
        predecessor._next=newest
        newest._next=self._trailer
        self.size+=1
        print(newest)

    def printy(self):
        a=None;b=None
        for i in range(0,self.size):
            if i==0:                           # loop used because CLASSICAL first_value has to be
                a = self._header._next         # defined for i==0 and last_value+1 for i=len(n)-1
                b = a._element                 # and no value at that len(n) location
                print(b,end="-")
            else:
                a = a._next
                b = a._element
                print(b,end="-")

    def second_last(self):
        a = self._header._next
        b = a._element
        for _ in range(0,self.size-2):
            a=a._next
            b=a._element
        return b


c = LinkedList()                               # all this occurs for a single object , not multiple
c.insert_between(4,c._header)
e1=c._header._next
c.insert_between(5,e1)
e2=e1._next
c.insert_between(6,e2)
e3=e2._next
c.insert_between(7,e3)
c.printy()
print("\n",c.second_last())

'''
---------01
---------03
---------02
---------02
---------02
<__main__.LinkedList._Node object at 0x000002845E0BC820>
---------02
<__main__.LinkedList._Node object at 0x000002845E0BC7C0>
---------02
<__main__.LinkedList._Node object at 0x000002845E0BC790>
---------02
<__main__.LinkedList._Node object at 0x000002845E0BC760>
4-5-6-7-bu0i-
  7
'''


#-------------------------------------------------------------------------------------------------R-7.2 , R-7.9 , C-7.26
class LinkedList:
    class _Node:
        __slots__ = "_element", "_next"

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._header = self._Node(None, None)
        self._trailer = self._Node("last", None)
        self._header._next = self._trailer
        self.size=1

    def insert_between(self,value,predecessor):
        newest=self._Node(value,predecessor)
        predecessor._next=newest
        newest._next=self._trailer
        self.size+=1

    def printy(self):
        a=None;b=None
        for i in range(0,self.size):
            if i==0:
                a = self._header._next
                b = a._element
                print(b,end="-")
            else:
                a = a._next
                b = a._element
                print(b,end="-")

    def combine(self,self_1,self_2):
           val=None;a=None;b=None
           for i in range(0,self_1.size-1):
               if i == 0:
                   a = self._header
                   b = self_1._header._next
                   val = b._element
                   self.insert_between(val,a)
               else:
                   a=a._next
                   b=b._next
                   val=b._element
                   self.insert_between(val,a)


           for i in range(0,self_2.size-1):
               if i == 0:
                   a = a._next
                   b = self_2._header._next
                   val = b._element
                   self.insert_between(val,a)
               else:
                   a=a._next
                   b=b._next
                   val=b._element
                   self.insert_between(val,a)


c = LinkedList()
c.insert_between(4,c._header)
e1=c._header._next
c.insert_between(5,e1)
e2=e1._next
c.insert_between(6,e2)
e3=e2._next
c.insert_between(7,e3)
c.printy()

print("\n")
d = LinkedList()
d.insert_between(8,d._header)
e1=d._header._next
d.insert_between(9,e1)
e2=e1._next
d.insert_between(10,e2)
e3=e2._next
d.insert_between(11,e3)
d.printy()

print("\n")
e=LinkedList()
e.combine(c,d)
print("\n-")
e.printy()



#------------------------------------------------------------------------------------------------------------------R-7.3
class LinkedList:
    class _Node:
        __slots__ = "_element", "_next"

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._header = self._Node(None, None)
        self._trailer = self._Node(None, None)
        self._header._next = self._trailer
        self.size=1

    def insert_between(self,value,predecessor):
        newest=self._Node(value,predecessor)
        predecessor._next=newest
        newest._next=self._trailer
        self.size+=1

    def printy(self):
        a=None;b=None
        for i in range(0,self.size):
            if i==0:
                a = self._header._next
                b = a._element
                print(b,end="-")
            else:
                a = a._next
                b = a._element
                print(b,end="-")

    def count(self):
        a = self._header._next
        t=0
        for i in range(0,self.size):
          if a._element!=None:
              t+=1
              a=a._next
        return t



c = LinkedList()
c.insert_between(4,c._header)
e1=c._header._next
c.insert_between(5,e1)
e2=e1._next
c.insert_between(6,e2)
e3=e2._next
c.insert_between(7,e3)
c.printy()
print("\n",c.count())



#-----------------------------------------------------------------------------------------------------------R-7.4, R-7.5
class LinkedList:
    class _Node:
        __slots__ = "_element", "_next"

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._header = self._Node(None, None)
        self._trailer = self._Node(None, None)
        self._header._next = self._trailer
        self.size=1

    def insert_between(self,value,predecessor):
        newest=self._Node(value,predecessor)
        predecessor._next=newest
        newest._next=self._trailer
        self.size+=1

    def printy(self):
        a=None;b=None
        for i in range(0,self.size):
            if i==0:
                a = self._header._next
                b = a._element
                print(b,end="-")
            else:
                a = a._next
                b = a._element
                print(b,end="-")

    def swap(self1,self2):                                         # can use names instead of self            #########
        a=self1._header._next
        b=self2._header._next
        for i in range(0,self1.size):
            a._element , b._element = b._element , a._element
            a=a._next
            b=b._next


c = LinkedList()
c.insert_between(4,c._header)
e1=c._header._next
c.insert_between(5,e1)
e2=e1._next
c.insert_between(6,e2)
e3=e2._next
c.insert_between(7,e3)
c.printy()


print("\n")
d = LinkedList()
d.insert_between(8,d._header)
e1=d._header._next
d.insert_between(9,e1)
e2=e1._next
d.insert_between(10,e2)
e3=e2._next
d.insert_between(11,e3)
d.printy()


c.swap(d)


print("\n")
c.printy()
print("\n")
d.printy()



#------------------------------------------------------------------------------------------------------------------R-7.6
class LinkedList:
    class _Node:
        __slots__ = "_element", "_next"

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._header = self._Node(None, None)
        self._trailer = self._Node(None, None)
        self._header._next = self._trailer
        self.size=1

    def insert_between(self,value,predecessor):
        newest=self._Node(value,predecessor)
        predecessor._next=newest
        newest._next=self._trailer
        self.size+=1
        return predecessor._next

    def printy(self):
        a=None;b=None
        for i in range(0,self.size):
            if i==0:
                a = self._header._next
                b = a._element
                print(b,end="-")
            else:
                a = a._next
                b = a._element
                print(b,end="-")

    def reference(self,x,y):
        a=self._header._next
        for i in range(0,self.size):
            if a==x:                             # directly check reference location,                         #########
                print("x is present",x)          # no need to convert into str
            elif a==y:
                print("y is present",y)
            a=a._next


c = LinkedList()
c.insert_between(4,c._header)
e1=c._header._next
c.insert_between(5,e1)
e2=e1._next                                       # store reference location                                 ##########
x=c.insert_between(6,e2)
e3=e2._next
y=c.insert_between(7,e3)                          # store reference location
c.printy()

print("\n")
c.reference(x,y)




#------------------------------------------------------------------------------------------------------------------R-7.7
class LinkedList:
    class _Node:
        __slots__ = "_element", "_next"

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._header = self._Node(None, None)
        self._trailer = self._Node(None, None)
        self._header._next = self._trailer
        self.size=1

    def insert_between(self,value,predecessor):
        newest=self._Node(value,predecessor)
        predecessor._next=newest
        newest._next=self._trailer
        self.size+=1

    def printy(self):
        a=None;b=None
        for i in range(0,self.size):
            if i==0:
                a = self._header._next
                b = a._element
                print(b,end="-")
            else:
                a = a._next
                b = a._element
                print(b,end="-")

    def roatatey(self,location):
        a=self._header._next
        b=copy.copy(self._header._next)                # here copy used , else both a, b would point to same    ########
        location._next=a                               # location, and any change in a causes b to change
        a._next=self._trailer                          # and we would be unable to set new self._header
        self._header=b


import copy
c = LinkedList()
c.insert_between(4,c._header)
e1=c._header._next
c.insert_between(5,e1)
e2=e1._next
c.insert_between(6,e2)
e3=e2._next
c.insert_between(7,e3)
c.printy()

print("\n")
e4=e3._next
c.roatatey(e4)                        # send NEXT from where you want to rotate it, by                         #########
c.printy()                            # inserting element from index 0(most left hand-side)
                                      # to index right-side of NEXT
print("\n")
e5=e4._next
c.roatatey(e5)
c.printy()




#------------------------------------------------------------------------------------------------------------------R-7.8
class LinkedList:
    class _Node:
        __slots__ = "_element", "_next"

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._header = self._Node(None, None)
        self._trailer = self._Node(None, None)
        self._header._next = self._trailer
        self.size=1

    def insert_between(self,value,predecessor):
        newest=self._Node(value,predecessor)
        predecessor._next=newest
        newest._next=self._trailer
        self.size+=1

    def printy(self):
        a=None;b=None
        for i in range(0,self.size):
            if i==0:
                a = self._header._next
                b = a._element
                print(b,end="-")
            else:
                a = a._next
                b = a._element
                print(b,end="-")

    def middle(self):
        c=math.ceil((self.size-1)/2)                     # math.ceil for upper value                          #########
        a=self._header._next                             # math.floor for lower value
        for i in range(1,self.size):
             if c==i:
                 print(a._element)
                 return
             a=a._next


import math
c = LinkedList()
c.insert_between(4,c._header)
e1=c._header._next
c.insert_between(5,e1)
e2=e1._next
c.insert_between(6,e2)
e3=e2._next
c.insert_between(7,e3)
e4=e3._next
c.insert_between(8,e4)
c.printy()

print()
c.middle()






#--------------------------------------------------------------------------------------------------------R-7.11 , R-7.12
class LinkedList:
    print("--------------00")
    class _Node:
        __slots__ = "_element", "_next"

        def __init__(self, element, next):
            print("--------------01")
            self._element = element
            self._next = next

    def __init__(self):
        print("--------------02")
        self._header = self._Node(None, None)
        self._trailer = self._Node(None, None)
        self._header._next = self._trailer
        self.size=1

    def insert_between(self,value,predecessor):
        print("--------------06")
        newest=self._Node(value,predecessor)
        predecessor._next=newest
        newest._next=self._trailer
        self.size+=1

    def printy(self):
        a=None;b=None
        for i in range(0,self.size):
            if i==0:
                a = self._header._next
                b = a._element
                print(b,end="-")
            else:
                a = a._next
                b = a._element
                print(b,end="-")
        print("\n")

    def max(self):
        a=self._header._next
        m=0
        for i in range(0,self.size):
            if a._element>m:
                m=a._element
            else:
                a=a._next
        return m


class PositionalList(LinkedList):
    print("--------------03")

    class Position:
        def __init__(self, container, node):
            print("--------------04")
            self._container = container
            self._node = node

        def element(self):
            print("--------------05")
            return self._node._element

    def _make_position(self,node):
        print("--------------06")
        return self.Position(self,node)

    def _insertion(self,e,predecessor):
        print("--------------07")
        node=super().insert_between(e,predecessor)


c = PositionalList()
print("---------------------------------------")
c._insertion(9,c._header)
print("-----------------------")
e1=c._header._next
c._insertion(5,e1)
print("-----------------------")
e2=e1._next
c._insertion(6,e2)
print("-----------------------")
e3=e2._next
c._insertion(7,e3)
print("-----------------------")
e4=e3._next
c._insertion(8,e4)
print("-----------------------")
c.printy()

z=c._make_position(e3)
print(z)
print(z.element())


print(c.max())                             # here max called through object of class PositionalList            #########
print(PositionalList.max(c))               # here since object is passed, hence we call function of
                                           # PositionalList class manually





#------------------------------------------------------------------------------------------------WORKING_POSITIONAL_LIST
class LinkedList:                                                              #########################################
    print("--------------00")

    class _Node:
        print("--------------09")
        __slots__ = "_element", "_next"

        def __init__(self, element, next):
            print("--------------01")
            self._element = element
            self._next = next

    # note that """ """ must be indented
    """                                                     EXECUTION ORDER-                                  
                                                            --------------00
                                                            --------------09
                                                            --------------03
                                                            --------------10
                                                            --------------02
                                                            --------------01
                                                            --------------01
                                                            ---------------------------------------
                  In the first situation, the PositionalList is extending the class LinkedClass and since you are not  
                  redefining the special method named __init__() in PositionalList, it gets inherited from LinkedClass.
    """

    def __init__(self):
        print("--------------02")
        self._header = self._Node(None, None)
        self._trailer = self._Node(None, None)
        self._header._next = self._trailer
        self.size = 1

    def insert_between(self, value, predecessor):
        print("--------------06")
        newest = self._Node(value, predecessor)
        predecessor._next = newest
        newest._next = self._trailer
        self.size += 1
        return newest

    def printy(self):
        a = None;
        b = None
        for i in range(0, self.size):
            if i == 0:
                a = self._header._next
                b = a._element
                print(b, end="-")
            else:
                a = a._next
                b = a._element
                print(b, end="-")
        print("\n")


class PositionalList(LinkedList):
    print("--------------03")

    class Position:
        print("--------------10")

        def __init__(self, container, node):
            print("--------------04")
            self._container = container  # Memory location of variable c in memory, does not change
                                         # for different inputs for object c. It only changes when
                                         # we make a new object of class PositionalList.

            self._node = node  # Basically store individual node of parent class

        def element(self, _node="_node"):
            print("--------------05")
            return self._node._element  # get element of individual node that is stored here from parent class,
                                        # (reference is stored) and then value got from parent class

    def _make_position(self, node):
        print("--------------06")
        return self.Position(self, node)

    def _insertion(self, e, predecessor):
        print("--------------07")
        node = super().insert_between(e, predecessor)  # how super is invoked
        return self._make_position(node)



c = PositionalList()
print("---------------------------------------")
c._insertion(9, c._header)

e1 = c._header._next
c._insertion(5, e1)
e2 = e1._next
c._insertion(6, e2)
e3 = e2._next
c._insertion(7, e3)
e4 = e3._next
c._insertion(8, e4)

c.printy()

print(hex(id(c)))  # memory location of variable c in memory

z = c._make_position(e3)
z = c._make_position(e2)
z = c._make_position(e1)
z = c._make_position(e4)

print("---------", z.element())
print("---------", z.element(e1))

c.printy()  # unchanged



#--------------------------------------------------------------------------------------------------------R-7.13 , R-7.14
class LinkedList:

    class _Node:
        __slots__ = "_element", "_next"

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._header = self._Node(None, None)
        self._trailer = self._Node(None, None)
        self._header._next = self._trailer
        self.size = 1

    def insert_between(self, value, predecessor):
        newest = self._Node(value, predecessor)
        predecessor._next = newest
        newest._next = self._trailer
        self.size += 1
        return newest

    def value_of_node(self,node):
        return node._element


class PositionalList(LinkedList):
    class Position:

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def torture(self,node):
            return self.value_of_node(node)

    def find(self, node, value):
        v = PositionalList.Position.torture(self, node)
        if v == value:
            print("SUCCESS", v, value)
        return v == value

    def _make_position(self, node):
        return self.Position(self, node)

    def _insertion(self, e, predecessor):
        node = super().insert_between(e, predecessor)  #
        return self._make_position(node)



c = PositionalList()

c._insertion(9, c._header)
e1 = c._header._next
c._insertion(5, e1)
e2 = e1._next
c._insertion(6, e2)
e3 = e2._next
c._insertion(7, e3)
e4 = e3._next
c._insertion(8, e4)

z = c._make_position(e3)
z = c._make_position(e2)
z = c._make_position(e1)
z = c._make_position(e4)

value=7
for i in(e1,e2,e3,e4):                                                                               ###################
    r=c.find(i,value)       # c.find(i,value) used because class object is c, but i=c._header._next , and already has c.
    if r==True:             # Hence, c is sent(self) but not used above and all the functions are modified due to this.
        break

        "OR"


f=[e1, e2, e3, e4]
i=0
value=7
def recursion(f,i,value):
        r = c.find(f[i], value)
        if r == True:
            return
        else:
            i+=1
            recursion(f,i,value)

recursion(f,i,value)



#-----------------------------------------------------------------------------------------------------------------R-7.15
class LinkedList:

    class _Node:
        __slots__ = "_element", "_next"

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._header = self._Node(None, None)
        self._trailer = self._Node(None, None)
        self._header._next = self._trailer
        self.size = 1

    def insert_between(self, value, predecessor):
        newest = self._Node(value, predecessor)
        predecessor._next = newest
        newest._next = self._trailer
        self.size += 1
        return newest

    def value_of_node(self,node):
        return node._element


class PositionalList(LinkedList):
    class Position:

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def torture(self,node):
            return self.value_of_node(node)

    def find(self, node):
        return PositionalList.Position.torture(self, node)

    def _make_position(self, node):
        return self.Position(self, node)

    def _insertion(self, e, predecessor):
        node = super().insert_between(e, predecessor)  #
        return self._make_position(node)

    def __reversed__(self):
        f = [e1, e2, e3, e4]
        i=3
        while i>-1:
            s=f[i]
            yield self.find(s)
            i-=1



c = PositionalList()

c._insertion(9, c._header)
e1 = c._header._next
c._insertion(5, e1)
e2 = e1._next
c._insertion(6, e2)
e3 = e2._next
c._insertion(7, e3)
e4 = e3._next
c._insertion(8, e4)

z = c._make_position(e3)
z = c._make_position(e2)
z = c._make_position(e1)
z = c._make_position(e4)


print("----")
a=reversed(c)
print(next(a))
print(next(a))
print(next(a))
print(next(a))





#--------------------------------------------------------------------------------------R-7.18 , R-7.20 , R-7.22 , C-7.24
class a:
    class b:
        __slots__ = "_element","_next"
        def __init__(self,value,node):
           self._element=value
           self._next=node

    def __init__(self):
        self.head=None
        self.size=0

    def insert(self,value):
        self.head=self.b(value,self.head)
        self.size+=1

    def data(self):
        a=self.head
        for i in range(0,self.size):
            print(a._element)
            a=a._next

    def acesss(self,check):
        a = self.head
        b=  self.head
        for i in range(0, self.size):
            if a._element==check:
                    self.shift_top(a,b,check)
                    return
            else:
             b=a
             a = a._next

    def shift_top(self,a,b,check):             # we are changing the ._next of different nodes and            ##########
        if b!=self.head:                       # rearranging them without creating new node
            b._next=a._next
            c=self.head
            self.head=a
            self.head._next=c

        else:
            self.head._next=a._next
            a._next=self.head
            self.head=a                        # don't forget to reset header                                 ##########

    def clear(self):
        self.head=None
        self.size=0



y=a()
y.insert(1)
y.insert(2)
y.insert(3)
y.insert(4)
y.insert(5)
y.data()
print("\n")
y.acesss(2)
y.insert(6)
y.data()


print("\n")
z=a()
z.insert(1)
z.insert(2)
z.insert(3)
z.insert(4)
z.data()
print("\n")
z.acesss(3)
z.acesss(2)
z.acesss(1)
z.data()


print("\n----")
z.clear()
z.data()





#-----------------------------------------------------------------------------------------------------------------R-7.23
class a:
    class b:
        __slots__ = "_element","_next","_count"       # add extra instance variable _count                  ############
        def __init__(self,value,node):
           self._element=value
           self._next=node
           self._count=0

    def __init__(self):
        self.head=None
        self.size=0

    def insert(self,value):
        self.head=self.b(value,self.head)
        self.size+=1

    def data(self):
        a=self.head
        for i in range(0,self.size):
            print(a._element)
            a=a._next

    def acesss(self,check):
        a = self.head
        b=  self.head
        for i in range(0, self.size):
            if a._element==check:
                    a._count+=1
                    self.shift_top(a,b,check)
                    return
            else:
             b=a
             a = a._next

    def shift_top(self,a,b,check):             # we are changing the ._next of different nodes and            ##########
        if b!=self.head:                       # rearranging them without creating new node
            b._next=a._next
            c=self.head
            self.head=a
            self.head._next=c

        else:
            self.head._next=a._next
            a._next=self.head
            self.head=a                        # don't forget to reset header                                 ##########

    def clear(self):
        self.head=None
        self.size=0


    def data_county(self):
       a = self.head
       for i in range(0, self.size):
           print(a._element,":",a._count)
           a = a._next


    def clear_county(self):
        a = self.head
        for i in range(0, self.size):
            a._count=0
            a = a._next


y=a()
y.insert(1)
y.insert(2)
y.insert(3)
y.insert(4)
y.insert(5)
y.data()
print("\n")
y.acesss(2)
y.insert(6)
y.data()


print("\n")
z=a()
z.insert(1)
z.insert(2)
z.insert(3)
z.insert(4)
z.data()
print("\n")
z.acesss(3)
z.acesss(2)
z.acesss(1)
z.data()


print("\n counts")
y.data_county()
print("\n")
z.data_county()


print("\n")
y.clear_county()
z.clear_county()
y.data_county()
print("\n")
z.data_county()






#-----------------------------------------------------------------------------------------------------------------C-7.27
class Node:
    def __init__(self, element, next=None):
        self._element = element
        self._next = next


    def prepend(self, element):
        return Node(element, self)

    def __iter__(self):
        #print("/2")
        yield self._element
        #print("/3")
        if self._next is not None:
            #print("/4")
            yield from self._next

    def __repr__(self):                                                                        #########################
        #print("/1")
        return "->".join(map(repr, self))

a = Node(4).prepend(3).prepend(2).prepend(1)
print(a)

'''
/1
/2
/3
/4
/2
/3
/4
/2
/3
/4
/2
/3
1->2->3->4
'''




#-----------------------------------------------------------------------------------------------------------------C-7.28
class a:
    class b:
        __slots__ = "_element","_next"
        def __init__(self,value,node):
           self._element=value
           self._next=node

    def __init__(self):
        self.head=None
        self.size=0

    def insert(self,value):
        self.head=self.b(value,self.head)
        self.size+=1

    def data(self):
        a=self.head
        for i in range(0,self.size):
            print(a._element)
            a=a._next



    '''
    a=9
    b=a
    a=7
    print(b,a)   # 9,7 logic at page 52
    '''
    def reversal(self,h,p=0):                                                                            ###############
          if p==self.size-1:
                return
          else:
            p += 1
            a = self.head
            for _ in range(0,p):
              a=a._next
            h._next=a._next
            a._next=self.head
            self.head=a
            print("---------",self.head._element,a._next._element,a._next._next._element,a._next._next._next._element)
            self.reversal(h,p)



y=a()
y.insert(1)
y.insert(2)
y.insert(3)
y.insert(4)
y.data()
print("\n")
y.reversal(y.head)
y.data()





#-----------------------------------------------------------------------------------------------------------------C-7.30
class a:
    class b:
        __slots__ = "_element","_next"
        def __init__(self,value,node):
           self._element=value
           self._next=node

    def __init__(self,limit):
        self.head=None
        self.size=0
        self.limit=limit
        print(self.limit,"--------")


    def insert(self,value):
        self.size += 1
        if self.size > self.limit:
            self.leaky_stack()
        self.head=self.b(value,self.head)


    def data(self):
        a=self.head
        for i in range(0,self.size):
            print(a._element)
            a=a._next

    def leaky_stack(self):
            a=self.head
            for i in range(1,self.size):
                if i!=self.size-2:
                    a=a._next
                else:
                    a._next = None     # to remove node just change ._next of previous to None         #################
                    self.size -= 1
                    return




y=a(4)
y.insert(1)
y.insert(2)
y.insert(3)
y.insert(4)
y.data()

print("\n")
y.insert(5)
y.data()




#--------------------------------------------------------------------------------------------------------C-7.31 , C-7.32
class a:
    class b:
        __slots__ = "_next","_element"
        def __init__(self,element,node):
            self._element=element
            self._next=node

    def __init__(self):
        self.head=None
        self.size=0

    def insert(self,value):
        self.head=self.b(value,self.head)
        self.size+=1

    def data(self):
        a=self.head
        for i in range(0,self.size):
            print(a._element)
            a=a._next


class c(a):
    def put(self,value):
        self.insert(value)

    def show(self):
        self.data()

    def top(self):
        print(self.head._element)

    def last(self):
        a=self.head
        for i in range(0,self.size):
            if i==self.size-1:
                print(a._element)
            else:
               a=a._next

    def rotate(self):
        a=self.head
        b=None
        for i in range(0,self.size):
            if i==self.size-1:
               a._next=self.head
               b._next=None
               self.head=a
            else:
               b=a
               a=a._next



    def delete(self,value):
        a=self.head
        b=None
        for i in range(0,self.size):
            if a._element==value and i==0:
                print("----------00")
                self.head=self.head._next
                self.size -= 1
                return
            elif a._element==value and i==self.size-1:
                print("----------01")
                b._next=None
                self.size -= 1
                return
            elif a._element==value:
                b._next=a._next
                self.size -= 1
                return
            else:
               b=a
               a=a._next
        self.size+=1
        print("value not in linked list")


y=c()
y.insert(6)
y.insert(7)
y.insert(8)
y.insert(9)
y.insert(10)
y.data()

print("\n")
y.top()
y.last()

print("\n")
y.delete(10)
y.data()

print("\n")
y.delete(6)
y.data()

print("\n")
y.delete(8)
y.data()

print("\n")
y.insert(8)
y.insert(9)
y.insert(10)
y.data()


print("\n")
y.rotate()
y.data()



#-----------------------------------------------------------------------------------------------------------------C-7.33
class a:
    class b:
        __slots__ = '_next', "_element", "_prev"
        def __init__(self,element,prev,next):
            self._element=element
            self._next=next
            self._prev=prev

    def __init__(self):
        self.head=self.b(None,None,None)
        self.tail=self.b(None,None,None)
        self.head._next=self.tail
        self.tail._prev=self.head
        self.size=0

    def head_intial(self):
        return self.head

    def tail_intial(self):
        return self.tail

    def insert(self,value,before,after):
        newest=self.b(value,before,after)
        before._next=newest
        after._prev=newest
        self.size+=1
        return newest

    def data(self):
        a=self.head._next
        for i in range(0,self.size):
            print(a._element)
            a=a._next
        print("")

        b = self.tail._prev
        for i in range(0, self.size):
            print(b._element)
            b = b._prev


y=a()
after=y.tail_intial()
before=y.head_intial()
c=y.insert(6,before,after)
d=y.insert(7,c,after)
e=y.insert(8,d,after)
f=y.insert(9,e,after)
y.data()


#-----------------------------------------------------------------------------------------------------------------C-7.34
class a:
    class b:
        __slots__ = '_next', "_element", "_prev"
        def __init__(self,element,prev,next):
            self._element=element
            self._next=next                    #previous head, hence self.head will have next
            self._prev=prev                    #next tail, hence self.tail will have previous

    def __init__(self):
        self.head=self.b(None,None,None)
        self.tail=self.b(None,None,None)
        self.head._next=self.tail
        self.tail._prev=self.head
        self.size=0

    def head_intial(self):
        return self.head

    def tail_intial(self):
        return self.tail

    def insert(self,value,before,after):
        newest=self.b(value,before,after)
        before._next=newest
        after._prev=newest
        self.size+=1
        return newest

    def data(self,a="",b=""):
        if a=="":
         a=self.head._next
        print("head to tail")
        for i in range(0,self.size):
            print(a._element)
            a=a._next

        print("\ntail to head")
        if b=="":
            b=self.tail._prev
        for i in range(0, self.size):
            print(b._element)
            b = b._prev
        print("\n")


    def swap(self,a,b):                  # Here head has ->next and tail has <-previous
                                         # e.g.
        s1=self.head                     # [NONE]Head <->L1<->L2<->L3<->L4<->L5<-> Tail[NONE]
        s2=self.tail                     # let us swap L2, and L5

                                            #1. Changing the corresponding previous elements reference-
        a._prev._next=b                         # here L2.prev=L1 then L1._next point to L5
        b._prev._next=a                         # here L5.prev=L4 then L4.next points to L2

        k = a._prev                         #2. Changing the respective nodes reference to previous nodes:
        a._prev=b._prev                         # here L2.prev points to L5.prev that is L4
        b._prev=k                               # here L5.prev points to L2.prev that is L1

                           #----------------------------------------------------------------------------
        b._next._prev=a                     # repeat same for this for next
        a._next._prev=b

        e=b._next
        b._next=a._next
        a._next=e

        return s1._next,s2._prev


y=a()
after=y.tail_intial()
before=y.head_intial()
c=y.insert(6,before,after)
d=y.insert(7,c,after)
e=y.insert(8,d,after)
f=y.insert(9,e,after)
y.data()
print("-----------------------")
f,g=y.swap(d,e)
y.data(f,g)




#-----------------------------------------------------------------------------------------------------------------C-7.35
class a:
    class b:
        __slots__ = '_next', "_element", "_prev"
        def __init__(self,element,prev,next):
            self._element=element
            self._next=next
            self._prev=prev

    class c:
        def iterator(self):
            a=self.head._next
            for i in range(0,self.size):
                yield a._element
                a=a._next



    def __init__(self):
        self.head=self.b(None,None,None)
        self.tail=self.b(None,None,None)
        self.head._next=self.tail
        self.tail._prev=self.head
        self.size=0

    def head_intial(self):
        return self.head

    def tail_intial(self):
        return self.tail

    def insert(self,value,before,after):
        newest=self.b(value,before,after)
        before._next=newest
        after._prev=newest
        self.size+=1
        return newest


y=a()
after=y.tail_intial()
before=y.head_intial()
c=y.insert(6,before,after)
d=y.insert(7,c,after)
e=y.insert(8,d,after)
f=y.insert(9,e,after)

n=y.c.iterator(y)            # how to get value iterator from nested iterator class          ###########################
for i in n:
 print(i)


'''
To print the message given to yield will have to iterate the generator object as shown in the example below:
def testy():
    yield "welcome bro"


output = testy()
for i in output:
    print(i)                'welcome bro'
'''





#-----------------------------------------------------------------------------------------------------------------C-7.37
class a:
    class b:
        __slots__ = '_next', "_element", "_prev"
        def __init__(self,element,prev,next):
            self._element=element
            self._next=next
            self._prev=prev

    def __init__(self):
        self.head=self.b(None,None,None)
        self.tail=self.b(None,None,None)
        self.head._next=self.tail
        self.tail._prev=self.head
        self.size=0

    def head_intial(self):
        return self.head

    def tail_intial(self):
        return self.tail

    def insert(self,value,before,after):
        newest=self.b(value,before,after)
        before._next=newest
        after._prev=newest
        self.size+=1
        return newest

    def data(self,a="",b=""):
        if a=="":
         a=self.head._next
        print("head to tail")
        for i in range(0,self.size):
            print(a._element)
            a=a._next

        print("\ntail to head")
        if b=="":
            b=self.tail._prev
        for i in range(0, self.size):
            print(b._element)
            b = b._prev
        print("\n")

    def sum_of_2(self,value):
        a=self.head
        for i in range(0,self.size):
            b = self.head._next
            a=a._next
            for j in range(0,self.size):
                if b._element+a._element==value and a!=b:
                    print("sum of",a._element,b._element)
                    return
                else:
                    b=b._next
        print("no such pair exists")
        return



y=a()
after=y.tail_intial()
before=y.head_intial()
c=y.insert(6,before,after)
d=y.insert(7,c,after)
e=y.insert(8,d,after)
f=y.insert(9,e,after)
y.data()

y.sum_of_2(15)
y.sum_of_2(120)





#-----------------------------------------------------------------------------------------------------------------C-7.38
class a:
    class b:
        __slots__ = '_next', "_element", "_prev"
        def __init__(self,element,prev,next):
            self._element=element
            self._next=next
            self._prev=prev

    def __init__(self):
        self.head=self.b(None,None,None)
        self.tail=self.b(None,None,None)
        self.head._next=self.tail
        self.tail._prev=self.head
        self.size=0

    def head_intial(self):
        return self.head

    def tail_intial(self):
        return self.tail

    def insert(self,value,before,after):
        newest=self.b(value,before,after)
        before._next=newest
        after._prev=newest
        self.size+=1
        return newest

    def data(self,a="",b=""):
        if a=="":
         a=self.head._next
        print("head to tail")
        for i in range(0,self.size):
            print(a._element)
            a=a._next

        print("\ntail to head")
        if b=="":
            b=self.tail._prev
        for i in range(0, self.size):
            print(b._element)
            b = b._prev
        print("")


    def bubble_sort(self):
        print("--------------01",self.size)
        for i in range(0,(self.size-1)*(self.size-1)):            # bubble sort                            #############
            a=self.head
            b=self.head._next
            a=a._next
            b=b._next
            for j in range(0,self.size-1):
                if b._element<a._element:
                    self.swap(b,a)
                    a = a._next
                    b = b._next
                else:
                    a=a._next
                    b=b._next


    def swap(self,a,b):

        a._prev._next=b
        b._prev._next=a

        k = a._prev
        a._prev=b._prev
        b._prev=k


        b._next._prev=a
        a._next._prev=b

        e=b._next
        b._next=a._next
        a._next=e



y=a()
after=y.tail_intial()
before=y.head_intial()
c=y.insert(6,before,after)
d=y.insert(9,c,after)
e=y.insert(8,d,after)
f=y.insert(7,e,after)
g=y.insert(5,f,after)
y.data()
print("-----------------------")


y.bubble_sort()
y.data()




#-----------------------------------------------------------------------------------------------------------------C-7.39
class a:
    class b:
        __slots__ = '_next', "_element", "_prev"
        def __init__(self,element,prev,next):
            self._element=element
            self._next=next
            self._prev=prev

    def __init__(self):
        self.head=self.b(None,None,None)
        self.tail=self.b(None,None,None)
        self.head._next=self.tail
        self.tail._prev=self.head
        self.size=0

    def head_intial(self):
        return self.head

    def tail_intial(self):
        return self.tail

    def insert(self,value,before,after):
        newest=self.b(value,before,after)
        before._next=newest
        after._prev=newest
        self.size+=1
        return newest

    def delete(self,value,before,after):
        before._next=after
        after._prev=before
        self.size-=1
        print(value,"deleted!")


    def data(self,a="",b=""):
        if a=="":
         a=self.head._next
        print("head to tail")
        for i in range(0,self.size):
            print(a._element)
            a=a._next

        print("\ntail to head")
        if b=="":
            b=self.tail._prev
        for i in range(0, self.size):
            print(b._element)
            b = b._prev
        print("")


    def swap(self,a,b):

        a._prev._next=b
        b._prev._next=a

        k = a._prev
        a._prev=b._prev
        b._prev=k


        b._next._prev=a
        a._next._prev=b

        e=b._next
        b._next=a._next
        a._next=e



y=a()
after=y.tail_intial()
before=y.head_intial()
c=y.insert(6,before,after)
d=y.insert(7,c,after)
e=y.insert(8,d,after)
f=y.insert(9,e,after)
g=y.insert(10,f,after)
y.data()
print("-----------------------")

y.delete(9,e,g)
y.data()





#-----------------------------------------------------------------------------------------------------------------C-7.40
class a:
    class b:
        __slots__ = '_next', "_element", "_prev"
        def __init__(self,element,prev,next):
            self._element=element
            self._next=next
            self._prev=prev

    class c:
        __slots__ = '_nxt', "_ele","_ct"
        def __init__(self,element,next):
            print('---------')
            self._ele=element
            self._nxt=next
            self._ct=0

    def __init__(self):
        self.head=self.b(None,None,None)
        self.tail=self.b(None,None,None)
        self.head._next=self.tail
        self.tail._prev=self.head
        self.size=0
        self.top=self.c(None,None)

    def move_to_front(self,val,size):
        self.top=self.c(val,self.top)
        v=self.top
        l=[]
        toll=0
        for i in range(0,self.size+1):
            if toll==size:
                v._nxt=None
                return
            if v._ele not in l:
              print(v._ele )
              l.append(v._ele)
              toll+=1
              v = v._nxt
            else:
              v = v._nxt


    def head_intial(self):
        return self.head

    def tail_intial(self):
        return self.tail

    def insert(self,value,before,after):
        newest=self.b(value,before,after)
        before._next=newest
        after._prev=newest
        self.size+=1
        self.top = self.c(value,self.top)
        return newest

    def data(self,a="",b=""):
        if a=="":
         a=self.head._next
        print("head to tail")
        for i in range(0,self.size):
            print(a._element)
            a=a._next

        print("\ntail to head")
        if b=="":
            b=self.tail._prev
        for i in range(0, self.size):
            print(b._element)
            b = b._prev
        print("")


y=a()
after=y.tail_intial()
before=y.head_intial()
c=y.insert(6,before,after)
d=y.insert(7,c,after)
e=y.insert(8,d,after)
f=y.insert(9,e,after)
g=y.insert(10,f,after)
y.data()

print("-----------------------")
y.move_to_front(8,4)




#-----------------------------------------------------------------------------------------------------------------C-7.41
class a:
    class b:
        __slots__ = "_val1","_val2","_val3","_next"
        def __init__(self,value1,value2,next,value3):
            self._val1=value1
            self._val2=value2
            self._val3=value3
            self._next=next

    def __init__(self):
        self.head=self.b(None,None,None,None)
        self.size=0


    def insert(self,value1,value2,value3=0):
        self.head=self.b(value1,value2,self.head,value3)
        self.size+=1

    def printy(self):
        a=self.head
        for i in range(0,self.size):
            print(a._val1,a._val2,a._val3)
            a=a._next
        print("")

    def natural_join(self,self2,self3):
        a2=self2.head
        b3=self3.head
        for i in range(0,self2.size):
            b3 = self3.head
            for j in range(0,self3.size):
                if a2._val2==b3._val1:
                    self.head=self.b(a2._val1, a2._val2, self.head, b3._val2)
                    self.size+=1
                    b3=b3._next
                else:
                    b3=b3._next
            a2=a2._next



x=a()
x.insert(1,2)
x.insert(3,4)
x.printy()

y=a()
y.insert(2,10)
y.insert(4,11)
y.printy()

print("applying natural join")
z=a()
z.natural_join(x,y)
z.printy()


#-----------------------------------------------------------------------------------------------------------------C-7.43
class a:
    class b:
        __slots__ = "_next","_element"
        def __init__(self,element,node):
            self._element=element
            self._next=node

    def __init__(self):
        self.head=None
        self.size=0

    def insert(self,value):
        self.head=self.b(value,self.head)
        self.size+=1

    def data(self):
        a=self.head
        for i in range(0,self.size):
            print(a._element)
            a=a._next

    def mid_point(self):
        a=self.head
        for i in range(0,int(self.size/2)):
            a=a._next
        return a

    def shuffle(self,self2,mid):
        a=self.head
        b=mid
        for i in range(0, int(self.size / 2)):
            self2.insert(a._element)
            self2.insert(b._element)
            a=a._next
            b=b._next


y=a()
y.insert(1)
y.insert(2)
y.insert(3)
y.insert(4)
y.insert(5)
y.insert(6)
y.insert(7)
y.insert(9)
y.data()

mid=y.mid_point()

print("\n--------",mid._element)                                                                        ################
z=a()                                                   # create object_2 then send it to object_1 method's and
y.shuffle(z,mid)                                        # add solutions of object_1 nodes into object_2 nodes.
z.data()




#-----------------------------------------------------------------------------------------------------------------P-7.44
class a:
    class b:
        __slots__ = "_element","_next","_previous"
        def __init__(self,e,n,p):
            self._element=e
            self._next=n
            self._previous=p

    def __init__(self):
        self.head=self.b(None,None,None)
        self.tail=self.b(None,None,None)
        self.tail._previous=self.head
        self.head._next=self.tail
        self.size=0

    def insert(self,value,next,previous):
        new_node=self.b(value,next,previous)
        next._previous=new_node
        previous._next=new_node
        self.size+=1
        return new_node

    def delete(self,node):
        node._previous._next=node._next
        node._next._previous=node._previous
        node=None
        self.size-=1

    def display(self):
        print("from head to tail:")
        a=self.head
        #print(a._element)
        for i in range(0,self.size):
            a=a._previous
            print(a._element)

        print("from tail to head:")
        b=self.tail
        for i in range(0,self.size):
            b=b._next
            print(b._element)


    def location(self,choice,cursor,value=None):
        if choice=="left" and cursor._previous!=self.tail:
            cursor=cursor._previous
        elif choice=="right" and cursor._next!=self.head:
            cursor=cursor._next
        elif choice=="insert":
             self.insert(value,cursor._next,cursor)
        elif choice=="delete" and cursor!=self.head:
             self.delete(cursor._next)
        return cursor



y=a()
k0=y.head
k1=y.tail
k2=y.insert(11,k0,k1)
k3=y.insert(12,k0,k2)
k4=y.insert(13,k0,k3)
y.display()

print("\n---------CURSOR:")

print("----------left-")
c1=y.location("left",k0)
print(c1._element)
c2=y.location("left",c1)
print(c2._element)
c3=y.location("left",c2)
print(c3._element)
c4=y.location("left",c3)
print(c4._element)

print("----------right-")
c1=y.location("right",c4)
print(c1._element)
c2=y.location("right",c1)
print(c2._element)
c3=y.location("right",c2)
print(c3._element)

print("----------insert-")
c1=y.location("insert",c3,5)
y.display()
c2=y.location("insert",c1,6)
y.display()

print("----------delete-")
c1=y.location("delete",c2)
y.display()
c2=y.location("delete",c1)
y.display()



#-----------------------------------------------------------------------------------------------------------------P-7.46
class a:
    def __init__(self):
        self.list=[]
        self.size=0

    def insert(self,value,index):
        self.list.append([value,index])
        self.size+=1
        return self.size

    def insert_between(self,value,index):
        a=[]
        for i in range(0,self.size+1):
            if i<index:
                a.append(self.list[i])
            elif i == index:
                a.append([value,i])
                self.size+=1
            elif i>index:
                c=self.list[i-1][0]
                a.append([c,i])
        self.list=a

    def data(self):
        for i in range(0,self.size):
            print(self.list[i])

y=a()
y.insert(11,0)
y.insert(12,1)
y.insert(13,2)
y.insert(14,3)
y.insert(15,4)
y.data()

print("---------------")
y.insert_between(16,2)
y.data()




#-----------------------------------------------------------------------------------------------------------------P-7.47
class a:
    class b:
        __slots__ = "element","next","previous"
        def __init__(self,element,next,previous):
            self.element=element
            self.next=next
            self.previous=previous

    def __init__(self):
        self.head1=self.b(None,None,None) #heart
        self.head2=self.b(None,None,None) #club
        self.head3=self.b(None,None,None) #spade
        self.head4=self.b(None,None,None) #diamond
        self.tail5=self.b(None,None,None)
        self.head1.next=self.head2
        self.head2.next=self.head3
        self.head3.next=self.head4
        self.head4.next=self.tail5
        self.tail5.previous=self.head4
        self.head4.previous=self.head3
        self.head3.previous=self.head2
        self.head2.previous=self.head1
        self.size1=0
        self.size2=0
        self.size3=0
        self.size4=0


    def insert(self,value,type,before,after):
            new=self.b(value,before,after)
            after.next=new
            before.previous=new
            if type=="hearts":
             self.size1+=1
            elif type=="clubs":
             self.size2+=1
            elif type=="spades":
             self.size3+=1
            elif type=="diamonds":
             self.size4+=1
            return new

    def data(self,type):
        c=None
        a=None
        print("playing",type,end=" : ")
        if type == "hearts":
            c=self.size1
            a=self.head1
        elif type == "clubs":
            c=self.size2
            a=self.head2
        elif type == "spades":
            c=self.size3
            a=self.head3
        elif type == "diamonds":
            c=self.size4
            a=self.head4
        for i in range(0,c):
            a=a.previous
            if i != c-1:
             print(a.element,end=" , ")
            else:
             print(a.element)

    def play(self,type):
        if type == "hearts":
          if self.head1.previous!=self.head2:
            self.size1-=1
            self.head1.previous.previous.next=self.head1
            self.head1.previous=self.head1.previous.previous
          else:
              type="clubs"
        if type == "clubs":
          if self.head2.previous!=self.head3:
            self.size2-=1
            self.head2.previous.previous.next=self.head2
            self.head2.previous=self.head2.previous.previous
          else:
              type="spades"
        if type == "spades":
          if self.head3.previous!=self.head4:
            self.size3-=1
            self.head3.previous.previous.next=self.head3
            self.head3.previous=self.head3.previous.previous
          else:
              type="diamonds"
        if type == "diamonds":
          if self.head4.previous != self.tail5:
            self.size4-=1
            self.head4.previous.previous.next=self.head4
            self.head4.previous=self.head4.previous.previous
          else:
              print("\n------------------------------------------------OUT OF CARDS")

    def full_data(self):
        print("-----------------------------------all cards")
        a=("hearts","clubs","spades","diamonds")
        for i in a:
            self.data(i)
        print("-------------------------------------------")


y=a()
e1=y.head1
e2=y.head2
e3=y.insert(1,"hearts",e1,e2)
e4=y.insert(2,"hearts",e1,e3)
e5=y.insert(3,"hearts",e1,e4)
y.data("hearts")

f1=y.head2
f2=y.head3
f3=y.insert(4,"clubs",f1,f2)
f4=y.insert(5,"clubs",f1,f3)
f5=y.insert(6,"clubs",f1,f4)
y.data("clubs")

g1=y.head3
g2=y.head4
g3=y.insert(7,"spades",g1,g2)
g4=y.insert(8,"spades",g1,g3)
g5=y.insert(9,"spades",g1,g4)
y.data("spades")


h1=y.head4
h2=y.tail5
h3=y.insert(10,"diamonds",h1,h2)
h4=y.insert(11,"diamonds",h1,h3)
h5=y.insert(12,"diamonds",h1,h4)
y.data("diamonds")


y.full_data()


print("----------------------")
y.play("hearts")
y.data("hearts")
y.play("clubs")
y.data("clubs")
y.play("spades")
y.data("spades")
y.play("diamonds")
y.data("diamonds")

print("---------------------")
y.play("hearts")
y.data("hearts")
y.play("hearts")
y.data("hearts")
y.play("hearts")
y.data("clubs")
y.play("hearts")
y.play("hearts")
y.data("clubs")
y.data("spades")
y.play("spades")
y.play("spades")
y.data("spades")
y.data("diamonds")
y.play("spades")
y.data("diamonds")
y.play("spades")





