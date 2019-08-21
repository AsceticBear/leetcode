'''
Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.

For example, 

Given the tree:
        4
       / \
      2   7
     / \
    1   3

And the value to search: 2
You should return this subtree:

      2     
     / \   
    1   3
'''

# Add code here

'''
分析：

1. while 循环遍历

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None

        node = root
        while node:
            if node.val == val:
                return node
            elif val > node.val:
                node = node.right
            else:
                node = node.left

        return None

2. 递归

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        elif root.val == val:
            return root
        elif val > root.val:
            return self.searchBST(root.right,val)
        else:
            return self.searchBST(root.left,val)

'''