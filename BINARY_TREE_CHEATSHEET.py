#-----------------------------------------------------------------------------------------------------LINKED_BINARY_TREE
class LinkedBinaryTree:
    class _Node:
        __slots__ = "_element","_parent","_left","_right"
        def __init__(self,element=None,parent=None,left=None,right=None):
            print("------------------0000")
            self._element=element
            self._parent=parent
            self._right=right
            self._left=left

    class Position:
        def __init__(self,container,node):
            print("------------------0011")
            self._container=container
            self._node=node
        def element(self):
            print("------------------0022")
            return self._node._element                                     # clever trick
        def __eq__(self, other):
            print("------------------0033")
            return type(other) is type(self) and other._node is self._node

    def _validate(self,p):
        print("------------------0044")
        if not isinstance(p,self.Position):
            raise TypeError("p must be proper Positon type")
        if p._container is not self:
            raise ValueError("p dose not belong to this container")
        if p._node._parent is p._node:
            raise ValueError("p is no longer valid")
        return p._node                                                     # super clever trick

    def _make_position(self,node):
        print("------------------0055")
        return self.Position(self,node) if node is not None else None


    def __init__(self):
        print("------------------0066")
        self._root=None
        self._size=0
    def __len__(self):
        return self._size
    def root(self):
       return self._make_position(self._root)
    def parent(self,p):
        node=self._validate(p)
        return self._make_position(node._parent)
    def left(self,p):
        node=self._validate(p)
        return self._make_position(node._left)
    def right(self,p):
        node=self._validate(p)
        return self._make_position(node._right)
    def num_children(self,p):
        count=0
        node = self._validate(p)
        if node._left is not None:
            count+=1
        if node._right is not None:
            count+=1
        return count


    def _add_root(self,e):
        print("------------------0077")
        if self._root is not None:
            raise ValueError("Root already exists")
        self._size=1
        self._root=self._Node(e)
        box_root_node=self._make_position(self._root)
        print(self._root, box_root_node)
        return box_root_node
    def _add_left(self,p,e):
        print("------------------0088")
        node=self._validate(p)
        if node._left is not None:
            raise ValueError("Left child already exists")
        self._size +=1
        node._left=self._Node(e,node)
        return self._make_position(node._left)
    def _add_right(self,p,e):
        print("------------------0099")
        node=self._validate(p)
        if node._right is not None:
            raise ValueError("right child already exists")
        self._size +=1
        node._right=self._Node(e,node)
        return self._make_position(node._right)
    def replace(self,p,e):
        print("------------------0110")
        node=self._validate(p)
        old=node._element
        node._element=e
        return old
    def _delete(self,p):
        print("------------------0121")
        node=self._validate(p)
        if self.num_children(p)==2:
            raise ValueError("p has two children")
        child=node._left if node._left else node._right
        if child is not None:
            node._parent=node._parent
        if node is self._root:
            self._root=child
        else:
            parent=node._parent
            if node is parent._left:
                parent._left=child
            else:
                parent._right=child
        self._size-=1
        node._parent=node
        return node._element
    def _attach(self,p,t1,t2):
        print("------------------00132")
        node=self._validate(p)
        if not self.is_leaf(p):
            raise ValueError("position must be leaf")
        if not type(self) is type(t1) is type(t2):
            raise TypeError("Tree type must match")
        self._size+=t1._size+t2._size
        if t1._size:
            t1._root._parent=node
            node._left=t1._root
            t1._size=0
        if t2._size:
            t2._root._parent=node
            node._right=t2._root
            t2._size=0
    def is_leaf(self,p):
        print("------------------0143")
        if p._node._left==None and p._node._right==None:
                return True
        return False
    def print_tree(self,a):
        if a._parent==None and a._element!=None:
            print(a._element)
        if a._left!=None:
            print(a._left._element)
            self.print_tree(a._left)
        if a._right!=None:
            print(a._right._element)
            self.print_tree(a._right)


a=LinkedBinaryTree()
print("-------------------------")
x00=a._add_root(1)
print("-------------------------")
x01=a._add_left(x00,2)
print("-------------------------")
x02=a._add_right(x00,3)
print("-------------------------")
x03=a._add_left(x01,4)
x04=a._add_right(x01,5)
print("-------------------------")
x05=a._add_left(x02,6)
x06=a._add_right(x02,7)

#--------------------------------------------------_print
print("-------------------------")
print(x00._node)
root=x00._node
a.print_tree(root)

#--------------------------------------------------_check_if_leaf
print("-------------------------")
print(a.is_leaf(x06))
print(a.is_leaf(x01))

#--------------------------------------------------_replace_value
print("-------------------------")
a.replace(x00,9)
print("-------------------------")
print(x00._node)
root=x00._node
a.print_tree(root)

#--------------------------------------------------_delete_node
print("-------------------------")
a._delete(x06)
print("-------------------------")
print(x00._node)
root=x00._node
a.print_tree(root)

#-------------------------------------------------_join_tree1,_tree2,_tree3
b=LinkedBinaryTree()
y00=b._add_root(10)
y01=b._add_left(y00,11)
y02=b._add_right(y00,12)
c=LinkedBinaryTree()
z00=c._add_root(27)
a._attach(x04,b,c)
print("-------------------------")
print(x00._node)
root=x00._node
a.print_tree(root)


#-------------------------------------------------------------_remaining_public_accessors_&_class_Position_methods
#-------------------------------------------------_length
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
print(len(a))

#-------------------------------------------------_root
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
n1=a.root()
print(n1)
a.replace(n1,100)
a.print_tree(n1._node)

#-------------------------------------------------_parent
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
n2=a.parent(x01)
print(n2)
print(n2.element())

#-------------------------------------------------_left
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
n3=a.left(x00)
print(n3)
print(n3.element())

#-------------------------------------------------_right
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
n4=a.right(x00)
print(n4)
print(n4.element())

#-------------------------------------------------_children
print(a.num_children(x00))
print(a.num_children(x04))                                   # here tree_2 and tree_3 joined at x04 above
print(a.num_children(x05))

#-------------------------------------------------_equal_-->(__eq__)
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
n5=a.right(x00)
n6=a.right(x00)
print(n5==n6)
