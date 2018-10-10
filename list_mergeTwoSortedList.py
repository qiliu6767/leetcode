# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        Merge two sorted linked lists and return it as a new list. The new list should be made by splicing         together the nodes of the first two lists.
        """
        dummy = ListNode(0) 
        mergedList = dummy
        
        while (l1 and l2):
            if l1.val <= l2.val:
                mergedList.next = l1
                l1 = l1.next
                mergedList = mergedList.next
            elif l1.val > l2.val:
                mergedList.next = l2
                l2 = l2.next
                mergedList = mergedList.next
                
        if l1:
            mergedList.next = l1
        else:
            mergedList.next = l2
        
        return dummy.next 