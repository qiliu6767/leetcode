class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        You are climbing a stair case. It takes n steps to reach to the top.
		Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
        """
#         if n == 1:
#             return 1
#         if n == 2:
#             return 2
        
#         return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        a = 1
        b = 2
        if n == 1:
            return 1
        
        if n == 2:
            return 2
        
        for i in range(n - 2):
            a, b = b, a + b
            
        return b