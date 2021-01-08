"""
42. Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
 
Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
link - https://leetcode.com/problems/trapping-rain-water/
"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        total_water_trapped = 0
        
        
        for idx, h in enumerate(height):
            max_value_right = float("-inf")
            for i in range(idx + 1, n):
                if height[i] > max_value_right:
                    max_value_right = height[i]
            max_value_left = float("-inf")
            for i in range(0 , idx):
                if height[i] > max_value_left:
                    max_value_left = height[i]
                    
            water_trapped = min (max_value_right, max_value_left) - height[idx]
            if water_trapped > 0:
                total_water_trapped += water_trapped
        return total_water_trapped