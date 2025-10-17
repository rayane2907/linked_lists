"""
Enhanced Linked List Implementations with Type Hints and Advanced Features
"""

from typing import Optional, Any, Iterator, List
from dataclasses import dataclass


@dataclass
class Node:
    """Node class for singly linked list."""
    data: Any
    next: Optional['Node'] = None
    
    def __repr__(self) -> str:
        return f"Node({self.data})"


@dataclass
class DNode:
    """Node class for doubly linked list."""
    data: Any
    next: Optional['DNode'] = None
    prev: Optional['DNode'] = None
    
    def __repr__(self) -> str:
        return f"DNode({self.data})"


class SinglyLinkedList:
    """Enhanced Singly Linked List with comprehensive operations."""
    
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self._size: int = 0
    
    def __len__(self) -> int:
        """Return the number of elements in the list."""
        return self._size
    
    def is_empty(self) -> bool:
        """Return True if the list is empty."""
        return self.head is None
    
    def insert_at_beginning(self, data: Any) -> None:
        """Insert a new node at the beginning. O(1) time complexity."""
        new_node = Node(data, self.head)
        self.head = new_node
        self._size += 1
    
    def insert_at_end(self, data: Any) -> None:
        """Insert a new node at the end. O(n) time complexity."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self._size += 1
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        self._size += 1
    
    def insert_at_position(self, data: Any, position: int) -> None:
        """Insert a new node at the specified position. O(n) time complexity."""
        if position < 0 or position > self._size:
            raise IndexError(f"Position {position} out of bounds. List size: {self._size}")
        
        if position == 0:
            self.insert_at_beginning(data)
            return
        
        new_node = Node(data)
        current = self.head
        for _ in range(position - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self._size += 1
    
    def delete_from_beginning(self) -> Optional[Any]:
        """Delete and return the first node's data. O(1) time complexity."""
        if not self.head:
            raise IndexError("Cannot delete from empty list")
        
        data = self.head.data
        self.head = self.head.next
        self._size -= 1
        return data
    
    def delete_from_end(self) -> Optional[Any]:
        """Delete and return the last node's data. O(n) time complexity."""
        if not self.head:
            raise IndexError("Cannot delete from empty list")
        
        if not self.head.next:
            data = self.head.data
            self.head = None
            self._size -= 1
            return data
        
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        
        data = second_last.next.data
        second_last.next = None
        self._size -= 1
        return data
    
    def delete_from_position(self, position: int) -> Any:
        """Delete and return the node's data at specified position. O(n) time complexity."""
        if position < 0 or position >= self._size:
            raise IndexError(f"Position {position} out of bounds. List size: {self._size}")
        
        if position == 0:
            return self.delete_from_beginning()
        
        current = self.head
        for _ in range(position - 1):
            current = current.next
        
        data = current.next.data
        current.next = current.next.next
        self._size -= 1
        return data
    
    def delete_by_value(self, value: Any) -> bool:
        """Delete the first node with the specified value. Returns True if found."""
        if not self.head:
            return False
        
        if self.head.data == value:
            self.head = self.head.next
            self._size -= 1
            return True
        
        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                self._size -= 1
                return True
            current = current.next
        
        return False
    
    def search(self, value: Any) -> int:
        """Return the index of the first occurrence of value, or -1 if not found."""
        current = self.head
        index = 0
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1
    
    def get(self, index: int) -> Any:
        """Return the data at the specified index."""
        if index < 0 or index >= self._size:
            raise IndexError(f"Index {index} out of bounds. List size: {self._size}")
        
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data
    
    def reverse(self) -> None:
        """Reverse the linked list in-place. O(n) time complexity."""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
    def detect_loop(self) -> bool:
        """Detect if there's a loop in the linked list using Floyd's algorithm."""
        slow = fast = self.head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
    def get_middle(self) -> Optional[Any]:
        """Return the middle element of the list."""
        if not self.head:
            return None
        
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data
    
    def remove_duplicates(self) -> None:
        """Remove duplicate values from the list (for sorted lists)."""
        current = self.head
        while current and current.next:
            if current.data == current.next.data:
                current.next = current.next.next
                self._size -= 1
            else:
                current = current.next
    
    def to_list(self) -> List[Any]:
        """Convert linked list to Python list."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
    
    def __iter__(self) -> Iterator[Any]:
        """Make the linked list iterable."""
        current = self.head
        while current:
            yield current.data
            current = current.next
    
    def __str__(self) -> str:
        """String representation of the linked list."""
        if not self.head:
            return "None"
        return " -> ".join(str(data) for data in self) + " -> None"
    
    def __repr__(self) -> str:
        return f"SinglyLinkedList([{', '.join(str(data) for data in self)}])"


class DoublyLinkedList:
    """Enhanced Doubly Linked List with comprehensive operations."""
    
    def __init__(self) -> None:
        self.head: Optional[DNode] = None
        self.tail: Optional[DNode] = None
        self._size: int = 0
    
    def __len__(self) -> int:
        return self._size
    
    def is_empty(self) -> bool:
        return self.head is None
    
    def insert_at_beginning(self, data: Any) -> None:
        """Insert at the beginning. O(1) time complexity."""
        new_node = DNode(data, next=self.head)
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node
        self._size += 1
    
    def insert_at_end(self, data: Any) -> None:
        """Insert at the end. O(1) time complexity (using tail pointer)."""
        new_node = DNode(data, prev=self.tail)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self._size += 1
    
    def delete_from_beginning(self) -> Optional[Any]:
        """Delete from beginning. O(1) time complexity."""
        if not self.head:
            raise IndexError("Cannot delete from empty list")
        
        data = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self._size -= 1
        return data
    
    def delete_from_end(self) -> Optional[Any]:
        """Delete from end. O(1) time complexity (using tail pointer)."""
        if not self.tail:
            raise IndexError("Cannot delete from empty list")
        
        data = self.tail.data
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self._size -= 1
        return data
    
    def reverse(self) -> None:
        """Reverse the doubly linked list in-place."""
        current = self.head
        self.head, self.tail = self.tail, self.head
        
        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev
    
    def __iter__(self) -> Iterator[Any]:
        current = self.head
        while current:
            yield current.data
            current = current.next
    
    def __reversed__(self) -> Iterator[Any]:
        """Iterate in reverse using tail pointer."""
        current = self.tail
        while current:
            yield current.data
            current = current.prev
    
    def __str__(self) -> str:
        if not self.head:
            return "None"
        return "None <-> " + " <-> ".join(str(data) for data in self) + " <-> None"
    
    def __repr__(self) -> str:
        return f"DoublyLinkedList([{', '.join(str(data) for data in self)}])"


class CircularLinkedList:
    """Enhanced Circular Linked List implementation."""
    
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self._size: int = 0
    
    def __len__(self) -> int:
        return self._size
    
    def is_empty(self) -> bool:
        return self.head is None
    
    def insert_at_beginning(self, data: Any) -> None:
        """Insert at the beginning of circular list."""
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
        else:
            # Find last node
            last = self.head
            while last.next != self.head:
                last = last.next
            new_node.next = self.head
            last.next = new_node
            self.head = new_node
        self._size += 1
    
    def insert_at_end(self, data: Any) -> None:
        """Insert at the end of circular list."""
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
        else:
            last = self.head
            while last.next != self.head:
                last = last.next
            last.next = new_node
            new_node.next = self.head
        self._size += 1
    
    def delete_from_beginning(self) -> Optional[Any]:
        """Delete from the beginning of circular list."""
        if not self.head:
            raise IndexError("Cannot delete from empty list")
        
        data = self.head.data
        if self.head.next == self.head:
            self.head = None
        else:
            last = self.head
            while last.next != self.head:
                last = last.next
            last.next = self.head.next
            self.head = self.head.next
        self._size -= 1
        return data
    
    def __iter__(self) -> Iterator[Any]:
        if not self.head:
            return
        current = self.head
        while True:
            yield current.data
            current = current.next
            if current == self.head:
                break
    
    def __str__(self) -> str:
        if not self.head:
            return "None"
        elements = list(self)
        return " -> ".join(str(e) for e in elements) + f" -> {elements[0]} (circular)"


def merge_sorted_lists(list1: SinglyLinkedList, list2: SinglyLinkedList) -> SinglyLinkedList:
    """Merge two sorted singly linked lists into one sorted list."""
    merged = SinglyLinkedList()
    p, q = list1.head, list2.head
    
    # Create a dummy node to simplify logic
    dummy = Node(0)
    current = dummy
    
    while p and q:
        if p.data <= q.data:
            current.next = Node(p.data)
            p = p.next
        else:
            current.next = Node(q.data)
            q = q.next
        current = current.next
        merged._size += 1
    
    # Attach remaining nodes
    while p:
        current.next = Node(p.data)
        p = p.next
        current = current.next
        merged._size += 1
    
    while q:
        current.next = Node(q.data)
        q = q.next
        current = current.next
        merged._size += 1
    
    merged.head = dummy.next
    return merged


# ========== DEMONSTRATION AND TESTS ==========

if __name__ == "__main__":
    print("=" * 60)
    print("SINGLY LINKED LIST DEMONSTRATION")
    print("=" * 60)
    
    sll = SinglyLinkedList()
    
    # Insert operations
    print("\n1. Inserting elements...")
    for i in [1, 2, 3, 4, 5]:
        sll.insert_at_end(i)
    print(f"   List: {sll}")
    print(f"   Length: {len(sll)}")
    
    # Access operations
    print("\n2. Accessing elements...")
    print(f"   Element at index 2: {sll.get(2)}")
    print(f"   Middle element: {sll.get_middle()}")
    print(f"   Search for 3: index {sll.search(3)}")
    
    # Modification operations
    print("\n3. Modifying list...")
    sll.insert_at_beginning(0)
    print(f"   After insert at beginning (0): {sll}")
    sll.insert_at_position(10, 3)
    print(f"   After insert at position 3 (10): {sll}")
    
    # Deletion operations
    print("\n4. Deleting elements...")
    deleted = sll.delete_from_end()
    print(f"   Deleted from end: {deleted}, List: {sll}")
    sll.delete_by_value(10)
    print(f"   After deleting value 10: {sll}")
    
    # Advanced operations
    print("\n5. Advanced operations...")
    sll.reverse()
    print(f"   After reversing: {sll}")
    print(f"   Has loop? {sll.detect_loop()}")
    print(f"   As Python list: {sll.to_list()}")
    
    print("\n" + "=" * 60)
    print("DOUBLY LINKED LIST DEMONSTRATION")
    print("=" * 60)
    
    dll = DoublyLinkedList()
    
    print("\n1. Building doubly linked list...")
    for i in range(1, 6):
        dll.insert_at_end(i)
    print(f"   Forward: {dll}")
    print(f"   Backward: {list(reversed(dll))}")
    
    print("\n2. Operations...")
    dll.insert_at_beginning(0)
    print(f"   After insert at beginning: {dll}")
    dll.reverse()
    print(f"   After reversing: {dll}")
    
    print("\n" + "=" * 60)
    print("CIRCULAR LINKED LIST DEMONSTRATION")
    print("=" * 60)
    
    cll = CircularLinkedList()
    
    print("\n1. Building circular linked list...")
    for i in range(1, 6):
        cll.insert_at_end(i)
    print(f"   {cll}")
    
    print("\n" + "=" * 60)
    print("MERGE SORTED LISTS DEMONSTRATION")
    print("=" * 60)
    
    list1 = SinglyLinkedList()
    list2 = SinglyLinkedList()
    
    for i in [1, 3, 5, 7]:
        list1.insert_at_end(i)
    for i in [2, 4, 6, 8]:
        list2.insert_at_end(i)
    
    print(f"\n   List 1: {list1}")
    print(f"   List 2: {list2}")
    
    merged = merge_sorted_lists(list1, list2)
    print(f"   Merged: {merged}")
