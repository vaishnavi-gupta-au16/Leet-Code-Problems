"""
230. Kth Smallest Element in a BST

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

 

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3

link - https://leetcode.com/problems/kth-smallest-element-in-a-bst/solution/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def kthSmallest(self, root: TreeNode, k: int) -> int:
		def do(main):
			if main==None or self.ans!=None:
				return 
			do(main.left)
			self.count-=1
			if self.count==0:
				self.ans=main.val
			do(main.right)
		self.count=k
		self.ans=None
		do(root)
		return self.ans
        