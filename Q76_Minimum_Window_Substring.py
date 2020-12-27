"""
76. Minimum Window Substring

Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Example 2:

Input: s = "a", t = "a"
Output: "a"

https://leetcode.com/problems/minimum-window-substring/
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        l,r,i,j,missing = 0,0,0,0, len(t)
        while r < len(s):
            if need[s[r]] >0:
                missing -=1
            need[s[r]]-=1 
            r+=1
                
            while missing == 0:
                if j==0 or r-l < j-i:
                    i,j=l,r
                need[s[l]]+=1
                if need[s[l]]>0:
                    missing +=1
                l += 1
        return s[i:j]