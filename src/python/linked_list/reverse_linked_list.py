'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        prev = None
        while(cur):
            tmp = prev 
            prev = ListNode(cur.val)
            prev.next = tmp
            
            cur = cur.next

        return prev
    
    def reverseList_recurisive(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head
        
        sub = self.reverseList_recurisive(head.next)
        head.next.next = head
        head.next = None
        return sub


    def print_linked_list(self, head: ListNode):
        t = head
        while(t):
            print(t.val)
            t = t.next



if __name__ == '__main__':
    s = Solution()
    print('################################ example1:')
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    # s.print_linked_list(s.reverseList(node1))
    s.print_linked_list(s.reverseList_recurisive(node1))
