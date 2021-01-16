"""
350. Intersection of Two Arrays II

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

link - https://leetcode.com/problems/intersection-of-two-arrays-ii/submissions/
"""
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        l1=len(nums1)
        l2=len(nums2)
        lst=[]
        if l1>l2:
            for i in range(l2):
                if nums2[i] in nums1:
                    lst.append(nums2[i])
                    nums1.pop(nums1.index(nums2[i]))
        else:
            for i in range(l1):
                if nums1[i] in nums2:
                    lst.append(nums1[i])
                    nums2.pop(nums2.index(nums1[i]))
        return lst