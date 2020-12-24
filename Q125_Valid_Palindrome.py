"""
125. Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

Link - https://leetcode.com/problems/valid-palindrome/

"""
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = s.strip().lower()
        temp_string = ""
        if s == "":
            return True
        
        else:
            for i in s:
                if i.isalnum():
                    temp_string += i
                    
            return temp_string == temp_string[::-1]