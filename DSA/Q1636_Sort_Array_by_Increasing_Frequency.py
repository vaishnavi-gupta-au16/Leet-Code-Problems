"""
1636. Sort Array by Increasing Frequency

Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.

 

Example 1:

Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.

link - https://leetcode.com/problems/sort-array-by-increasing-frequency/
"""
class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if (len(s)) != (len(t)):
            return False
        
        s = sorted(s)
        t = sorted(t)
        
        for i in range(0, len(s)):
            if s[i] != t[i]:
                return False
        return True 

                