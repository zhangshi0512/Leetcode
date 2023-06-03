# Big O Analysis

Here's an updated table that includes the Big O notation for the time and space complexity of common operations in a singly linked list:

| Operation                           | Time Complexity | Space Complexity |
| ----------------------------------- | --------------- | ---------------- |
| Accessing an element by index       | O(n)            | O(1)             |
| Accessing the first element         | O(1)            | O(1)             |
| Accessing the last element          | O(n)            | O(1)             |
| Inserting an element at the front   | O(1)            | O(1)             |
| Inserting an element at the end     | O(n)            | O(1)             |
| Inserting an element in the middle  | O(n)            | O(1)             |
| Removing an element from the front  | O(1)            | O(1)             |
| Removing an element from the end    | O(n)            | O(1)             |
| Removing an element from the middle | O(n)            | O(1)             |
| Searching for an element            | O(n)            | O(1)             |
| Reversing the linked list           | O(n)            | O(1)             |

Note: The time complexity indicates the worst-case scenario for each operation, and the space complexity refers to the additional space used by the data structure itself, excluding the space required to store the elements.

# Singly Linked List Methods

Here's a demo code for each method of a Singly Linked List in Python with comments explaining each step:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        # Check if the linked list is empty
        return self.head is None

    def length(self):
        # Return the length of the linked list
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def append(self, data):
        # Append an element to the end of the linked list
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def insert(self, data, position):
        # Insert an element at a given position in the linked list
        if position == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(position - 1):
                if current is None:
                    raise IndexError("Position out of range")
                current = current.next
            new_node = Node(data)
            new_node.next = current.next
            current.next = new_node

    def remove(self, data):
        # Remove the first occurrence of an element from the linked list
        if self.head is None:
            raise ValueError("Linked list is empty")
        if self.head.data == data:
            self.head = self.head.next
        else:
            current = self.head
            while current.next is not None and current.next.data != data:
                current = current.next
            if current.next is None:
                raise ValueError("Element not found")
            current.next = current.next.next

    def search(self, data):
        # Search for the first occurrence of an element in the linked list
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    def reverse(self):
        # Reverse the linked list
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def display(self):
        # Display the linked list
        if self.head is None:
            print("Linked list is empty")
            return
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Usage example
my_list = LinkedList()

print("Is empty:", my_list.is_empty())  # Output: True

my_list.append(42)
my_list.append(23)
my_list.append(15)
my_list.display()  # Output: 42 -> 23 -> 15 -> None

print("Length:", my_list.length())  # Output: 3

my_list.insert(56, 1)
my_list.display()  # Output: 42 -> 56 -> 23 -> 15 -> None

my_list.remove(23)
my_list.display()  # Output: 42 -> 56 -> 15 -> None

print("Search 56:", my_list.search(56))  # Output: True
print("Search 23:", my

_list.search(23))  # Output: False

my_list.reverse()
my_list.display()  # Output: 15 -> 56 -> 42 -> None
```

This code provides a demonstration of each method and includes comments explaining each step for better understanding.
