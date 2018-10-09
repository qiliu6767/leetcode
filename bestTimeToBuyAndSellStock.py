# -*- coding: utf-8 -*

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        current_max = 0
        final_max = 0
        for i in range(1, len(prices)):
            current_max += prices[i]  - prices[i - 1]
            current_max = max(0, current_max)
            final_max = max(final_max, current_max)
        
        return final_max

# current_max刻画了截止到日期，正数差值，而final_max则刻画了最大的正数差值
