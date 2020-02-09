'''
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

https://leetcode.com/problems/middle-of-the-linked-list/
'''

'''
I. 快慢指针

快指针的速度是慢指针速度的两倍，那么快指针到达终点的时候，慢指针就在中点的位置了。

class Solution(object):
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

II. 数组

把单链表的数据迭代循环放置在数组里，最后由数组输出。

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ll = [head]
        while ll[-1].next:
            ll.append(ll[-1].next)
        print(ll[len(ll)//2]) 
        
'''