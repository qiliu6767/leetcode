class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        res = collections.defaultdict(int) # The format of value is int, initiated as 0
        for string in A:
            even = "".join(sorted(string[0::2]))
            odd = "".join(sorted(string[1::2]))
            
            res[(even, odd)] += 1
        
        return len(res)
    
    
"""
If two strings are special-equivalent, 
then they are the same after exchaning several characters with the locations of the same parity, 
which is to say, when the characters at location with same parity are sorted, 
they should be the same. 
"""