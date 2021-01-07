"""
144. Binary Tree Preorder Traversal

Given the root of a binary tree, return the preorder traversal of its nodes' values.
Example 1:


Input: root = [1,null,2,3]
Output: [1,2,3]
Example 2:

Input: root = []
Output: []
Example 3:

link - https://leetcode.com/problems/binary-tree-preorder-traversal/

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.ans = []
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return
        self.ans.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
        return(self.ans)
