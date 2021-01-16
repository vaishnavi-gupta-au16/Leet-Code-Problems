"""
215. Kth Largest Element in an Array

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

link - https://leetcode.com/problems/kth-largest-element-in-an-array/

"""
class Solution(object):
    def findKthLargest(self, nums, k):
	for i in range(len(nums)): 
		nums[i] = nums[i]*-1
	heapq.heapify(nums)

	i = 1
	while i < k:
		heapq.heappop(nums)
		i += 1

	return -1*heapq.heappop(nums)