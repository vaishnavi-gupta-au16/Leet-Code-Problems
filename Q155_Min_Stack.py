"""
155. Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

link - https://leetcode.com/problems/min-stack/

"""
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        self.min = list()
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if not self.stack or x < self.min[-1]:
            self.min.append(x)
        else:
            self.min.append(self.min[-1])
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack = self.stack[:-1]
        self.min = self.min[:-1]

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if not self.min: return None
        return self.min[-1]