"""
21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a sorted list. 
The list should be made by splicing together the nodes of the first two 
lists.
Example 1:

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: l1 = [], l2 = []
Output: []

Example 3:

Input: l1 = [], l2 = [0]
Output: [0]
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def _init_(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        result = ListNode(0) 
        # result store all the result.
        temp = result 
        # temp store the last node.
        while l1 and l2:
        
        # If any of the list gets completely empty. 
        # directly join all the elements of the other list.
            if l1 is None:
                temp.next = l2
                break
            if l2 is None:
                temp.next = l1
                break
            # Compare the data of the lists and whichever is smaller is 
            # appended to the last of the merged list and the head is changed.
            if l1.val <= l2.val:
                temp.next = ListNode(l1.val)
                l1 = l1.next
            else:
                temp.next = ListNode(l2.val)
                l2 = l2.next
            # Advance the temp.
            temp = temp.next
            
        if l1:
            temp.next = l1
        else:
            temp.next = l2
        # Returns the head of the merged list.
        return result.next