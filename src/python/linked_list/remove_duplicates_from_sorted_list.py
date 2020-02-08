'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        t = head
        while(t):
            if t.next and t.val == t.next.val:
                if t.next.next:
                    t.next = t.next.next
                    continue
                else:
                    t.next = None
            print("===> ", t.val)
            t = t.next
        
        return head


if __name__ == "__main__":
    s = Solution()
    
    print("################################ example1: ")
    n_1 = ListNode(1);
    n_1_1 = ListNode(1);
    n_2 = ListNode(2);

    n_1.next = n_1_1;
    n_1_1.next = n_2;
    s.deleteDuplicates(n_1);

    print("################################ example2: ")
    node_1 = ListNode(1);
    node_1_1 = ListNode(1);
    node_2 = ListNode(2);
    node_3 = ListNode(3);
    node_3_1 = ListNode(3);

    node_1.next = node_1_1
    node_1_1.next = node_2
    node_2.next = node_3
    node_3.next = node_3_1
    s.deleteDuplicates(node_1)

    print("################################ example3: ")
    n_1 = ListNode(1);
    n_1_1 = ListNode(1);
    n_1_2 = ListNode(1);

    n_1.next = n_1_1;
    n_1_1.next = n_1_2;
    s.deleteDuplicates(n_1);