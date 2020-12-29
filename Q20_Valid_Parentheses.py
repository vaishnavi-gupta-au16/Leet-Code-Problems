"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true

Link - https://leetcode.com/problems/valid-parentheses/
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = list()
        for c in s :
            if c == "(":
                stack.append(c)
            elif c == "[":
                stack.append(c)
            elif c == "{":
                stack.append(c)
            elif c == ")" and stack[-1] == "(":
                stack.pop()
            elif c == "]" and stack[-1] == "[":
                stack.pop()
            elif c == "}" and stack[-1] == "{":
                stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        return False
            
    
        











