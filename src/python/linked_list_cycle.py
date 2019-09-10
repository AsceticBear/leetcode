'''
Given a linked list, determine if it has a cycle in it.

https://leetcode.com/problems/linked-list-cycle/solution/
'''

'''
I. Hash Table

如果有循环的话，遍历一定会重复某一个节点，用 hash table，如果两次经过同一个节点，自然有循环。

public boolean hasCycle(ListNode head) {
    Set<ListNode> nodesSeen = new HashSet<>();
    while (head != null) {
        if (nodesSeen.contains(head)) {
            return true;
        } else {
            nodesSeen.add(head);
        }
        head = head.next;
    }
    return false;
}

II. Two Points

快慢两个指针。如果没有循环，快的指针一定会第一个到终点。如果有循环，快的指针一定会追上慢的指针。

public boolean hasCycle(ListNode head) {
    if (head == null || head.next == null) {
        return false;
    }
    ListNode slow = head;
    ListNode fast = head.next;
    while (slow != fast) {
        if (fast == null || fast.next == null) {
            return false;
        }
        slow = slow.next;
        fast = fast.next.next;
    }
    return true;
}

'''