class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        Write a function that takes a string as input and reverse only the vowels of a string.
        """
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        stack = []
        for ch in s:
            if ch in vowels:
                stack.append(ch)
        
        s_lst = list(s)
        for i, ch in enumerate(s_lst):
            if ch in vowels:
                s_lst[i] = stack.pop()
        
        return "".join(s_lst)

# The application of stack
# String does NOT accept value assignment
