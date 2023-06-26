class Node:
    """
    an object for storing a single node of a linked list
    models two attributes - data and the link to the next node in the list
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data


class LinkedList:
    """
    Singly linked list
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        """
        returns the number of nodes in the list
        takes O(n) time
        """
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        """
        adds a new node containing data at head of the list
        takes O(1) time
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        search for the first node containing data that matches the key
        return the node for 'None' if not found
        takes O(n) time
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node

        return None

    def node_at_index(self, index):
        """
        returns the node at specified index
        takes O(n) time
        """

        if index >= self.size():
            raise IndexError('index out of range')

        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position += 1

            return current

    def insert(self, data, index):
        """
        inserts a new node containing data at index position
        insertion takes O(1) time but finding the node at the insertion point takes O(n) time
        takes overall O(n) time        
        """
        if index == 0:
            self.add(data)

        if index > 0:
            # create a new node
            new = Node(data)
            # use a counter variable
            position = index
            # use the head as the start
            current = self.head
            # keeps pushing the node to next node
            # the loop end before the index, in case for last item
            # need to "rewire" link by two side of inserted node
            while position > 1:
                current = current.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    def remove(self, key):
        """
        removes node containing data that matches the key
        returns the node or none if key doesn't exist
        takes O(n) time
        """
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node

        return current

    def remove_at_index(self, index):
        if index >= self.size():
            raise IndexError('index out of range')

        current = self.head

        if index == 0:
            self.head = current.next_node
            self.size -= 1
            return current

        position = index

        while position > 1:
            current = current.next_node
            position -= 1

        prev_node = current
        current = current.next_node
        next_node = current.next_node

        prev_node.next_node = next_node
        self.size -= 1

        return current

    def __iter__(self):
        current = self.head

        while current:
            yield current
            current = current.next_node

    def __repr__(self):
        """
        return a string representation of the list
        takes O(n) time
        """
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node

        return '-> '.join(nodes)


# create two nodes and their link
"""
N1 = Node(10)
print(N1)
N2 = Node(20)
print(N2)
N1.next_node = N2
print(N1.next_node)
"""

# create a linked list by defining head
"""
l = LinkedList()
l.head = N1
print(l.size())
"""

# create a linked list by using add
"""
l1 = LinkedList()
l1.add(1)
l1.add(2)
l1.add(3)
print(l1.size())
"""

# represent the linked list
"""
print(l1)
"""

# search for the first node that matches the key
"""
l1.add(2)
l1.add(9)
l1.add(11)
print(l1)
n = l1.search(11)
print(n)
"""

# insert a node after the 2nd value
"""
l1.insert(17, 2)
print(l1)
"""

# removes a node from the linked list
"""
l1.remove(2)
print(l1)
"""
