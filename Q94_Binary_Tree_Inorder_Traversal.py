"""
94. Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' values.
Example 1:

Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []

link - https://leetcode.com/problems/binary-tree-inorder-traversal/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ans = []
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return
        self.inorderTraversal(root.left)
        self.ans.append(root.val)
        self.inorderTraversal(root.right)
        return(self.ans)


