"""
349. Intersection of Two Arrays

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]

link - https://leetcode.com/problems/intersection-of-two-arrays/

"""
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        l1 = len(nums1)
        l2 = len(nums2)
        add = []
        if l1 < l2:
            for i in range(l1):
                if nums1[i] in nums2:
                    if nums1[i] not in add:
                        add.append(nums1[i])
        else:
            for i in range(l2):
                if nums2[i] in nums1:
                    if nums2[i] not in add:
                        add.append(nums2[i])
        return add