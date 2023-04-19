# linked_lsts
        class Tree:
        class _Node:
          __slots__:'_left','right','parent','data'
          def __int__(self,left,right,parent,data):
            self._left=left
            self._right=right
            self._parent=parent
            self._data=data
        class _position:
          def __init__(self,container,node):
            self._cotainer=cotainer
            self._node=node
          def _element(self):
            return self._node._data
          def _validate (self,p):
            if not isintance(p, self_position):
              raise TypeError ('p should be a valid position')
            if p_container is not self:
              raise ValueError ('p should be created for this tree')
            if p._node._parent is p._node:
              raise ValueError ('p is no longer valid position')
            return p._node
          def _make_position (self, node):
            if node is not None:
               return self._position
            else None 
          def __init__(self):
            self._root= none
            self._size = 0
          def __len__(self):
            return self._size
          def root(self):
            return self._make_position(self.root)
          def parent(self,p):
            node = self._validate(p)
            return self._make_position(node.parent)
          def left(self,p):
            node = self._validate(p)
            return self._make_position(node.left)
         def right(self,p):
          node= self._validate(p)
          return self._make_position(node.right)
         def _nbr_children(self,p):
           count=0
           if self.left is not None
             counter+=1
             return counter
         def add_root(self,e):
           if self.root is not None:
             raise ValueError ('root exists')
             self._size=1
             self._root=self._node(data=e)
           return self._make_position(self._root)
         def add_left(self, p, e):
           node=self._validate(p)
           if node.left is not None:
             raise ValueError ('left child exists')
           node.left=selft._node(e, node)
           selff._size+=1
           return self._make_position(self._left)
         def add_left(self, p, e):
           node=left._validate(p)
           if node.right is not None:
             raise ValueError ('right child exists')
           node.right=selft._node(e, node)
           selff._size+=1
           return self._make_position(self._right)
         def _replace(self,p,e):
           node=self._validate(p)
           old=node._element
           node._element=e
           return old
