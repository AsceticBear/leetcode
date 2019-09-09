'''
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
'''

'''
I.

l = ['13', '5', '2']

list zip(l, l[1:]) = list zip(['13', '5', '2'], ['5', '2'])

input: [5, 2, 13] 

list: [
        TreeNode{val: 13, left: None, right: None}, 
        TreeNode{val: 5, left: TreeNode{val: 2, left: None, right: None}, right: TreeNode{val: 13, left: None, right: None}}, 
        TreeNode{val: 2, left: None, right: None}
    ]
    [
        TreeNode{val: 5, left: TreeNode{val: 2, left: None, right: None}, right: TreeNode{val: 13, left: None, right: None}}, 
        TreeNode{val: 2, left: None, right: None}
    ]

out put: [18, 20, 13]


def convertBST(self, root: TreeNode) -> TreeNode:
        def reverse(root):
            return reverse(root.right) + [root] + reverse(root.left) if root else []
        for a, b in zip(reverse(root), reverse(root)[1:]):    // 这个招式太牛逼了
            b.val += a.val
        return root
'''
