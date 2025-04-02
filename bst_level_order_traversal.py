'''
Created on Apr 1, 2025

@author: bigcv
'''

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        q = []
        if root is not None:
            q.append(root)
        i = 0
        while i < len(q):
            n = q[i]
            if n.left is not None:
                q.append(n.left)
            if n.right is not None:
                q.append(n.right)
            i += 1
        print(" ".join(str(x.data) for x in q))

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)

