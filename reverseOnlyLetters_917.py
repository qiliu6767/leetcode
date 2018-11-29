import re

class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        # Extract all the letters and reverse them
        S_letters = iter("".join(re.findall("[a-zA-Z]+", S))[::-1])
        
        res = ""
        for i in range(len(S)):
            if S[i].isalpha():
                res += next(S_letters)
            else:
                res += S[i]
        
        return res
    
        
        