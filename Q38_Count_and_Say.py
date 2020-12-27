"""
38. Count and Say

The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of groups so that each group is a contiguous section all of the same character. Then for each group, say the number of characters, then say the character. To convert the saying into a digit string, replace the counts with a number and concatenate every saying.

For example, the saying and conversion for digit string "3322251":

Example 1:

Input: n = 1
Output: "1"
Explanation: This is the base case.

Q2. https://leetcode.com/problems/count-and-say/
"""

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ini = '1'
        post = ''
        for i in range(n-1):
            cur_digit,count = ini[0],1
            for i in range(1,len(ini)+1):
                if i == len(ini):
                    post += str(count) + ini[i-1]
                elif ini[i] != cur_digit:
                    post += str(count) + cur_digit
                    cur_digit = ini[i]
                    count = 1
                else:
                    count += 1
            ini,post=post,''
        return ini

  
