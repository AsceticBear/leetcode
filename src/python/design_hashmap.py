'''
Design a HashMap without using any built-in hash table libraries.
'''

# Add code here

'''
分析:

方法1： 因为题目比较简单，用一个就数组解决。

class MyHashMap(object):
    
    def __init__(self):
        self.table = [-1] * 1000001

    def put(self, key, value):
        self.table[key] = value
        
    def get(self, key):
        return self.table[key]
        

    def remove(self, key):
        self.table[key] = -1

方法2： 链表

class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self, capacity=1000):
        """
        Initialize your data structure here.
        """
        self.capacity = capacity
        self.data = [None] * capacity

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        idx = key % self.capacity
        node = self.data[idx]
        while node:
            if node.key == key:
                node.val = value
                return
            node = node.next

        new_node = ListNode(key, value)
        new_node.next = self.data[idx]   // 头插法
        self.data[idx] = new_node
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        node = self.data[key % self.capacity]
        while node:
            if node.key == key:
                return node.val
            node = node.next
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        node = self.data[key % self.capacity]
        if node and node.key == key:
            self.data[key % self.capacity] = node.next
            return
        
        pre = None
        while node:
            if node.key == key:
                pre.next = node.next
                return
            pre = node
            node = node.next
'''