import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        Given a string, determine if it is a palindrome, considering only alphanumeric characters and             ignoring cases.
        """
        if not s:
            return True
        
        s = s.lower() # Change all characters into lower case
        s = re.sub('\W+', '', s) # Remove all the special characters
        
        return s == s[::-1]
        