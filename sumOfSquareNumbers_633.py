class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if c == 0:
            return True
        
        factor_lst = self.all_prime_factors(c)
        factor_times = collections.Counter(factor_lst)
        for factor in factor_times:
            if factor % 4 == 3 and factor_times[factor] % 2 == 1:
                return False
        
        return True
        
    
    def all_prime_factors(self, n):
        res = []
        while n % 2 == 0:
            res.append(2)
            n /= 2
        
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0:
                res.append(i)
                n /= i
        
        if n > 2:
            res.append(n)
        
        return res
    