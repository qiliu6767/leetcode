# -*- coding: utf-8 -*

class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if count > 0:
                    return False
                if i > 1 and nums[i] < nums[i - 2]:
                    nums[i] = nums[i - 1]
                count += 1
        return True

# 如果要进行"if i > 1 and nums[i] < nums[i - 1]"这一步，首先要保证之前的count = 0 



