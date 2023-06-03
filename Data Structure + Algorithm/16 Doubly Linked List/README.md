# Big O Analysis

Certainly! Here's a table that lists common operations on a doubly linked list along with their time and space complexities:

| Operation                           | Time Complexity | Space Complexity |
| ----------------------------------- | --------------- | ---------------- |
| Accessing an element by index       | O(n)            | O(1)             |
| Accessing the first element         | O(1)            | O(1)             |
| Accessing the last element          | O(1)            | O(1)             |
| Inserting an element at the front   | O(1)            | O(1)             |
| Inserting an element at the end     | O(1)            | O(1)             |
| Inserting an element in the middle  | O(n)            | O(1)             |
| Removing an element from the front  | O(1)            | O(1)             |
| Removing an element from the end    | O(1)            | O(1)             |
| Removing an element from the middle | O(n)            | O(1)             |
| Searching for an element            | O(n)            | O(1)             |

# Doubly Linked List Methods

Here's a demo code for each method of a Doubly Linked List in Python with comments explaining each step:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        # Check if the doubly linked list is empty
        return self.head is None

    def length(self):
        # Return the length of the doubly linked list
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def append(self, data):
        # Append an element to the end of the doubly linked list
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def insert(self, data, position):
        # Insert an element at a given position in the doubly linked list
        if position == 0:
            new_node = Node(data)
            new_node.next = self.head
            if self.head is not None:
                self.head.prev = new_node
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
        else:
            current = self.head
            for _ in range(position - 1):
                if current is None:
                    raise IndexError("Position out of range")
                current = current.next
            new_node = Node(data)
            new_node.next = current.next
            new_node.prev = current
            if current.next is not None:
                current.next.prev = new_node
            current.next = new_node

    def remove(self, data):
        # Remove the first occurrence of an element from the doubly linked list
        if self.head is None:
            raise ValueError("Doubly linked list is empty")
        if self.head.data == data:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        else:
            current = self.head
            while current.next is not None and current.next.data != data:
                current = current.next
            if current.next is None:
                raise ValueError("Element not found")
            current.next = current.next.next
            if current.next is not None:
                current.next.prev = current

    def search(self, data):
        # Search for the first occurrence of an element in the doubly linked list
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    def display(self):
        # Display the doubly linked list
        if self.head is None:
            print("Doubly linked list is empty")
            return
        current = self.head
        while current is not None:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")


# Usage example
my_list = DoublyLinkedList()

print("Is empty:", my_list.is_empty())  # Output: True

my_list.append(42)
my_list.append(23)
my_list.append(15)
my_list.display()  # Output: 42 <-> 23 <-> 15 <-> None

print("Length:", my_list.length())  # Output: 3

my_list.insert(56, 1)
my_list

.display()  # Output: 42 <-> 56 <-> 23 <-> 15 <-> None

my_list.remove(23)
my_list.display()  # Output: 42 <-> 56 <-> 15 <-> None

print("Search 56:", my_list.search(56))  # Output: True
print("Search 23:", my_list.search(23))  # Output: False
```

This code provides a demonstration of each method and includes comments explaining each step for better understanding.
