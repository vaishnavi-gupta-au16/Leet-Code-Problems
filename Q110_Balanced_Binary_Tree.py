"""
110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
link - https://leetcode.com/problems/balanced-binary-tree/

"""

class Solution(object):
    def isBalanced(self, root):
        def balanced(node):

            if not node:
                return 0

            left_depth = balanced(node.left)
            right_depth = balanced(node.right)

            if left_depth == -1 or right_depth == -1:
                return -1
            if abs(left_depth - right_depth) > 1:
                return -1

            return 1 + max(left_depth, right_depth)

        return balanced(root) != -1