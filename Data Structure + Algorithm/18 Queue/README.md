# Big O Analysis

Here are the common operations performed on a queue and their corresponding time and space complexities. Python's collections.deque (double-ended queue) can be used to implement a queue efficiently.

| Operation  | Time Complexity | Space Complexity |
| ---------- | --------------- | ---------------- |
| Enqueue    | O(1)            | O(1)             |
| Dequeue    | O(1)            | O(1)             |
| IsEmpty    | O(1)            | O(1)             |
| Size       | O(1)            | O(1)             |
| Peek/Front | O(1)            | O(1)             |

# Code Template

Here's a basic Python code template for a queue using `collections.deque`:

```python
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    # Add an element to end of queue
    def enqueue(self, data):
        self.queue.append(data)

    # Remove an element from front of queue
    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        return "Queue is empty."

    # Check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Get the size of the queue
    def size(self):
        return len(self.queue)

    # Get the first element in queue
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        return "Queue is empty."
```

In this code, `collections.deque` is used to create a queue because it allows for O(1) time complexity for append and pop operations from both ends. The space complexity for each operation is also O(1), because each operation only requires a constant amount of space to perform.
