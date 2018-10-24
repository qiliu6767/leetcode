class Solution(object):
    def isPalin(self, num):
        '''
        Check whether n is a palindrome
        '''
        s = str(num)
        return s == s[::-1]
        
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        palin_lst = []
        for i in range(10 ** (n - 1), 10 ** n)[::-1]:
            for j in range(10 ** (n - 1), 10 ** n)[::-1]:
                prod = i * j
                if self.isPalin(prod):
                	palin_lst.append(prod)
        return max(palin_lst) % 1337

soln = Solution()
print(soln.largestPalindrome(n = 3))
