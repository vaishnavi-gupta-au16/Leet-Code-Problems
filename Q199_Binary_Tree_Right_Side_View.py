"""
199. Binary Tree Right Side View

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

link - https://leetcode.com/problems/binary-tree-right-side-view/

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
        
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def collect(node, cur_level):
            if node:
                if cur_level == len(max_level):
                    max_level.append(node.val)
                collect(node.right, cur_level+1)
                collect(node.left, cur_level+1)
        max_level = []
        collect(root, 0)
        return max_level