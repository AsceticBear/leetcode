'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    1. push(x) -- Push element x onto stack.
    2. pop() -- Removes the element on top of the stack.
    3. top() -- Get the top element.
    4. getMin() -- Retrieve the minimum element in the stack.

https://leetcode.com/problems/min-stack/
'''

'''
I. 用语言内置 stack 工具

II. 用列表
class MinStack {
    private Node head;
    
    public void push(int x) {
        if(head == null) 
            head = new Node(x, x);
        else 
            head = new Node(x, Math.min(x, head.min), head);
    }

    public void pop() {
        head = head.next;
    }

    public int top() {
        return head.val;
    }

    public int getMin() {
        return head.min;
    }
    
    private class Node {
        int val;
        int min;
        Node next;
        
        private Node(int val, int min) {
            this(val, min, null);
        }
        
        private Node(int val, int min, Node next) {
            this.val = val;
            this.min = min;
            this.next = next;
        }
    }
}
'''