#figuring out the interactions e.g. stack
#FIFO
class a:
    class b:
        print("--------xx")
        __slots__ = "_e","_next"

        def __init__(self,e,next):
            self._e=e
            self._next=next
            print("-------04  ",self._e,self._next)

    def __init__(self):
        print("-------00")
        self._f=None                                   #intially create a head node

    def insertion(self,e):
        print("--------01")
        self._f=self.b(e,self._f)                      # send value + head and create link to
                                                       # current head to point to a new node
    def element(self):
            print("--------02")
            n=self._f._e                               # top of stack is head of list
            return n

    def deletion(self):
        self._f=self._f._next


x=a()
x.insertion(1)
print(x.element())
print("\n")
x.insertion(2)
print(x.element())
print("\n")
x.deletion()
print(x.element())


'''
--------xx
-------00
--------01
-------04   1 None
--------02
1


--------01
-------04   2 <__main__.a.b object at 0x0000024DEEE19F70>
--------02
2


--------02
1

'''




#-----------------------------------------------------------------------------------------------------------------------
#figuring out the interactions e.g. stack
#FIFO + Inheritance
class a:
    class b:
        print("--------xx")
        __slots__ = "_e","_next"

        def __init__(self,e,next):
            self._e=e
            self._next=next
            print("-------04  ",self._e,self._next)

    def __init__(self):
        print("-------00")
        self._f=None

    def insertion(self,e):
        print("--------01")
        self._f=self.b(e,self._f)

    def element(self):
            print("--------02")
            n=self._f._e
            return n


class c(a):
    def insert(self,e):
        self.insertion(e)

    def value(self):
        return self.element


y=c()
y.insert(4)
print(y.value())

'''
--------xx
-------00
--------01
-------04   4 None
<bound method a.element of <__main__.c object at 0x000001ECBE468F70>>
'''


#-----------------------------------------------------------------------------------------------------------------------
# figuring out the interactions e.g. stack
# FIFO + Inheritance (with class inside class)
class a:
    class b:
        __slots__ = "_e", "_next"

        def __init__(self, e, next):
            self._e = e
            self._next = next

    def __init__(self):
        self._header = self.b(None, None)
        self._f = self._header._next

    def insertion(self, e):
        self._f = self.b(e, self._f)
        return self._f

    def element(self):
        n = self._f._e
        return n


class g(a):
    class d:

        def __init__(self, o, nxt):                   # self
            self._object = o
            self._nxt = nxt._e
            print(self, "------------", self._object, "-----------02  ", self._nxt, nxt)

        def gt_elmt(self, k):
            print("__________03", k)
            return k._nxt                              # k is self , of __init__ from above

    def put(self, e):
        node = super().insertion(e)
        return self.make_position(node)   # make node in above in class a,b
                                          # then pass to class d

    def make_position(self, node):        # making objects of class d
        return self.d(self, node)

    def show_val(self, k):
        print("---------", self.d.gt_elmt(self, k))    # this is how you call method of
                                                       # class inside class


y = g()
print("--------01", y)
k1 = y.put(4)
k2 = y.put(5)
k3 = y.put(6)
y.show_val(k1)
print(k1)
print(k2)
print(k3)

'''
 def __init__(self, o: int, nxt):
     self._object = o

     here self points to objects of class d , and return of put returns locations of objects of d , 
     self._object=o points to object y of g() , and nxt points to objects of b ,
     self._nxt points to values of objects of b .
'''


'''         
--------01 <__main__.g object at 0x0000019919599FA0>
<__main__.g.d object at 0x0000019919599BE0> ------------ <__main__.g object at 0x0000019919599FA0> -----------02   4 <__main__.a.b object at 0x0000019919599C10>
<__main__.g.d object at 0x0000019919599B50> ------------ <__main__.g object at 0x0000019919599FA0> -----------02   5 <__main__.a.b object at 0x0000019919599B80>
<__main__.g.d object at 0x0000019919599AC0> ------------ <__main__.g object at 0x0000019919599FA0> -----------02   6 <__main__.a.b object at 0x0000019919599AF0>
__________03 <__main__.g.d object at 0x0000019919599BE0>
--------- 4
<__main__.g.d object at 0x0000019919599BE0>
<__main__.g.d object at 0x0000019919599B50>
<__main__.g.d object at 0x0000019919599AC0>
'''




#---------------------------------------------------------------------------------------------SINGLE_LINKED_LIST_/_STACK
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


y=a()
y.insert(1)
y.insert(2)
y.insert(3)
y.insert(4)
y.data()

'''
4
3
2
1
'''


#----------------------------------------------------------------------------------------DOUBLE_LINKED_LIST + SWAP LOGIC
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

'''
head to tail
6
7
8
9

tail to head
9
8
7
6


-----------------------
head to tail
6
8
7
9

tail to head
9
7
8
6
'''

#--------------------------------------------------------------------------------------[CLEAN_CODE]-->DOUBLE_LINKED_LIST
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

y=a()
k0=y.head
k1=y.tail
k2=y.insert(11,k0,k1)
k3=y.insert(12,k0,k2)
k4=y.insert(13,k0,k3)
y.display()

'''
from head to tail:
13
12
11
from tail to head:
11
12
13
'''

