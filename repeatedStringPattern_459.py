class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        Given a non-empty string check if it can be constructed 
        by taking a substring of it and appending multiple copies of the substring together.
		
		Input: "abab"
		Output: True
		Explanation: It's the substring "ab" twice.

        :type s: str
        :rtype: bool

        """
        # One-line solution
        # return s in (s+s)[1:-1]
        
        # Regular solution
        # Find all possible substring lengths which are factors of len(s)
        check_list = []
        for i in range(1, int(math.ceil(len(s) / 2)) + 1):
            if len(s) % i == 0:
                check_list.append(i)
        
        # Check whether or not the string determined by a particular length can be repeated to get s
        for j in check_list:
            if s[:j] * int(math.ceil(len(s) / j)) == s:
                return True
        
        return False