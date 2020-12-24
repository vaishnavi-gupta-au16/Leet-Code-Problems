"""
238. Product of Array Except Self

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]

Link - https://leetcode.com/problems/product-of-array-except-self/

"""
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [1]*len(nums)
        answer[0] = 1
        for i in range(1, len(nums)):
            answer[i] = answer[i-1] * nums[i-1]
            rightProduct = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] = answer[i] * rightProduct
            rightProduct *= nums[i]
        return answer