import itertools
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        L = [[i.lower(), i.upper()] if i.isalpha() else i for i in S]
        return [''.join(i) for i in itertools.product(*L)]
    
'''
itertools.product(A, B) returns the same result as
[(x, y) for x in A for y in B]
'''
