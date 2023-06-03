# Heap

Here's a table with the Big O time and space complexity for common operations on a binary heap:

| Operation    | Time Complexity | Space Complexity |
| ------------ | --------------- | ---------------- |
| Insert       | O(log n)        | O(n)             |
| Delete       | O(log n)        | O(n)             |
| Find Min/Max | O(1)            | O(n)             |
| Peek Min/Max | O(1)            | O(n)             |
| Heapify      | O(n)            | O(n)             |

Here's a basic implementation of a binary heap in Python (we'll use min-heap for this example):

```python
class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[parent_index] > self.heap[index]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            self._heapify_up(parent_index)

    def delete(self):
        if len(self.heap) > 1:
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            min_val = self.heap.pop()
            self._heapify_down(0)
        elif len(self.heap) == 1:
            min_val = self.heap.pop()
        else:
            min_val = None
        return min_val

    def _heapify_down(self, index):
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        smallest = index
        if left_index < len(self.heap) and self.heap[left_index] < self.heap[smallest]:
            smallest = left_index
        if right_index < len(self.heap) and self.heap[right_index] < self.heap[smallest]:
            smallest = right_index
        if smallest != index:
            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            self._heapify_down(smallest)

    def peek(self):
        return self.heap[0] if self.heap else None
```

# Priority Queue

Here is the Big O complexity table for a Priority Queue:

| Operation        | Time Complexity | Space Complexity |
| ---------------- | --------------- | ---------------- |
| Insert (enqueue) | O(log n)        | O(n)             |
| Delete (dequeue) | O(log n)        | O(n)             |
| Peek             | O(1)            | O(n)             |

This table assumes a priority queue implemented using a binary heap. Insert and delete operations involve restructuring the heap to maintain the heap property, hence they have a logarithmic time complexity. The peek operation is simply accessing the top element of the heap, which is a constant time operation.

The space complexity for all these operations is O(n) because in the worst case we may need to store n elements in the heap.

Priority queues can be implemented using binary heaps. The time and space complexities remain the same as for the binary heap.

```python
class PriorityQueue(MinHeap):
    def __init__(self):
        super().__init__()

    def enqueue(self, val):
        self.insert(val)

    def dequeue(self):
        return self.delete()

# Sample usage:
pq = PriorityQueue()
pq.enqueue(3)
pq.enqueue(2)
pq.enqueue(1)
print(pq.dequeue())  # Output: 1
```

The `enqueue` operation inserts a new element into the priority queue, and `dequeue` removes and returns the highest priority element. In this case, we've set up the priority queue as a min-heap, so lower values have higher priority. For a max-heap based priority queue, you would adjust the `_heapify_up` and `_heapify_down` methods accordingly.
