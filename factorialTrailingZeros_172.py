# -*- coding: utf-8 -*-

class Solution(object):
    
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        Given an integer n, return the number of trailing zeroes in n!.

		Example 1:
		Input: 3
		Output: 0
		Explanation: 3! = 6, no trailing zero.
		
		Example 2:
		Input: 5
		Output: 1
		Explanation: 5! = 120, one trailing zero.
        """
        res = 0
        i = 5
        while i <= n:
            res += n / i
            i *= 5
        return res

# 需要注意的是，不只要查看5对应于1个零，25对应于2个零，125对应于3个零，等等。
# 算由5生成的0时，由25生成的0已经计数过一遍，所以算25生成的0时，只需要再加一遍就可以。
# 计数125生成的0类似。