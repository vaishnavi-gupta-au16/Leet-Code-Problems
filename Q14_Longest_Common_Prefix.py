"""
# Q3. https://leetcode.com/problems/longest-common-prefix/
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        min_len = len(strs[0])
        for i in range(len(strs)):
            min_len = min(len(strs[i]),min_len)
        lcp = ""
        i = 0
        while i < min_len:
            char = strs[0][i]
            for j in range(1,len(strs)):
                if strs[j][i] != char:
                    return lcp
            lcp = lcp + char
            i = i+1
        return lcp