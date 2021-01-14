"""
328. Odd Even Linked List

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL

link - https://leetcode.com/problems/odd-even-linked-list/
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        for_odd = ListNode(0)
        for_even = ListNode(0)
        odd_Head = for_odd
        even_Head = for_even
        
        isodd = True
        while head:
            if isodd:
                for_odd.next = head
                for_odd = for_odd.next
            else:
                for_even.next = head
                for_even = for_even.next
            isodd = not isodd
            head = head.next
        for_even.next = None
        for_odd.next = even_Head.next
        
        return odd_Head.next
            
            
        