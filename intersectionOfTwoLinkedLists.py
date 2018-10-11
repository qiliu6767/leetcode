# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        Write a program to find the node at which the intersection of two singly linked lists begins.
		For example, the following two linked lists:

		A:        a1 → a2
                   		↘
                     	         c1 → c2 → c3
                   		↗            
		B:   b1 → b2 → b3
		begin to intersect at node c1.
        """
        # Get the length of each list
        len_A = self.getlen(headA)
        len_B = self.getlen(headB)
        currA = headA
        currB = headB
        
        # Change the length of currA or currB to make them the same
        if len_A > len_B:
            diff = len_A - len_B
            while diff > 0:
                currA = currA.next
                diff -= 1
        
        if len_A < len_B:
            diff = len_B - len_A
            while diff > 0:
                currB = currB.next
                diff -= 1
        
        # Find the node where intersection begins
        while currA:
            if currA == currB:
                return currA
            else:
                currA = currA.next
                currB = currB.next
        
        return None
    
    def getlen(self, node):
        '''
        Get the length of the given list
        '''
        len_node = 0
        while node != None:
            len_node += 1
            node = node.next
        return len_node
