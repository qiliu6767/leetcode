class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1
        while left < right and s[left] == s[right]:
            left += 1
            right -= 1
        
        if left >= right:
            return True
        
        # Remove the first different element from the left
        s_rl = s[:left] + s[(left + 1):]
        
        # Remove the first different element from the right
        s_rr = s[:right] + s[(right + 1):]
        
        return s_rl == s_rl[::-1] or s_rr == s_rr[::-1]
        