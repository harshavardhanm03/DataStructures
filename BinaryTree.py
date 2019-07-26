# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 15:17:11 2019

@author: harsh
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class Solution:
    def preorderTraversal(self,root):
        stack=[root]
        print(stack)
        res=[]
        while(stack):
            node=stack.pop()
            print(res)
            if(node!=None):
                res.append(node.data)
                stack.append(node.left)
                stack.append(node.right)
                print(res)
                print("iteration")
        return res

root=Node(10)
root.left=Node(6)
root.right=Node(5)
root.left.left=Node(9)
root.left.right=Node(7)
root.right.right=Node(2)
#root.right.left=Node(3)

solution=Solution()
solution.preorderTraversal(root)


""""

    10
   / \
   6  5
  /\  /\
 9 7  2 3



""""



def isPowerOfThree(n):
        if(n==0):
            return False
        while(n>0):
            if(n==1):
                return True
            print(n)
            n=n/3
        return False
isPowerOfThree(3**250)

print(3//2)


solution=Solution1()
solution.inorder(root)

