class Solution(object):
    def convertToTitle(self, n):
        """
        168.
        :type n: int
        :rtype: str
        Given a positive integer, return its corresponding column title as appear in an Excel sheet.
        """
        res = ""
        while n > 26:
            n, r = divmod(n, 26)
            if r == 0:
                n -= 1
                r += 26
            res = chr(ord("A") - 1 + r) + res
        res = chr(ord("A") - 1 + n) + res
        
        return res
