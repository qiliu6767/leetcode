class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        cnt = 0
        for i in range(L, R + 1):
            if self.is_prime(str(bin(i)).count("1")):
                cnt += 1
        
        return cnt
    
    def is_prime(self, n):
        '''
        Check whether n is a prime number
        '''
        if all(n % i for i in range(2, n)) and n > 1:
            return True
        else:
            return False
    