# -*- coding: utf-8 -*-

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

		Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

		Example 1:

		Input: [1,2,3,1]
		Output: 4
		Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             		 Total amount you can rob = 1 + 3 = 4.
        """
        if not nums:
            return 0
        curr = 0
        prev = 0
        for n in nums:
            prev, curr = curr, max(prev + n, curr)
        return curr

'''
198 题:House Robber 个人理解:
假设 F (i) 表示到 nums 的第 i 个元素为 止，所能抢到的最大的数额，
那么有这样的关系:F(i) = max(F(i − 2) + nums[i], F(i − 1))。
该题的代码中，prev, curr = curr, max(prev+n, curr)， 
等式 curr = max(prev + n, curr) 表示的即是 F(i) = max(F(i − 2) + nums[i],F(i−1))，
而 prev = curr 表示的是将 F(i−1) 的值赋给 F(i−2)， 以此进行循环。
'''
            

