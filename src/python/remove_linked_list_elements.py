'''
Remove all elements from a linked list of integers that have value val.

https://leetcode.com/problems/remove-linked-list-elements/
'''

'''

I. Recursive

public ListNode removeElements(ListNode head, int val) {
    if(head == null) return null;
    ListNode next = removeElements(head.next, val);
    if(head.val == val) return next;
    head.next = next;
    return head;
}

II. Iteration


'''