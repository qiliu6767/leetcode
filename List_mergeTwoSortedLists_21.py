# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Special cases
        if not l1:
            return l2
        if not l2:
            return l1
        if not l1 and not l2:
            return 
        
        head = ListNode(0) # Initialize a new linked list to store result
        cur = head # Initialize a pointer
        while l1 and l2:
            if l1.val > l2.val:
                cur.next = ListNode(l2.val)
                l2 = l2.next
            elif l1.val <= l2.val:
                cur.next = ListNode(l1.val)
                l1 = l1.next
            
            cur = cur.next # "cur" is now at the newly generated node, with its next = None
        
        if l1 is None:
            cur.next = l2
        if l2 is None:
            cur.next = l1
        
        return head.next