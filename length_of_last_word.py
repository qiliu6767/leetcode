class Solution(object):
    def lengthOfLastWord(self, s):
        """
        Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
        If the last word does not exist, return 0.
        Note: A word is defined as a character sequence consists of non-space characters only.
        """
        # Remove all the blanks in the end of s
        s = s.strip()
        
        if not s:
            return 0
        
        length = 0
        for i in range(len(s))[::-1]:
            if s[i] != ' ':
                length += 1
            else:
                break
        return length

