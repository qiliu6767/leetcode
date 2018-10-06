class Solution(object):
	'''
	Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

	An input string is valid if:

	Open brackets must be closed by the same type of brackets.
	Open brackets must be closed in the correct order.
	Note that an empty string is also considered valid.
	'''
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        
        left = ["{", "[", "("]
        right = ["}", "]", ")"]
        p_dict = {"{": "}", "[": "]", "(": ")"}
        
        s_left = []
        for p in s:
            if p in left:
                s_left.append(p)
            elif p in right:
                if not s_left:
                    return False
                if p_dict[s_left[-1]] == p:
                    s_left.pop()
                else:
                    return False
        return not s_left