"""
75. Sort Colors

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Follow up:

Could you solve this problem without using the library's sort function?
Could you come up with a one-pass algorithm using only O(1) constant space?
 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Link - https://leetcode.com/problems/sort-colors/
"""
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n):
            min_ele = nums[i]
            min_ele_idx = i
        
            for idx in range(i, len(nums)):
                if nums[idx] < min_ele:
                    min_ele = nums[idx]
                    min_ele_idx = idx
            nums[i], nums[min_ele_idx] = nums[min_ele_idx], nums[i]
        return nums