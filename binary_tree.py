"""
Enhanced Binary Tree Implementation with Proper Error Handling
"""

class BinaryTree:
    """A binary tree implementation using linked nodes."""
    
    class _Node:
        """Lightweight node structure for tree."""
        __slots__ = '_left', '_right', '_parent', '_data'
        
        def __init__(self, data, left=None, right=None, parent=None):
            self._data = data
            self._left = left
            self._right = right
            self._parent = parent
    
    class Position:
        """Abstraction representing the location of a single element."""
        
        def __init__(self, container, node):
            self._container = container
            self._node = node
        
        def element(self):
            """Return the element stored at this position."""
            return self._node._data
        
        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node
        
        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)
    
    def _validate(self, p):
        """Return associated node, if position is valid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:  # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node
    
    def _make_position(self, node):
        """Return Position instance for given node (or None if no node)."""
        return self.Position(self, node) if node is not None else None
    
    def __init__(self):
        """Create an initially empty binary tree."""
        self._root = None
        self._size = 0
    
    def __len__(self):
        """Return the total number of elements in the tree."""
        return self._size
    
    def is_empty(self):
        """Return True if tree is empty."""
        return self._size == 0
    
    def root(self):
        """Return the root Position of the tree (or None if empty)."""
        return self._make_position(self._root)
    
    def parent(self, p):
        """Return the Position of p's parent (or None if p is root)."""
        node = self._validate(p)
        return self._make_position(node._parent)
    
    def left(self, p):
        """Return the Position of p's left child (or None if no left child)."""
        node = self._validate(p)
        return self._make_position(node._left)
    
    def right(self, p):
        """Return the Position of p's right child (or None if no right child)."""
        node = self._validate(p)
        return self._make_position(node._right)
    
    def num_children(self, p):
        """Return the number of children of Position p."""
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count
    
    def is_leaf(self, p):
        """Return True if Position p is a leaf."""
        return self.num_children(p) == 0
    
    def add_root(self, e):
        """Place element e at the root of an empty tree and return new Position.
        Raise ValueError if tree is not empty.
        """
        if self._root is not None:
            raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)
    
    def add_left(self, p, e):
        """Create a new left child for Position p, storing element e.
        Return the Position of new node.
        Raise ValueError if Position p already has a left child.
        """
        node = self._validate(p)
        if node._left is not None:
            raise ValueError('Left child exists')
        self._size += 1
        node._left = self._Node(e, parent=node)
        return self._make_position(node._left)
    
    def add_right(self, p, e):
        """Create a new right child for Position p, storing element e.
        Return the Position of new node.
        Raise ValueError if Position p already has a right child.
        """
        node = self._validate(p)
        if node._right is not None:
            raise ValueError('Right child exists')
        self._size += 1
        node._right = self._Node(e, parent=node)
        return self._make_position(node._right)
    
    def replace(self, p, e):
        """Replace the element at position p with e, and return old element."""
        node = self._validate(p)
        old = node._data
        node._data = e
        return old
    
    def delete(self, p):
        """Delete the node at Position p, and replace it with its child, if any.
        Return the element that had been stored at Position p.
        Raise ValueError if Position p has two children.
        """
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError('Position has two children')
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node  # convention for deprecated node
        return node._data
    
    def attach(self, p, t1, t2):
        """Attach trees t1 and t2 as left and right subtrees of external p."""
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError('Position must be leaf')
        if not type(self) is type(t1) is type(t2):
            raise TypeError('Tree types must match')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0
    
    # Tree traversal methods
    def preorder(self):
        """Generate a preorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p
    
    def _subtree_preorder(self, p):
        """Generate a preorder iteration of positions in subtree rooted at p."""
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other
    
    def inorder(self):
        """Generate an inorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p
    
    def _subtree_inorder(self, p):
        """Generate an inorder iteration of positions in subtree rooted at p."""
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other
    
    def postorder(self):
        """Generate a postorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p
    
    def _subtree_postorder(self, p):
        """Generate a postorder iteration of positions in subtree rooted at p."""
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p
    
    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
    
    def height(self, p=None):
        """Return the height of the subtree rooted at Position p.
        If p is None, return the height of the entire tree.
        """
        if p is None:
            p = self.root()
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self.height(c) for c in self.children(p))
    
    def depth(self, p):
        """Return the number of levels separating Position p from the root."""
        if p == self.root():
            return 0
        else:
            return 1 + self.depth(self.parent(p))


# Example usage and tests
if __name__ == "__main__":
    tree = BinaryTree()
    
    # Build a sample tree
    root = tree.add_root(1)
    left = tree.add_left(root, 2)
    right = tree.add_right(root, 3)
    tree.add_left(left, 4)
    tree.add_right(left, 5)
    tree.add_left(right, 6)
    tree.add_right(right, 7)
    
    print(f"Tree size: {len(tree)}")
    print(f"Root element: {tree.root().element()}")
    print(f"Tree height: {tree.height()}")
    
    print("\nPreorder traversal:")
    for pos in tree.preorder():
        print(pos.element(), end=" ")
    
    print("\n\nInorder traversal:")
    for pos in tree.inorder():
        print(pos.element(), end=" ")
    
    print("\n\nPostorder traversal:")
    for pos in tree.postorder():
        print(pos.element(), end=" ")
    print()
