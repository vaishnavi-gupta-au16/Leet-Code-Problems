"""
897. Increasing Order Search Tree

Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

 

Example 1:


Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

link - https://leetcode.com/problems/increasing-order-search-tree/

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
            
        self.nodes = []
        self.inorder(root)
        
        if self.nodes:
            tn = TreeNode(self.nodes.pop(0))
            cur = tn
            
            for _ in range(len(self.nodes)):
                cur.right = TreeNode(self.nodes.pop(0))
                cur = cur.right
                
            return tn
        else:
            return self.nodes
        
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.nodes.append(root.val)
            self.inorder(root.right)
        