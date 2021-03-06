"""
145. Binary Tree Postorder Traversal

Given the root of a binary tree, return the postorder traversal of its nodes' values.
Example 1:

Input: root = [1,null,2,3]
Output: [3,2,1]
Example 2:

Input: root = []
Output: []

link - https://leetcode.com/problems/binary-tree-postorder-traversal/
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.ans = []
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return
        self.postorderTraversal(root.left)
        # self.ans.append(root.val)
        self.postorderTraversal(root.right)
        self.ans.append(root.val)
        return(self.ans)

