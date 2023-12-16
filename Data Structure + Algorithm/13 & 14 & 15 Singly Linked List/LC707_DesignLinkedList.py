"""
707. Design Linked List

Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
 

Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3
 

Constraints:

0 <= index, val <= 1000
Please do not use the built-in LinkedList library.
At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.
"""


class MyLinkedList:
    # 初始化链表
    def __init__(self):
        self.size = 0  # 维护链表的长度
        self.head = ListNode(0)  # 创建虚拟头节点，简化插入和删除操作

    # 获取链表中指定位置的节点值
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1  # 索引无效时返回-1

        current = self.head
        # 遍历链表以到达指定位置
        for _ in range(index + 1):
            current = current.next
        return current.val

    # 在链表头部添加节点
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    # 在链表尾部添加节点
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    # 在链表指定位置添加节点
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return  # 如果索引超出链表长度，则不进行插入

        index = max(0, index)  # 确保索引非负
        self.size += 1
        pred = self.head
        # 移动到指定位置的前一个节点
        for _ in range(index):
            pred = pred.next

        # 创建新节点并执行插入操作
        to_add = ListNode(val)
        to_add.next = pred.next
        pred.next = to_add

    # 删除链表中指定位置的节点
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return  # 如果索引无效，则不进行删除

        self.size -= 1
        pred = self.head
        # 移动到指定位置的前一个节点
        for _ in range(index):
            pred = pred.next

        # 删除操作
        pred.next = pred.next.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
