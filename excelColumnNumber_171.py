class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        Given a column title as appear in an Excel sheet, return its corresponding column number.
        """
        res = 0
        for i in range(len(s)):
            res += (ord(s[i]) - ord("A") + 1) * (26 ** (len(s) - 1 - i))
        
        return res