# 🔗 Comprehensive Linked Lists & Binary Trees Tutorial

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive, production-ready implementation of fundamental data structures with modern Python features including type hints, comprehensive documentation, and advanced operations.

## 📋 Table of Contents

- [Features](#-features)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Data Structures](#-data-structures)
- [Performance](#-performance)
- [API Reference](#-api-reference)
- [Examples](#-examples)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features

- **🎯 Type-Safe**: Full type hints for better IDE support and type checking
- **📝 Well-Documented**: Comprehensive docstrings and examples
- **🚀 Optimized**: O(1) operations where possible with tail pointers and size tracking
- **🔒 Robust**: Extensive error handling and edge case coverage
- **🧪 Tested**: Includes demonstration code and test examples
- **🐍 Pythonic**: Uses Python protocols (`__iter__`, `__len__`, `__str__`, etc.)
- **📊 Advanced Features**: Loop detection, merging, reversing, and more

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/rayane2907/linked_lists.git
cd linked_lists

# No external dependencies required!
python improved_linked_lists.py
```

## 🚀 Quick Start

### Singly Linked List

```python
from improved_linked_lists import SinglyLinkedList

# Create a new list
sll = SinglyLinkedList()

# Add elements
sll.insert_at_end(1)
sll.insert_at_end(2)
sll.insert_at_end(3)

# Access elements
print(sll)  # Output: 1 -> 2 -> 3 -> None
print(f"Middle element: {sll.get_middle()}")  # Output: Middle element: 2

# Advanced operations
sll.reverse()
print(sll)  # Output: 3 -> 2 -> 1 -> None

# Check for loops
has_loop = sll.detect_loop()  # Output: False
```

### Doubly Linked List

```python
from improved_linked_lists import DoublyLinkedList

dll = DoublyLinkedList()

# O(1) operations at both ends!
dll.insert_at_beginning(1)
dll.insert_at_end(2)

# Iterate forward and backward
print(list(dll))  # [1, 2]
print(list(reversed(dll)))  # [2, 1]
```

### Binary Tree

```python
from improved_binary_tree import BinaryTree

tree = BinaryTree()

# Build tree
root = tree.add_root(1)
left = tree.add_left(root, 2)
right = tree.add_right(root, 3)
tree.add_left(left, 4)
tree.add_right(left, 5)

# Traverse
for pos in tree.inorder():
    print(pos.element(), end=" ")  # 4 2 5 1 3

# Get tree properties
print(f"Height: {tree.height()}")  # Height: 2
print(f"Size: {len(tree)}")  # Size: 5
```

## 📊 Data Structures

### 1. Singly Linked List
- Basic insertion/deletion operations
- Search and indexing
- Loop detection (Floyd's algorithm)
- Finding middle element
- Reversing
- Removing duplicates
- Merge sorted lists

### 2. Doubly Linked List
- Bidirectional traversal
- O(1) operations at both ends (with tail pointer)
- Reverse iteration support
- Efficient reverse operation

### 3. Circular Linked List
- Circular structure maintenance
- Efficient cyclic operations
- Useful for round-robin scheduling

### 4. Binary Tree
- Position-based interface
- Three traversal methods (preorder, inorder, postorder)
- Height and depth calculations
- Subtree attachment
- Node validation
- Flexible tree operations

## ⚡ Performance

| Operation | Array | Singly LL | Doubly LL | Binary Tree |
|-----------|-------|-----------|-----------|-------------|
| **Access by index** | O(1) | O(n) | O(n) | O(h)* |
| **Insert at start** | O(n) | O(1) | O(1) | - |
| **Insert at end** | O(1)† | O(n) | O(1)‡ | - |
| **Delete from start** | O(n) | O(1) | O(1) | - |
| **Delete from end** | O(1)† | O(n) | O(1)‡ | - |
| **Search** | O(n) | O(n) | O(n) | O(h)* |
| **Space** | O(n) | O(n) | O(n) | O(n) |

*h = height of tree, †Amortized, ‡With tail pointer

## 📖 API Reference

### SinglyLinkedList

#### Core Operations
- `insert_at_beginning(data)` - O(1)
- `insert_at_end(data)` - O(n)
- `insert_at_position(data, position)` - O(n)
- `delete_from_beginning()` - O(1)
- `delete_from_end()` - O(n)
- `delete_from_position(position)` - O(n)
- `delete_by_value(value)` - O(n)

#### Query Operations
- `search(value) -> int` - Find index of value
- `get(index) -> Any` - Get element at index
- `get_middle() -> Any` - Find middle element (O(n))
- `is_empty() -> bool` - Check if empty
- `__len__() -> int` - Get size (O(1))

#### Advanced Operations
- `reverse()` - Reverse list in-place
- `detect_loop() -> bool` - Detect cycle (Floyd's algorithm)
- `remove_duplicates()` - Remove consecutive duplicates
- `to_list() -> List[Any]` - Convert to Python list

#### Protocols
- `__iter__()` - Make iterable
- `__str__()` - String representation
- `__repr__()` - Developer representation

### DoublyLinkedList

All operations from SinglyLinkedList, plus:
- `__reversed__()` - Reverse iteration
- Improved `insert_at_end()` - O(1) with tail pointer
- Improved `delete_from_end()` - O(1) with tail pointer

### BinaryTree

#### Tree Construction
- `add_root(e)` - Create root
- `add_left(p, e)` - Add left child
- `add_right(p, e)` - Add right child
- `attach(p, t1, t2)` - Attach subtrees

#### Tree Navigation
- `root() -> Position` - Get root position
- `parent(p) -> Position` - Get parent
- `left(p) -> Position` - Get left child
- `right(p) -> Position` - Get right child
- `children(p)` - Get all children

#### Tree Analysis
- `height(p) -> int` - Calculate height
- `depth(p) -> int` - Calculate depth
- `num_children(p) -> int` - Count children
- `is_leaf(p) -> bool` - Check if leaf
- `is_empty() -> bool` - Check if empty

#### Tree Traversals
- `preorder()` - Preorder traversal
- `inorder()` - Inorder traversal
- `postorder()` - Postorder traversal

#### Tree Modification
- `replace(p, e)` - Replace element
- `delete(p)` - Delete node

## 💡 Examples

### Example 1: LRU Cache Implementation

```python
class LRUCache:
    """Least Recently Used Cache using Doubly Linked List"""
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.dll = DoublyLinkedList()
    
    def get(self, key):
        if key in self.cache:
            # Move to front (most recently used)
            self.dll.delete_by_value(key)
            self.dll.insert_at_beginning(key)
            return self.cache[key]
        return -1
    
    def put(self, key, value):
        if key in self.cache:
            self.dll.delete_by_value(key)
        elif len(self.cache) >= self.capacity:
            # Remove least recently used
            lru = self.dll.delete_from_end()
            del self.cache[lru]
        
        self.dll.insert_at_beginning(key)
        self.cache[key] = value
```

### Example 2: Expression Tree Evaluation

```python
def evaluate_expression_tree(tree, root):
    """Evaluate arithmetic expression tree"""
    if tree.is_leaf(root):
        return float(root.element())
    
    left = evaluate_expression_tree(tree, tree.left(root))
    right = evaluate_expression_tree(tree, tree.right(root))
    operator = root.element()
    
    if operator == '+':
        return left + right
    elif operator == '-':
        return left - right
    elif operator == '*':
        return left * right
    elif operator == '/':
        return left / right
```

### Example 3: Palindrome Checker

```python
def is_palindrome(sll: SinglyLinkedList) -> bool:
    """Check if linked list is a palindrome"""
    # Convert to list and check
    lst = sll.to_list()
    return lst == lst[::-1]

# Or using slow/fast pointers
def is_palindrome_optimal(sll: SinglyLinkedList) -> bool:
    """O(n) time, O(1) space palindrome check"""
    slow = fast = sll.head
    stack = []
    
    while fast and fast.next:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next
    
    if fast:  # Odd length
        slow = slow.next
    
    while slow:
        if slow.data != stack.pop():
            return False
        slow = slow.next
    
    return True
```

### Example 4: Merge K Sorted Lists

```python
from improved_linked_lists import merge_sorted_lists
import heapq

def merge_k_sorted_lists(lists: List[SinglyLinkedList]) -> SinglyLinkedList:
    """Merge k sorted linked lists using min-heap"""
    min_heap = []
    
    # Initialize heap with first node of each list
    for i, lst in enumerate(lists):
        if not lst.is_empty():
            heapq.heappush(min_heap, (lst.get(0), i, 0))
    
    result = SinglyLinkedList()
    
    while min_heap:
        val, list_idx, elem_idx = heapq.heappop(min_heap)
        result.insert_at_end(val)
        
        # Add next element from same list
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx].get(elem_idx + 1)
            heapq.heappush(min_heap, (next_val, list_idx, elem_idx + 1))
    
    return result
```

## 🎯 Use Cases

### Singly Linked Lists
- **Undo functionality** in text editors
- **Browser history** (back button)
- **Implementation of stacks and queues**
- **Symbol tables** in compilers

### Doubly Linked Lists
- **LRU/LFU cache implementation**
- **Browser navigation** (back and forward)
- **Music/video playlists** with bidirectional navigation
- **Undo/Redo functionality**

### Circular Linked Lists
- **Round-robin scheduling** in operating systems
- **Circular buffers** for streaming data
- **Multiplayer games** (turn-based)
- **Resource allocation** in networks

### Binary Trees
- **Expression parsing** and evaluation
- **File system hierarchies**
- **Organization charts**
- **Decision trees** in machine learning
- **Huffman coding** for compression

## 🧪 Running Tests

```python
# Run the demonstration scripts
python improved_linked_lists.py
python improved_binary_tree.py

# Or use pytest (if you add test files)
pytest tests/
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Setup

```bash
# Clone and setup
git clone https://github.com/rayane2907/linked_lists.git
cd linked_lists

# Install development dependencies (optional)
pip install black mypy pytest

# Run type checking
mypy improved_linked_lists.py

# Format code
black improved_linked_lists.py
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by classic data structures textbooks
- Implements algorithms from "Introduction to Algorithms" (CLRS)
- Follows Python Enhancement Proposals (PEPs) for style

## 📚 Further Reading

- [Python Data Structures Documentation](https://docs.python.org/3/tutorial/datastructures.html)
- [Big O Cheat Sheet](https://www.bigocheatsheet.com/)
- [Introduction to Algorithms (CLRS)](https://mitpress.mit.edu/books/introduction-algorithms-third-edition)
- [Data Structures in Python](https://realpython.com/python-data-structures/)

## 📞 Contact

Rayane - [@rayane2907](https://github.com/rayane2907)

Project Link: [https://github.com/rayane2907/linked_lists](https://github.com/rayane2907/linked_lists)

---

⭐ **If you find this project useful, please consider giving it a star!** ⭐
