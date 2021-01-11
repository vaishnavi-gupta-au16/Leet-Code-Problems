"""
662. Maximum Width of Binary Tree

Given a binary tree, write a function to get the maximum width of the given tree. The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

It is guaranteed that the answer will in the range of 32-bit signed integer.

Example 1:

Input: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
Example 2:

Input: 

          1
         /  
        3    
       / \       
      5   3     

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).

link - https://leetcode.com/problems/maximum-width-of-binary-tree/

"""
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        queue = deque([(root, 0)] if root else [])
        max_width = 0
        while queue:
            width = queue[-1][1]-queue[0][1]+1
            max_width = max(max_width, width)
            for _ in range(len(queue)):
                node,val = queue.popleft()
                if node.left:  queue.append((node.left,val*2+1))
                if node.right: queue.append((node.right,val*2+2))
        return max_width