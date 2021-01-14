"""
938. Range Sum of BST

Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].

Example 1:

Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23

link - https://leetcode.com/problems/range-sum-of-bst/

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root, L, R):
        if not root:
            return 0;

        if R < root.val:
            return self.rangeSumBST(root.left, L, R)
        elif L > root.val:
            return self.rangeSumBST(root.right, L, R)
        else:
            return self.rangeSumBST(root.left, L, R) + root.val + self.rangeSumBST(root.right, L, R)
        