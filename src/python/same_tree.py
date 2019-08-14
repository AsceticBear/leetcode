'''
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
'''


# Add code here

'''
分析：

1. 第一种方式

递归， 从根节点开始，查看 p 和 q 节点是否为 None，如果为空，查看 p 是否等于 q，如果相同，分别递归调用左子树和右子树。

2. 第二种方式

迭代

其他:

树的存储结构：

* 双亲表示法

    #define MAX_TREE_SIZE 100
    typedef int  ElemeType;

    typedef struct PTNode{ // 结点结构
        ElemeType data; //结点数据
        int parent;    // 双亲位置
    }PTNode;

    typedef struct { // 树结构
        PTNode nodes[MAX_TREE_SIZE];   // 结点数组
        int r; // 根的位置
        int n; // 结点数
    }PTree;

特点：
    1. 由于根结点是没有双亲的，约定根结点的位置位置域为-1.
    2. 根据结点的parent指针很容易找到它的双亲结点。所用时间复杂度为O(1)，直到parent为-1时，表示找到了树结点的根。
    3. 缺点：如果要找到孩子结点，需要遍历整个结构才行。

* 孩子表示法

把每个节点的孩子用单链表表示出来，如果是叶子节点，则此单链表为空。n 个头指针组成一个线性表，存储在一个一维数组里。

    #define MAX_TREE_SIZE 100
    typedef int  ElemeType;

    typedef struct CTNode{  // 孩子结点
        int child; // 孩子结点的下标
        struct CTNode * next; // 指向下一结点的指针
    }*ChildPtr;

    typedef struct {  // 表头结构
        ElemeType data; // 存放在树中的结点数据
        ChildPtr firstchild; // 指向第一个孩子的指针
    }CTBox;

    typedef struct {  // 树结构
        CTBox nodes[MAX_TREE_SIZE]; // 结点数组
        int r;  // 根的位置
        int n;  // 结点树
    }CTree;

特点：
    1. 便于查找某一个节点的孩子或者兄弟，但要寻找双亲节点的时候，比较麻烦。

可优化为双亲孩子表示法：

    #define MAX_TREE_SIZE 100
    typedef int ElemeType; 

    typedef struct CTNode{  // 孩子结点
        int child;  // 孩子结点的下标
        struct CTNode * next;  // 指向下一结点的指针
    }*ChildPtr; 

    typedef struct {  // 表头结构
        ElemeType data;  // 存放在数中的结点数据
        int parent;      // 存放双亲的下标
        ChildPtr firstchild;  // 指向第一个孩子的指针
    }CTBox; 

    typedef struct {  // 树结构
        CTBox nodes[MAX_TREE_SIZE]; // 结点数组
        int r;  // 根的位置
        int n;  // 结点树
    }CTree; 


* 孩子兄弟表示法
'''

from collections import deque
class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """    
        def check(p, q):
            # if both are None
            if not p and not q:
                return True
            # one of p and q is None
            if not q or not p:
                return False
            if p.val != q.val:
                return False
            return True
        
        deq = deque([(p, q),])
        while deq:
            p, q = deq.popleft()
            if not check(p, q):
                return False
            
            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))
                    
        return True