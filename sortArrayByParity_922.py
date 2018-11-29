class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # Method 1:
        # Create a list with odd numbers of A
        odd = iter([i for i in A if i % 2 == 1])
        
        # Create a list with even numbers of A
        even = iter([i for i in A if i % 2 == 0])
        
        res = []
        for i in range(len(A)):
            # Even location
            if i % 2 == 0:
                try:
                    res.append(next(even))
                except StopIteration:
                    break
            elif i % 2 == 1:
                try:
                    res.append(next(odd))
                except StopIteration:
                    break
        return res

        # Method 2
        odd = [a for a in A if a % 2 == 1]
        even = [a for a in A if a % 2 == 0]
        
        res = [even.pop() if i % 2 == 0 else odd.pop() for i in range(len(A))]
        
        return res